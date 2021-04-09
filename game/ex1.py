import pygame
import sys
pygame.init()
screan = pygame.display.set_mode((480,640))#매개변수로 튜플을 전달한것#창의 크기를 조절하는 코드다


#컴퓨터마다 연산속도가 다르다 #연산이 빠른 좋은컴퓨터는 상대적으로 빠르게 움직이기때문에
#컴퓨터마다 기준이 달라진다 그래서 컴퓨터에 상관없이
# 일정한 속도로 움직이기 위해서 그 while문의 반복속도를 조절하는것이 fps다
FPS = 30
fpsClock = pygame.time.Clock()

try:
    #게임에 필요한 이미지와 사운드를 불러오는코드
    sqaceshipimg = pygame.image.load("./img/spaceship.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0,asteroid1,asteroid2)#튜플
    gameover = pygame.image.load("./img/gameover.jpg")

    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")

    takeoffsound.play()
except Exception as err:
    print("그림 또는 효과음 삽입에 문제가 있습니다.", err)
    pygame.quit()
    sys.exit()





#이렇게하면 게임창이 잠깐등장했다가 꺼짐
#코드가 끝났기 때문


while True:#종료버튼을 누르기전까지 게임이 실행되어야한다

    fpsClock.tick(FPS)#fps의 설정으로 연산의 기준을 정하고#30으로 설정된fps는 초당30번 연산을반복한다



    for event in pygame.event.get():#반복적으로 내가 어떤행동을 하는지 파악하는 코드
        #종료버튼을 누르면 게임을 종료해라
        if event.type == pygame.QUIT :#만약에 exit버튼을 누른다면
            pygame.quit()#열었던 스크린을 닫아라
            sys.exit(0)# 프로그렘종료

    landingsound.play()#불러온 사운드가 while문안에서 반복되도록
    screan.fill((255,255,255))#rgb값화면을 하얗게 채운다라는 코드
    screan.blit(sqaceshipimg, (240,600))#이미지를 출력하고 튜플안에 좌표를 넣어줫다
    screan.blit(asteroidimgs[0], (240,320))

    pygame.display.flip()