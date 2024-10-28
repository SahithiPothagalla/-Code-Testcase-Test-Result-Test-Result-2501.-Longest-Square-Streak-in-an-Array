class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        jvrc = -1
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = nums[i]
        for i in range(len(nums)):
            curr = nums[i]
            loc = 0
            while(True):
                p = curr*curr
                if p in dic :
                    curr = (curr*curr)
                    loc += 1
                else:
                    break        
            if loc > jvrc and loc!=0 :
                jvrc = loc
        if(jvrc != -1):
            return jvrc+1
        return jvrc  
