class Character :

    #클래스는 속성을 갖고 있고
    #캐릭터를 예로들면 속성 - 그 캐릭터를 위한 능력치 같은것
    #HP,MP, 물공,마공




    #클래스는 기능을 갖고 있다.
    #캐릭터를 예로들면 기능 - 공격,이동,대화하기,길드 가입하기,...



def attack(monsterHP, warrior물리공격력):
    # 공격을 하기 위한 모션 (그래픽처리 )
    monsterHP = monsterHP - warrior물리공격력

    return monsterHP
    # 공격을 받은 모션(그래픽처리)


def move():
    pass


def say():
    pass


def buy():
    pass


def exit():
    pass

#플레이어블캐릭터 틀을 만들어 노혹
#그 틀을 사용해서
#전사의 능력치를 갖고 있는 캐릭터
#궁수의 능력치를 갖고 있는 캐릭터
#찍어낼 수 있음


#전사캐릭터

warriorHP = 100
warriorMP = 50
warrior물리공격력 = 15.4
warrior마법공격력 = 5

archerHP = 75
archerMP = 75
archer물리공격력 = 17
warrior마법공격력 = 10