
'''
for i in range (3):
    print("Hello Python")
    print("Nice to meet you")
    print("="*10)
'''

#위와같은 코드를 함수를 사용해서 줄일수 있다
def welcome():

        print("Hello Python")
        print("Nice to meet you")
        print("=" * 10)

for i in range(3):
    welcome()

#위와같이 함수를사용해서 소스코드들을 묶었다