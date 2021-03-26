#열 번 찍어서 안넘어가는 나무없다
import random

nansu = [False,False,False,False,False,False,False,True,False,False]

cutDown = False
hit = 0

while  True:
    cutDown = random.choice(nansu)

    if cutDown :
        print("나무를 쓰러트렸다.")

    else :
        hit += 1
        print("나무를 {0}번 찍었다".format(hit))
    if cutDown != True :

        break
        print("나무는 강하였다")
    elif hit  >= 10:
        break