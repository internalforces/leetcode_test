class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        sha = 0
        for row in grid:
            for value in row:
                if value != 0:
                    sha += 1
        
        for row in grid:
            sha += max(row)

        for col in zip(*grid):
            sha += max(col)

        return sha
        
        
        
        