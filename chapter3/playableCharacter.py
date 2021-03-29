class Character :

    #클래스는 속성을 갖고 있고
    #캐릭터를 예로들면 속성 - 그 캐릭터를 위한 능력치 같은것
    #HP,MP, 물공,마공
    #__init__라는 메서드를 정의하고
    #이 메서드 (생성자)안에 클래스가 필요한 속성들을 정의한다.
    #__init__는 생성자라고 부른다
    #생성자 메서드는 우리가 호출할 수 없는 메서드
    #일반적인 arrack과도 같은 메서드는 우리가 호출 할 수 있는 메서드
    def __init__(self):
        self.HP = 0
        self.MP = 0
        self.물리공격력 = 0
        self.마법공격력 = 0


    #클래스는 기능을 갖고 있다.
    #캐릭터를 예로들면 기능 - 공격,이동,대화하기,길드 가입하기,...
    #클래스 바깥에 기능이 정의 되어 있으면 - 함수
    #클래스 안에 기능이 정의되어 있으면 -메서드
    #메서드는 매개변수가 있든 없든 self가 있어야한다.
    #메서드는 첫 번째 매개변수가 반드시 필요하다.
    #메서드의 첫 번째 매개변수 이름은 self를 사용한다.
    #매개변수가 필요하지 않은 메서드라도 반드시 첫 번째 매개변수인 self를 넣어줘야한다.
    #self는 이 인스턴스에 있는 이라는 의미를 가진다


    def attack(self ,target):
        # 공격을 하기 위한 모션 (그래픽처리 )
        target.HP = target.HP - self.물리공격력

        # 공격을 받은 모션(그래픽처리)

        return target
    def move(self):
        pass


    def say(self):
        pass


    def buy(self):
        pass


    def exit(self):
        pass




#플레이어블캐릭터 틀을 만들어 노혹
#그 틀을 사용해서
#전사의 능력치를 갖고 있는 캐릭터
#궁수의 능력치를 갖고 있는 캐릭터
#찍어낼 수 있음


#전사캐릭터
worrior = Character()
worrior.HP = 100
worrior.MP = 50
worrior.물리공격력 = 10
worrior.마법공격력 = 5

#궁수 캐릭터
archer =Character()
archer.HP = 70
archer.MP = 70
archer.물리공격력 = 7
archer.마법공격력 = 7


worrior.attack(archer)
'''
매개변수로 객체를 전달하게 됐을때는
return을 통해서 값을 전달받지 않아도 됨
그 이유는 그 객체의 메모리주소가 복사되서 전달되기때문에
객체의 메모리주소 안에 들어가서 직접 헨들링된다 그래서 return을 하지 않아도 값이 들어가게 되는것

'''

archer.attack(worrior)

print(archer.HP)
print(worrior.HP)

