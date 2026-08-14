class Solution(object):
    def minPrice(self, prices, discounts):
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        total=0
        j=0
        for i in range(len(prices)):
            if j<len(discounts):
                discount =(prices[i])*(discounts[j]/100.0)
                j=j+1
            else:
                discount=0
            total +=prices[i]-discount
        return total

            

        