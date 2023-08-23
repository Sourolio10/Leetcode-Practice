def f(day, last, points, dp):
    if day ==0:
        maxi=0
        for i in range(3):
            if i!=last:
                maxi = max(maxi, points[0][i])
        dp[day][last] = maxi
        return dp[day][last]
    maxi =0
    for i in range(3):
        if i!=last:
            activity = points[day][i] + f(day-1, i, points, dp)
            maxi = max(maxi, activity)
    dp[day][last] = maxi
    return dp[day][last]


def ninjaTraining(n, points):
    dp = [[-1 for j in range(4)] for i in range(n)]
    return f(n - 1, 3, points, dp)

def main():
    points = [[10,40,70],
              [20,50,80],
              [30,60,90]]

    n = len(points)
    print(ninjaTraining(n, points))

if __name__ == '__main__':
    main()