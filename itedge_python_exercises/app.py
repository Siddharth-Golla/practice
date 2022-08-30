def getMaxRewards(levels, game):
    reward_possibilities = []
    coins = 1

    for i in range(1,levels):
        if game[i] > game[i - 1]:
            coins = coins + 1
        else:
            reward_possibilities.append(coins)
            coins = 1

    return max(reward_possibilities)


if __name__ == "__main__":
    levels = int(input())
    game = list(map(int, input().rstrip().split()))
    print(getMaxRewards(levels, game))