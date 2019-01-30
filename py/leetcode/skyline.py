class Solution:

    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        new_grid = [[] for x in range(len(grid))]
        max_x = []
        max_y = []
        for y, x in enumerate(grid):
            max_y.append(max(x))
            max_x.append(max([grid[z][y] for z in range(len(grid[0]))]))
        for x in range(len(max_x)):
            for y in range(len(max_y)):
                new_grid[x].append(min(max_x[y], max_y[x]))
        return sum(sum(x) for x in new_grid) - sum(sum(x) for x in grid)
                


print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))

