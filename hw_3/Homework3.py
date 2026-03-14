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

# Problem 2: Performance Analysis

def generate_keys(distribution, n):
    # uniform, skewed, or sequential
    pass

def measure_search_time(hashmap, keys):
    # use time.perf_counter()
    pass

def run_experiments():
    # test across different table sizes and load factors
    pass