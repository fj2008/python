import random

dice = 0
diceCount = 0

while True:
#while문에 꼭 true가 들어갈 필욘없음
#형식에 얽매일 필요가 없음

    dice = random.randint(1,8)
    diceCount +=1
    print("dice = %d / diceCount = %d" % (dice, diceCount))

    if dice ==5 or diceCount ==8:
        break
