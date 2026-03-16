# FEEL FREE TO ADD MORE FUNCTIONS AS PER YOUR NEED
# THERE IS NO UNCHANGEABLE "MAIN" FUNCTION IN THIS HW

import time
import random

# Implement HashMap in this class
# Do not use built in dictionary
# Implement own hashing function using division/multiplication method
class HashMap:
    def __init__(self, size=101):
        self.size = size
        self.count = 0
        # Array of buckets — each bucket is a list of [key, value] pairs (chaining)
        self.table = [[] for _ in range(self.size)]

    # retrieve a value associated with the key
    def search(self,key):
        index = self._hash(key, method="division")
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        raise KeyError(f"Key '{key}' not found")
        

    # insert the key value pair into the hash tables
    def insert(self,key,value):
        index = self._hash(key, method="division")
        bucket = self.table[index]

        # If key already exists, update the value
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        # Otherwise append a new [key, value] pair to the chain
        bucket.append([key, value])
        self.count += 1

        # Resize if load factor exceeds 0.75
        if self.count / self.size > 0.75:
            self.dynamicResizing()

    # remove the key value pair from the hash table
    def delete(self,key):
        index = self._hash(key, method="division")
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                self.count -= 1
                return pair[1]

        raise KeyError(f"Key '{key}' not found")

    # optional for open addressing collision method
    # if you choose chaining, don't forget to discuss it in the report
    def dynamicResizing(self):
        old_table = self.table
        # Roughly double the size, pick a prime-ish number
        self.size = self.size * 2 + 1
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        # Re-insert every existing key-value pair
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    # hashing methods
    def _hash(self, key, method="division"):
        # Implement division method
        # Implement multiplication method
        # Convert key to an integer regardless of type
        if isinstance(key, int):
            k = abs(key)
        elif isinstance(key, str):
            # Polynomial rolling hash: weighted sum of char codes
            k = 0
            for ch in key:
                k = k * 31 + ord(ch)
        elif isinstance(key, float):
            k = abs(int(key * 1_000_000))
        else:
            k = abs(id(key))

        if method == "division":
            # h(k) = k mod m
            return k % self.size
        elif method == "multiplication":
            # h(k) = floor(m * (k * A mod 1)),  A ≈ (√5 - 1)/2 (Knuth's suggestion)
            A = 0.6180339887498949
            return int(self.size * ((k * A) % 1))
        else:
            raise ValueError(f"Unknown hashing method: {method}")

    # also adding some extra helper functions 
    def __len__(self):
        return self.count

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def __repr__(self):
        items = []
        for bucket in self.table:
            for key, value in bucket:
                items.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(items) + "}"
    

    # this is used later in running different experiments 

    def chain_stats(self):
        lengths = [len(bucket) for bucket in self.table]
        non_empty = [l for l in lengths if l > 0]
        total_slots = self.size
        avg_all = sum(lengths) / total_slots if total_slots else 0
        avg_non_empty = sum(non_empty) / len(non_empty) if non_empty else 0
        max_len = max(lengths) if lengths else 0
        empty_slots = lengths.count(0)
        return {
            "avg_chain_all_slots": avg_all,
            "avg_chain_non_empty": avg_non_empty,
            "max_chain": max_len,
            "empty_slots": empty_slots,
            "total_slots": total_slots,
            "num_keys": self.count,
        }

# Problem 2: Performance Analysis

def generate_keys(distribution, n):
    # uniform, skewed, or sequential
    """Generate n keys following the specified distribution."""
    if distribution == "uniform":
        # Random integers spread across a wide range
        return [random.randint(0, n * 100) for _ in range(n)]

    elif distribution == "skewed":
        # Most keys clustered in a narrow range, few outliers
        keys = []
        for _ in range(n):
            if random.random() < 0.8:
                keys.append(random.randint(0, 50))   # 80% in tight cluster
            else:
                keys.append(random.randint(0, n * 100))  # 20% spread wide
        return keys

    elif distribution == "sequential":
        # Consecutive integers — worst case for naive division hashing
        return list(range(n))

    else:
        raise ValueError(f"Unknown distribution: {distribution}")


def measure_search_time(hashmap, keys, successful=True):
    """
    Measure average search time.
      successful=True  → search for keys that ARE in the table
      successful=False → search for keys that are NOT in the table
    """
    if successful:
        search_keys = keys
    else:
        # Generate keys guaranteed to miss
        max_existing = max(keys) if keys else 0
        search_keys = [max_existing + 1000 + i for i in range(len(keys))]
 
    num_searches = len(search_keys)
    start = time.perf_counter()
    for key in search_keys:
        try:
            hashmap.search(key)
        except KeyError:
            pass
    end = time.perf_counter()
 
    total = end - start
    avg = total / num_searches if num_searches else 0
    return total, avg

def run_experiments():
    # test across different table sizes and load factors
    distributions = ["uniform", "skewed", "sequential"]
    table_sizes = [11, 53, 101, 503, 1009]       # all primes — good for division method
    load_factors = [0.25, 0.50, 0.75, 1.0, 2.0]  # count / table_size
    hash_methods = ["division", "multiplication"]

    print(f"{'Distribution':<14} {'Method':<16} {'Table Size':<12} "
          f"{'Load Factor':<13} {'Num Keys':<10} {'Total (s)':<14} {'Avg (s)':<14}")
    print("-" * 105)

    for dist in distributions:
        for method in hash_methods:
            for size in table_sizes:
                for lf in load_factors:
                    num_keys = int(size * lf)
                    if num_keys == 0:
                        continue

                    keys = generate_keys(dist, num_keys)

                    # Build a hashmap using the chosen hash method
                    hm = HashMap(size=size)
                    # Override _hash to lock in the method for this experiment
                    orig = hm._hash
                    hm._hash = lambda k, method=None, _m=method, _o=orig: _o(k, method=_m)

                    # Insert phase
                    for key in keys:
                        hm.insert(key, key)

                    # Search phase — measure time
                    total_time, avg_time = measure_search_time(hm, keys)

                    print(f"{dist:<14} {method:<16} {size:<12} "
                          f"{lf:<13.2f} {num_keys:<10} {total_time:<14.8f} {avg_time:<14.10f}")

        print()  # blank line between distributions

