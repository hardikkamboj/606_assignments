import csv
import random
import sys
import time
import tracemalloc

class Homework4:

    # QUESTION 1
    # Implement randomized quicksort and heapsort in the below function
    # Input for the function - an array of floating point numbers ex: [3.0,9.0,1.0]
    # Output - sorted list of numbers ex: [1.0,3.0,9.0]
    # Numbers can be negative, repeated, and floating point numbers
    # DO NOT USE THE INBUILT HEAPQ MODULE TO SOLVE THE PROBLEMS
    def randomQuickSort(self,nums:list) -> list:
        # Todo: Implement randomized quicksort
        """
        Entry point for the Randomized Quicksort algorithm.
        Creates a copy of the input to ensure the original list remains 
        unchanged, then initiates the recursive sorting process.
        """
        result = nums[:]
        self._quick_sort_helper(result, 0, len(result) - 1)
        return result

    def _quick_sort_helper(self, arr, low, high):
        if low >= high:
            return
        split_pos = self._partition_random(arr, low, high)
        self._quick_sort_helper(arr, low, split_pos - 1)
        self._quick_sort_helper(arr, split_pos + 1, high)

    def _partition_random(self, arr, low, high):
        """
        Randomly selects a pivot, moves it to the front,
        then scans right-to-left to group elements around it.
        Returns the pivot's final sorted position.
        """
        # Pick a random element and swap it to the front
        hi = high
        chosen = random.randint(low, hi)
        arr[low], arr[chosen] = arr[chosen], arr[low]

        pivot_val = arr[low]
        wall = hi + 1

        # Walk backwards, pushing elements >= pivot toward the right end
        for cursor in range(hi, low, -1):
            if arr[cursor] >= pivot_val:
                wall -= 1
                arr[cursor], arr[wall] = arr[wall], arr[cursor]

        # Drop the pivot into its correct slot
        wall -= 1
        arr[low], arr[wall] = arr[wall], arr[low]
        return wall



    def heapSort(self,nums:list) -> list:
        # Todo: Implement heapsort
        data = nums[:]
        length = len(data)

        # Phase 1 — construct the max-heap from the bottom up
        k = length // 2 - 1
        while k >= 0:
            self._heapify(data, length, k)
            k -= 1

        # Phase 2 — extract max one at a time
        end = length - 1
        while end > 0:
            data[0], data[end] = data[end], data[0]
            self._heapify(data, end, 0)
            end -= 1

        return data

    def _heapify(self, data, size, root):
        """
        Iterative sift-down that enforces the max-heap invariant
        for the subtree rooted at index 'root'.
        """
        pos = root
        while True:
            lc = 2 * pos + 1
            rc = 2 * pos + 2
            top = pos

            if lc < size and data[lc] > data[top]:
                top = lc
            if rc < size and data[rc] > data[top]:
                top = rc

            if top == pos:
                break

            data[pos], data[top] = data[top], data[pos]
            pos = top

    def __init__(self):
        # Flag to ensure the performance analysis only runs once
        self.analysis_run = False

    # --- PROBLEM 3: PERFORMANCE ANALYSIS METHOD ---
    def run_performance_analysis(self):
        """
        Satisfies Problem 3: Varying N, measuring time/memory, 
        and handling RecursionErrors.
        """
        print("\n" + "="*50)
        print("PROBLEM 3: PERFORMANCE ANALYSIS REPORT")
        print("="*50)
        
        # Test sizes: adjust these if they run too fast/slow on your machine
        sizes = [10000, 100000, 500000, 1000000]
        
        for n in sizes:
            # Generate random floating point numbers
            data = [random.uniform(-1000.0, 1000.0) for _ in range(n)]
            print(f"\n--- Testing Input Size N = {n} ---")
            
            # Test both algorithms
            for algo_name, algo_func in [("QuickSort", self.randomQuickSort), ("HeapSort", self.heapSort)]:
                # Use a flag to prevent infinite recursion when calling from within itself
                self.analysis_run = True 
                
                tracemalloc.start()
                start_time = time.perf_counter()
                
                try:
                    # Pass a copy to keep inputs consistent
                    algo_func(list(data))
                    duration = time.perf_counter() - start_time
                    _, peak_mem = tracemalloc.get_traced_memory()
                    print(f"{algo_name:10} | Time: {duration:8.4f}s | Peak Memory: {peak_mem / 10**6:6.2f} MB")
                
                except RecursionError:
                    print(f"{algo_name:10} | FAILED: RecursionError (N={n} too deep for stack)")
                except Exception as e:
                    print(f"{algo_name:10} | FAILED: {str(e)}")
                finally:
                    tracemalloc.stop()
        
        print("\n" + "="*50 + "\n")



# Main Function
# Do not edit the code below
if __name__=="__main__":
    homework4  = Homework4()
    testCasesforSorting = []
    try:
        with open('testcases.csv','r') as file:
            testCases = csv.reader(file)
            for row in testCases:
                testCasesforSorting.append(row)
    except FileNotFoundError:
        print("File Not Found") 
    
    # Running Test Cases for Question 1
    print("RUNNING TEST CASES FOR QUICKSORT: ")
    
    for row , (inputValue,expectedOutput) in enumerate(testCasesforSorting,start=1):
        if(inputValue=="" and expectedOutput==""):
            inputValue=[]
            expectedOutput=[]
        else:
            inputValue=inputValue.split(" ")
            inputValue = [float(i) for i in inputValue]
            expectedOutput=expectedOutput.split(" ")
            expectedOutput = [float(i) for i in expectedOutput]
        actualOutput = homework4.randomQuickSort(inputValue)
        are_equal = all(x == y for x, y in zip(actualOutput, expectedOutput))
        if(are_equal):
            print(f"Test Case {row} : PASSED")
        else:
             print(f"Test Case {row}: Failed (Expected : {expectedOutput}, Actual: {actualOutput})")
    
    print("\nRUNNING TEST CASES FOR HEAPSORT: ")         
    for row , (inputValue,expectedOutput) in enumerate(testCasesforSorting,start=1):
        if(inputValue=="" and expectedOutput==""):
            inputValue=[]
            expectedOutput=[]
        else:
            inputValue=inputValue.split(" ")
            inputValue = [float(i) for i in inputValue]
            expectedOutput=expectedOutput.split(" ")
            expectedOutput = [float(i) for i in expectedOutput]
        actualOutput = homework4.heapSort(inputValue)
        are_equal = all(x == y for x, y in zip(actualOutput, expectedOutput))
        if(are_equal):
            print(f"Test Case {row} : PASSED")
        else:
             print(f"Test Case {row}: Failed (Expected : {expectedOutput}, Actual: {actualOutput})")
    # Run performance analysis
    homework4.run_performance_analysis()