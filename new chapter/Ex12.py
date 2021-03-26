# 정수들  중 최대값을 구하세요.
#max활용
#최댓값을 알아서 구해줌
maximum = max(1,10,1,23,43,534)

print(maximum)


numberList = [1,3,5,67,7,65,12,23]
maximum = max(numberList)
print(maximum)

#range, list , tuple, len
#sorted 함수 - 오름차순 정렬을 해주는함수
print("정렬 전")
print(numberList)
print("정렬 후")
print(sorted(numberList))

#오름차순 정렬함수를 직접 만들어보자

testList = [2,1,3,5,6]

for i in range(1,len(testList)):

    if testList[i-1]>testList[i] :
        temp = testList[i]
        testList[i] = testList[i-1]
        testList[i-1] = temp



print(testList)