1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left = 0
4        right = len(height) - 1
5        max_water = 0
6
7        while left < right:
8            width = right - left
9            container_height = min(height[left], height[right])
10            water = width * container_height
11
12            max_water = max(max_water, water)
13
14            if height[left] < height[right]:
15                left += 1
16            else:
17                right -= 1
18
19        return max_water