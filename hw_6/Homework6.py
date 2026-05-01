import csv
import ast  # For safely evaluating string representation of list

class Homework6:
    #Question 1 Number of Islands
    def countIslandsUsingDFS(self, grid):
        pass

    def countIslandsUsingBFS(self, grid):
        pass

    def countIslandsUsingDFSUsingStack(self, grid):
        pass

    def performanceAnalysis(): # optional
        pass

# DO NOT MODIFY THE CODE BELOW THIS LINE

if __name__ == "__main__":
    homework6 = Homework6()
    testCasesforQuestion1 = []

    try:
        with open('testcases1.csv', 'r') as file:
            testCases = csv.reader(file)
            for row in testCases:
                if len(row) == 2:
                    testCasesforQuestion1.append(row)
    except FileNotFoundError:
        print("File Not Found")
    print("RUNNING TEST CASES FOR NUMBER OF ISLANDS:")
    for row_num, (inputValue, expectedOutput) in enumerate(testCasesforQuestion1, start=1):
        try:
            inputGrid = ast.literal_eval(inputValue.strip())
            expectedOutput = int(expectedOutput.strip())
            actualOutputDFS = homework6.countIslandsUsingDFS(inputGrid)
            if actualOutputDFS == expectedOutput:
                print(f"Test Case {row_num}: PASSED Using DFS")
            else:
                print(f"Test Case {row_num}: FAILED (Expected: {expectedOutput}, Got: {actualOutputDFS}) Using DFS")
            actualOutputBFS = homework6.countIslandsUsingBFS(inputGrid)
            if actualOutputBFS == expectedOutput:
                print(f"Test Case {row_num}: PASSED Using BFS")
            else:
                print(f"Test Case {row_num}: FAILED (Expected: {expectedOutput}, Got: {actualOutputBFS}) Using BFS")
            actualOutputDFSUsingStack = homework6.countIslandsUsingDFSUsingStack(inputGrid)
            if actualOutputDFSUsingStack == expectedOutput:
                print(f"Test Case {row_num}: PASSED Using DFS Stack")
            else:
                print(f"Test Case {row_num}: FAILED (Expected: {expectedOutput}, Got: {actualOutputDFSUsingStack}) Using DFS STack")

        except Exception as e:
            print(f"Test Case {row_num}: ERROR - {e}")
