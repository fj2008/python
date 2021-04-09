import matplotlib as mpl

print(mpl.matplotlib_fname())
'''
캐시 - 어떤데이터를 매번 불러오는게 아니구 한번 불러온 데이터를 일정기간동안 저장을 해 두고 
해당 데이터를 다시사용할때는 캐시에서 데이터를 꺼내온다
'''

print(mpl.get_cachedir())