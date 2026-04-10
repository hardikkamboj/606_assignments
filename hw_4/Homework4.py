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
        arr = list(nums)
        self._quick_sort_helper(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort_helper(self, arr, low, high):
        """
        Recursive Divide and Conquer controller.
        It repeatedly partitions the array into smaller segments around a 
        pivot until the segments are reduced to a single element.
        """
        if low < high:
            pivot_index = self._partition_random(arr, low, high)
            # Recursively sort the sub-arrays to the left and right of the pivot
            self._quick_sort_helper(arr, low, pivot_index - 1)
            self._quick_sort_helper(arr, pivot_index + 1, high)

    def _partition_random(self, arr, low, high):
        """
        Randomized Partitioning Logic:
        1. Pivot Selection: Picks a random element and moves it to the end.
           This randomization prevents O(n^2) performance on sorted inputs.
        2. Reordering: Iterates through the segment, moving all elements 
           smaller than the pivot to the left side.
        3. Pivot Placement: Places the pivot in its final, correct sorted 
           position and returns that index.
        """
        # Step 1: Randomize pivot to ensure average-case O(n log n)
        rand_idx = random.randint(low, high)
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
        
        # Step 2: Organize elements around the pivot
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # Step 3: Finalize pivot position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1



    def heapSort(self,nums:list) -> list:
        # Todo: Implement heapsort
        """
        Main Heapsort driver.
        Converts the input list into a Max-Heap structure, then repeatedly
        extracts the largest element to build the sorted array from back to front.
        """
        arr = list(nums)
        n = len(arr)

        # Step 1: Build Max Heap
        # Transforms the array into a heap where every parent is larger than its children.
        # We start from the last non-leaf node and move upwards.
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)

        # Step 2: Extract elements from the heap
        # One by one, move the current root (largest element) to the end of the array,
        # then reduce the heap size and re-heapify the new root.
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap max element to the sorted portion
            self._heapify(arr, i, 0)         # Restore heap property for the remaining items
        
        return arr

    def _heapify(self, arr, n, i):
        """
        Recursive Heap Maintenance (Sift-Down):
        Ensures that the subtree rooted at index 'i' satisfies the Max-Heap 
        property. If a child is larger than the parent, they are swapped, 
        and the process continues down the tree.
        """
        largest = i
        left = 2 * i + 1   # Left child index
        right = 2 * i + 2  # Right child index

        # Check if left child exists and is greater than current largest
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest element is not the parent, swap and recurse
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # Recursively heapify the affected sub-tree
            self._heapify(arr, n, largest)

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