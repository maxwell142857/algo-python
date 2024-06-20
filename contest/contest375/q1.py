class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        ans = 0
        for item in batteryPercentages:
            if item - ans > 0:
                ans += 1
        return ans