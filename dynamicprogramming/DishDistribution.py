class DishDistribution:

    def solve(dishes, i, cooks, dp):

        if i == len(cooks) and dishes == 0:
            return 1
        
        if i == len(cooks) or dishes <= 0:
            return 0

        if dp[i][dishes] != -1:
            return dp[i][dishes]

        min_dishes = cooks[i][0]
        max_dishes = cooks[i][1]

        count = 0
        for d in range(min_dishes, max_dishes + 1):
            count += DishDistribution.solve(dishes - d, i + 1, cooks, dp)
        dp[i][dishes] = count
        return count

    def distribute(dishes, cno, cooks):
        dp = [[-1 for j in range(dishes + 1)] for i in range(cno)]
        return DishDistribution.solve(dishes, 0, cooks, dp)


if __name__ == '__main__':

    dishes, cno = map(int, input().split())
    cooks = []
    for i in range(cno):
        x, y = map(int, input().split())
        cooks.append([x, y])
    print(DishDistribution.distribute(dishes, cno, cooks))
