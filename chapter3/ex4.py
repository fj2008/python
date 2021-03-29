'''
                            TDD테스트 드리븐 개발방법
                            결과가 이미 다 만들어졌다고 생상상하고
                            그에 필요한 기능들을 만들어가는 방법
'''


class Cart :
    #생성자도 메서드 이기때문에 매개변수를 설정해서 인자를 받을수 있다

    def __init__(self,width,height,frame,wheel):
        self.width = width
        self.height = height
        self.frame = frame
        self.wheel = wheel
        self.goodsList = []
        self.nowPosition = {"x":0,"y":0}


    def move(self,x,y,speed) :
        if(x>0) :
            movedX = x*speed
            print("카트를 x축으로 {0}의 속도로 {1}만큼 움직임".format(speed,movedX))
            self.nowPosition["x"] +=movedX

        if(y>0) :
            movedY = y * speed
            print("카트를 y축으로{0}의 속도로{1}만큼 움직임".format(speed,movedY))
            self.nowPosition["y"] += movedY

    def putin(self,goods):
        self.goodsList.append(goods)
        print("카트에 {}을 담았습니다".format(goods))

    def putOut(self,goods):
        self.goodsList.remove(goods)

    def cart(self):
        print("카트의 가로",self.width)
        print("카트의 높이",self.height)
        print("카트의 제질",self.frame)
        print("카트의 바퀴갯수",self.wheel)
        print("카트안에 들어있는 물건",self.goodsList)


groceriesCart= Cart(100,200,"철제",4)

groceriesCart.cart()


EmartCart = Cart(200,150,"플라스틱",3)
EmartCart.cart()
#이렇게 생성자에 매개변수를 넣음으로 인해서 각각의 인스턴스에 개성을 부여한다


groceriesCart.move(10,10,1)

groceriesCart.putin("양파")
groceriesCart.putin("무")

groceriesCart.putOut("무")


print(groceriesCart.goodsList)



