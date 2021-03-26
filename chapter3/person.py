class person :

    def __init__(self):
        self.eyes=2
        self.nose =1
        self.mouse =1
        self.ear=2
        self.arm=2
        self.leg=2
        self.leftfinger=5
        self.ringtfinger=5
        self.lefttoe=5
        self.ringttoe=5

        self.name =0
        def eat(self) :
            print(self.name,"이(가) 먹는당")

        def speek(self):
            print(self.name,"이(가)말한당")

        def sleep(self):
            print(self.name,"이(가)잔당")

#preson1 객체(참조변수)
person1 = person()
#preson2 객체(참조변수)
person2 = person()

person1.name = "사람1"
person2.name = "사람2"

person1.eat()
