class PersonFaceInfo :
    def __init__(self,eye,nose,mouth):
        self.eye = eye
        self.nose = nose
        self.mouth = mouth

class PersonBodyInfo :
    def __init__(self,finger,toe,leg):
        self.finger = finger
        self.toe = toe
        self.leg = leg
# 사람은 눈,코,입,손가락,발가락,다리를 갖고 있다
#숨쉬고, 먹고, 말하기를 할 수 있다.
class Person:
    def __init__(self,finger,toe,leg,eye,nose,mouth):

        #얼굴과 관련된 데이터
        self.PersonFaceInfo = PersonFaceInfo(eye,nose,mouth)
        
        self.PersonBodyInfo =PersonBodyInfo(finger,toe,leg)

        #몸과 관련된 데이터

    def showInfo(self):
        print(self.PersonFaceInfo.eye)
        print(self.PersonFaceInfo.nose)
        print(self.PersonFaceInfo.mouth)
        print(self.PersonBodyInfo.toe)
        print(self.PersonBodyInfo.finger)
        print(self.PersonBodyInfo.leg)

#학생은 사람의 특징을 갖고 있으면서 신분이 학생이다,
#학생은 사람의 기능을 하면서 공부도 할 수 있다.
    def breaht(self):
        print("숨쉰다")

    def eat(self):
        print("먹는다")

    def say(self):
        print("말하기")

person1 = Person(2,1,1,10,10,2)
person1.showInfo()
