import pygame
import sys
import random
import time
def showScore(score, x, y, screen):
    font = pygame.font.Font(None,24)#글꼴스타일
                                                    #안티얼라이씽
    text = font.render("Score: " + str(score).zfill(6), True, (0,0,0))#출력할 글씨를 생성
    textRect = text.get_rect()#글씨의 경계를 만들어주는코드
    textRect.centerx = x
    textRect.centerx = y#글씨의 좌표
    screen.blit(text,textRect)#화면을 출력한다
pygame.init()
screan = pygame.display.set_mode((480,640))


FPS = 30
fpsClock = pygame.time.Clock()

asteroidtimer = 100#주기적으로 위에서 아래로 떨어질 행성을 만들어내는 매서드
            #x   #y
asteroids = [[20, 0, 0]]

score = 0

try:

    sqaceshipimg = pygame.image.load("./img/spaceship.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0,asteroid1,asteroid2)
    gameover = pygame.image.load("./img/gameover.jpg")

    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")

    takeoffsound.play()
except Exception as err:
    print("그림 또는 효과음 삽입에 문제가 있습니다.", err)
    pygame.quit()
    sys.exit()
running =True
while running:

    fpsClock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


    screan.fill((255, 255, 255))

    score =score +3
    showScore(score,400,10,screan)
    if score % 100 == 0 :
        FPS +=2


    position = pygame.mouse.get_pos()  # 마우스의 위치를 파악함
    spaceshippos = (position[0] - 10, 600)
    screan.blit(sqaceshipimg, (spaceshippos))

    spaceshipRect = pygame.Rect(sqaceshipimg.get_rect())
    spaceshipRect.left = spaceshippos[0]
    spaceshipRect.top = spaceshippos[1]

    #떨어질 행성을 생성하고 10씩 증가돼서 0이되도록
    asteroidtimer -= 50
    #새로운 행성을 생성하는코드
    if asteroidtimer <=0 :
        randomX = random.randint(5,475)# x=5,474=y사이에 임의의 행성을 생성
        asteroidType = random.randint(0,2)#행성이들어있는 리스드의 인덱스번호#행성의 종류를 렌덤으로
        asteroids.append([randomX,0,asteroidType])
        asteroidtimer = random.randint(50,200)

    #생성한 행성을 떨어뜨린다
    index = 0
    for stone in asteroids:
        stone[1] += 10
        if stone[1] >640:
            asteroids.pop(index)#데이터를 꺼내라
        stoneRect = pygame.Rect(asteroidimgs[stone[2]].get_rect())
        stoneRect.left = stone[0]
        stoneRect.top = stone[1]
        if stoneRect.colliderect(spaceshipRect):
            asteroids.pop(index)
            running =False
            time.sleep(2)

                                           #x      #y
        screan.blit(asteroidimgs[stone[2]],(stone[0],stone[1]))
        index += 1

    pygame.display.flip()


    landingsound.play()

screan.blit(gameover, (0,0))
showScore(score, screan.get_rect().centerx,screan.get_rect().centerx,screan)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
