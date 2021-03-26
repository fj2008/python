'''
클래스~~~
클래스는 틀같은 것이다
과자 틀이 있다고 가정하고 쿠키를 만든다 하면 똑같은 모양을 계속 만들어 낼수 있듯이
클래스만 있다면 같은 기능과 속성을 갖고 있는 객체를 계속 만들 수 있다
class 클래스명 :
    요소
    기능


게임 캐릭터에게 필요한
속성 - 체력, 마력 , 물리공격력, 마법공격력 , ....
기능 - 물리공격 , 마법공격, 이동 ....
'''
#소스코드를 넣어놓은 파일을 모듈이라고함
#소스파일에 별명을 붙일수 있음 'as 별명'

import  playableCharacter as PC
import  NonPlayableCharater as NPC

print("공격 받기 전 monsterHP = ", NPC,NPC.monsterHP)

#전사 캐릭터가 몬스터 캐릭터를 공격한다.
monsterHP = PC.attack(NPC.monsterHP,PC.warrior물리공격력)

print("공격 받은 후 monsterHP = ", NPC.monsterHP)

archerHP = 75
archerMP = 75
archer물리공격력 = 17
warrior마법공격력 = 10
