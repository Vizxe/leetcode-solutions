# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/description/
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def helper(timeNow, secondStartTime, secondDuration):
            bestTime = 2e15
            for i in range(len(secondStartTime)):
                bestTime = min(bestTime, max(0, secondStartTime[i] - timeNow) + secondDuration[i])
            return bestTime
        
        landFirst = helper(0, landStartTime, landDuration)
        waterFirst = helper(0, waterStartTime, waterDuration)

        landSecond = helper(waterFirst, landStartTime, landDuration)
        waterSecond = helper(landFirst, waterStartTime, waterDuration)

        return min(landFirst + waterSecond, waterFirst + landSecond)