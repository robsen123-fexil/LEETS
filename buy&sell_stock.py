class Solution:
    def stock(self, price: list) -> int:
        idn = price.index(min(price))
        res = []

        for i in range(idn, len(price)):
            res.append(price[i])

        lr = res.index(max(res))
        lr += 1
        st = max(res)
        nn = None

        if len(price) >= 2 and price[0] == price[1]:
            return 0

        for i in range(len(price)):
            if len(res) == 1:
                nn = 0
                break
            if price[i] == st:
                nn = price.index(price[i])
                return nn + 1

        if nn is None:
            return 0
        return nn + 1


obj = Solution()
result = obj.stock([1, 2])
print(result)  
