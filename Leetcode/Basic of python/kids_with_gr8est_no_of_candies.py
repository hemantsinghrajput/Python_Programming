class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxm= max(candies)
        ans=[]
        for i in range(len(candies)):
            if(candies[i]+extraCandies >= maxm):
                ans.append(True)
            else:
                ans.append(False)

        return ans