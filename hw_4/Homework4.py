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
        if lo >= hi:
            return
        split_pos = self._partition_random(seq, lo, hi)
        self._quick_sort_helper(seq, lo, split_pos - 1)
        self._quick_sort_helper(seq, split_pos + 1, hi)

    def _partition_random(self, arr, low, high):
        pass 



    def heapSort(self,nums:list) -> list:
        # Todo: Implement heapsort
        pass 

    def _heapify(self, arr, n, i):
        pass 


    # --- PROBLEM 3: PERFORMANCE ANALYSIS METHOD ---
    def run_performance_analysis(self):
        pass 



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