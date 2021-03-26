mix=10
price = 300
print("돈넣어라" ,end="")
coffe = int(input())

while True :
    mix -=1
    coffe -= price
    if mix ==0:

        print("믹스커피가 부족함. 반환되는 잔액은 %d원입니다"%coffe)
        break
    elif coffe< price:
        print("잔액이 부족합니다. 반환되는 잔액은 %d원 입니다."% coffe)
        break

