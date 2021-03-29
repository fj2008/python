'''
클래스 속성의 종류
클래스 속성
해당클래스가 갖고있는 속성
모든 객체가 공유
클래스 멤버 변수


인스턴스 속성
해당 객체만 갖고 있는 속성
고유한 속성 값이 있다
인스턴스 멤버 변수


공개 멤버 변수
지금까지 선언한 멤버변수들
클래스 바깥에서도 사용가능한 변수

비공개 멤버 변수
고정돼야할 변수값들이나 수정이 되면 안되는 변수들을 비공개 멤버변수를 활용해서
수정을 하지 못하게끔 만들어주는게 비공개 멤버변수
클래스바깥에서 사용하지 못한다
클래스 멤버변수와 인스턴스멤버변수 둘다에 사용가능하다
'__변수 이름'
위와같이 선언함
'''

class car :
    #클래스 멤버 변수 (속성)
    passengerList = []
    #모든 객체가 공유하는 멤버 변수


    def __init__(self):
        #이용요금은 1350원
        self.__charge = 1350
        #이동 수단의 종류
        self.kind = ""

        #이동수단의 바퀴 개수
        self.wheel  = 0
        self.maximumPeople = 0
        self.x = 0
        self.y = 0

    def move (self, x, y, speed) :

        self.x = x * speed
        self.y = y * speed

    def getIn(self,name,fee):
        print("이용요금은",self.__charge,"원 입니다.")
        print("지불하신 금액은", fee,"원 입니다.")

        money = fee - self.__charge
        if money >0 :
            print(name,"님의 잔액",money,"원 입니다.")
        else :
            print("잔액이 반환되지 않습니다.")



#클래스요소에 접근할때는 self보다 클래스명으로 하는게 좋다
##비공개 맴버변수는 클래스 바깥에서 사용할 수 없다
#고정된 데이터의 값의 수정을 방지하기 위함
bicycle = car()
bicycle.getIn("홍길동" ,1500)
vehicle = car()
vehicle.getIn("설까치",1233)

motorcycle = car()
motorcycle.getIn("하니",5000)

print(car.passengerList)
print(car.passengerList)
print(car.passengerList)