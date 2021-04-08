import matplotlib.pyplot as plt
#차트를 출력할수 있는 창을 하나 만든다

figure = plt.figure()
axes = figure.add_subplot(1,1,1)

x=[0,1,2,3,4]
y1=[4,1,3,5,2]
y2 = [0,8,5,3,1]

#plot> 꺾은선 그래프
# 그래프의 형태나 색상 등 시각적인 부분을 지정할 수 있다.
# linestyle -선의 형태
# linewidh - 선의 굵기
# color - 선의 색상
#marker - 표시
axes.plot(x,y1, linestyle="dotted", linewidth=5.0)
axes.plot(x,y2, color="r", marker ="v")

# plt.rc("font", family="굴림")


plt.title("this chart name")#차트이름
plt.xlabel("date")#x축이름
plt.ylabel("rank")#y축이름

plt.axis([1,31,0,200])
plt.show()
'''
figure = plt.figure()
#첫 번째 매개변수 - 행 번호
#두 번째 매개변수 = 열번호
#세번째 매개변수 = 차트의 번호

axes1 = figure.add_subplot(1,2,1)
axes2 = figure.add_subplot(1,2,2)
plt.show()
'''


