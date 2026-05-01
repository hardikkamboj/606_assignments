import csv
import ast  # For safely evaluating string representation of list

class Homework6:
    #Question 1 Number of Islands
    def countIslandsUsingDFS(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        # Make a deep-ish copy so we don't mutate the caller's grid
        # (the test harness reuses the same grid across all 3 methods).
        g = [row[:] for row in grid]
        count = 0

        def dfs(r, c):
            # Out of bounds or water/visited -> stop
            if r < 0 or r >= rows or c < 0 or c >= cols or g[r][c] != '1':
                return
            g[r][c] = '0'  # mark visited by sinking the land
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if g[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count

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
