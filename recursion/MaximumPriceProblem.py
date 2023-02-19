class Innoskrit:
    
    def solve(price, start, end, year):
        if(start > end):
            return 0
        
        left = price[start] * year + Innoskrit.solve(price, start + 1, end, year + 1)
        right = price[end] * year + Innoskrit.solve(price, start, end - 1, year + 1)
        
        return max(left, right)
    
    def findProfit(price, n):
        return Innoskrit.solve(price, 0, n - 1, 1)

if __name__ == '__main__':
    price = [2, 3, 5, 1, 4]
    n = 5
    print(Innoskrit.findProfit(price, n))