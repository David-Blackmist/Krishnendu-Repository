class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        count=0
        for i in costs:
            if i<=coins:
                count +=1
                coins=coins-i
            elif i>coins:
                break
        return count

        