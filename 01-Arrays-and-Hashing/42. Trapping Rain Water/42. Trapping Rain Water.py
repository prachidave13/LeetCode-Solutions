1class Solution:
2    def trap(self, height: List[int]) -> int:
3        left = 0
4        right = len(height) - 1
5
6        left_max = 0
7        right_max = 0
8        total_water = 0
9
10        while left < right:
11            if height[left] < height[right]:
12                left_max = max(left_max, height[left])
13                total_water += left_max - height[left]
14                left += 1
15            else:
16                right_max = max(right_max, height[right])
17                total_water += right_max - height[right]
18                right -= 1
19
20        return total_water