# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:19:26 2021

@author: choisungeun
"""

#%%데이터 시각화
import matplotlib.pyplot as plt
import numpy as np


#%%help는 Ctrl+i

#%%맑은 고딕체로 폰트 변경 방법
matplotlib.rcParams['font.family'] = 'MalgunGothic' 
matplotlib.rcParams['axes.unicode_minus'] = False

import matplotlib
matplotlib.rcParams['font.family'] = 'NanumGothic' 
matplotlib.rcParams['axes.unicode_minus'] = False


matplotlib.rcParams['font.family'] = 'NanumMyeongjo' 
matplotlib.rcParams['axes.unicode_minus'] = False

matplotlib.rcParams['font.family'] = 'gulim' #굴림
matplotlib.rcParams['axes.unicode_minus'] = False



matplotlib.rcParams['font.family'] = 'batang' #궁서
matplotlib.rcParams['axes.unicode_minus'] = False

matplotlib.rcParams['font.family'] = 'HYGothic-Extra' 
matplotlib.rcParams['axes.unicode_minus'] = False


import matplotlib.font_manager
fpaths = matplotlib.font_manager.findSystemFonts()

for i in fpaths:
    f = matplotlib.font_manager.get_font(i)
    print(f.family_name)
    
len(f.family_name)
#%%한글폰트로 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성하기
x = np.arange(0,5,1); x
y1 = x
y2 = x+1
y3 = x+2
y4 = x+3

plt.plot(x,y1,'>--r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.legend(['데이터 1','데이터 2','데이터 3','데이터 4'], loc='best')
plt.xlabel('X 축')
plt.ylabel('Y 축')
plt.title('그래프 제목')
plt.grid(True)  
plt.show()

#%%문자열 표시
plt.plot(x,y1,'>--r',x,y2,'s-g',x,y3,'d:b',x,y4,'-.Xc')
plt.text(0,6,"문자열 출력 1")
plt.text(0,5,"문자열 출력 2")
plt.text(3,1,"문자열 출력 3")
plt.text(3,0,"문자열 출력 4")
plt.show()

#%%example : 수식
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.text(1, 15, r'$\alpha > \beta$', fontdict={'size': 30})

plt.show()

#%%파이 그래프
#데이터 생성
fruit=['사과','바나나','딸기','오렌지','포도']
result=[7,6,3,2,2]

import matplotlib
matplotlib.rcParams['font.family'] = 'NanumGothic' 
matplotlib.rcParams['axes.unicode_minus'] = False

import matplotlib.pyplot as plt
plt.pie(result)
plt.show()

#그래프 너비&높이 조절
plt.figure(figsize=(5,5))
plt.pie(result)
plt.show()

#전체에서의 비율 표시
plt.figure(figsize=(10,10)) 
plt.subplot(2,2,1) #p=1
plt.pie(result, labels= fruit, autopct='%.0f') 

plt.subplot(2,2,2) #p=2
plt.pie(result, labels= fruit, autopct='%.1f') 

plt.subplot(2,2,3) #p=3
plt.pie(result, labels= fruit, autopct='%.0f%%') 

plt.subplot(2,2,4) #p=4
plt.pie(result, labels= fruit, autopct='%.1f%%') 

plt.show()


plt.figure(figsize=(5,5)) 
plt.pie(result, labels= fruit, autopct='%.0f') #비율값이 정수만 표시
plt.show() 

plt.figure(figsize=(5,5)) 
plt.pie(result, labels= fruit, autopct='%.1f') #비율값이 소수점 첫째 자리까지 표시
plt.show() 


plt.figure(figsize=(5,5)) 
plt.pie(result, labels= fruit, autopct='%.0f%%') #비율값이 정수에 %기호까지 표시
plt.show() 

plt.figure(figsize=(5,5)) 
plt.pie(result, labels= fruit, autopct='%.1f%%') #비율값이 소수점 첫째 자리와 %기호까지 표시(0.2,0.3)
plt.show() 

#%% startangle : 제일 처음 부채꼴 부분이 그려지는 각도로 x축을 중심으로 반시계방향으로 증가함
plt.figure(figsize=(10,10)) 
plt.subplot(2,2,1)
plt.pie(result, labels= fruit, autopct='%.1f%%') #startangle=0 기본값

plt.subplot(2,2,2)
plt.pie(result, labels= fruit, autopct='%.1f%%', startangle=90)  

plt.subplot(2,2,3)
plt.pie(result, labels= fruit, autopct='%.1f%%', startangle=180)  

plt.subplot(2,2,4)
plt.pie(result, labels= fruit, autopct='%.1f%%', startangle=270)  
plt.show()


#x counterclock: 데이터에서 부채꼴 부분이 그려지는 순서
plt.figure(figsize=(10,10)) 
plt.subplot(1,2,1)
plt.pie(result, labels= fruit, autopct='%.1f%%') #counterclock=True 기본값

plt.subplot(1,2,2)
plt.pie(result, labels= fruit, autopct='%.1f%%',counterclock = False)

plt.show() 


#%% explode
plt.figure(figsize=(10,10)) 
plt.subplot(1,2,1)
plt.pie(result, labels= fruit, autopct='%.1f%%')

plt.subplot(1,2,2)
explode_value = (0.1, 0, 0, 0, 0) 
plt.pie(result, labels= fruit, autopct='%.1f%%', explode=explode_value) 

plt.show() 

#%% shadow
plt.figure(figsize=(10,10)) 
plt.subplot(1,2,1)
explode_value = (0.1, 0, 0, 0, 0) 
plt.pie(result, labels= fruit, autopct='%.1f%%', explode=explode_value) 

plt.subplot(1,2,2)
explode_value = (0.1, 0, 0, 0, 0) 
plt.pie(result, labels= fruit, autopct='%.1f%%', explode=explode_value, shadow=True) 

plt.show() 

#여러 옵션 같이 사용
explode_value = (0.1, 0, 0, 0, 0) 
plt.figure(figsize=(5,5)) 
plt.pie(result, labels= fruit, autopct='%.1f%%', startangle=90,
counterclock = False, explode=explode_value, shadow=True) 
plt.show() 

#%%히스토그램
#기본그림
math = [76, 82, 84, 83, 90, 86, 85, 92, 72, 71, 100, 87, 81, 76,
        94, 78, 81, 60, 79, 69, 74, 87, 82, 68, 79] 
plt.hist(math) 


# bins : 계급 수 조정
plt.figure(figsize=(10,6)) 
plt.subplot(1,2,1)
plt.hist(math)

plt.subplot(1,2,2)
plt.hist(math, bins=8)

plt.show()


# color : 색깔 조정
plt.figure(figsize=(10,6)) 
plt.subplot(1,2,1)
plt.hist(math)

plt.subplot(1,2,2)
plt.hist(math, color="pink")

plt.show()

# 여러 옵션 사용
plt.hist(math, bins= 7, color="red") 
plt.xlabel('시험 점수') 
plt.ylabel('도수(frequency)') 
plt.title('수학 시험의 히스토그램') 
plt.grid() 
plt.show()


#%%산점도
import matplotlib.pyplot as plt
import numpy as np

#데이터 생성
height = [165, 177, 160, 180, 185, 155, 172] # 키 데이터 
weight = [62, 67, 55, 74, 90, 43, 64] # 몸무게 데이터 
    
#그리기
plt.scatter(height, weight) 
plt.xlabel('Height(m)') 
plt.ylabel('Weight(Kg)') 
plt.title('Height & Weight') 
plt.grid(True)
plt.show() 

#%%c, s
#c : 색깔 조정
plt.figure(figsize=(10,6)) 
plt.subplot(1,2,1)
plt.scatter(height, weight) 

plt.subplot(1,2,2)
plt.scatter(height, weight,c='r') # 컬러는 붉은색(red) 
plt.show()

#s : 마커 크기 조정
plt.figure(figsize=(10,6)) 
plt.subplot(1,2,1)
plt.scatter(height, weight) 

plt.subplot(1,2,2)
plt.scatter(height, weight, s=500) # 마커 크기는 500
plt.show()

#데이터마다 마커의 크기와 컬러 조정
size = 100 * np.arange(1,8) # 데이터별로 마커의 크기 지정 
size
colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y'] # 데이터별로 마커의 컬러 지정 
plt.scatter(height, weight, s=size, c=colors) 
plt.show() 


plt.scatter(height, weight, s=size, c='y') 
plt.show() 
#%%zip()
names=['James','Robert','Lisa','Mary']
scores=[95,96,97,94]

#method 1
for k in range(len(names)):
    print(names[k], scores[k])

#method 2
for name, score in zip(names, scores):
    print(name, score)


import matplotlib.pyplot as plt
import numpy as np

#%%산점도 example
# 도시
city = ['서울', '인천', '대전', '대구', '울산', '부산', '광주'] 
# 위도(latitude)와 경도(longitude) 
lat  = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]  
lon = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85] 
# 인구 밀도(명/km^2): 2017년 통계청 자료 
pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995] 

size = np.array(pop_den) * 0.2 # 마커의 크기 지정
np.array(pop_den)
size
colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y'] # 마커의 컬러 지정 

plt.scatter(lon, lat, s=size, c=colors, alpha=0.5) 
plt.xlabel('경도(longitude)') 
plt.ylabel('위도(latitude)') 
plt.title('지역별 인구 밀도(2017)') 

for x, y, name in zip(lon, lat, city):
    plt.text(x,y,name) # 위도 경도에 맞게 도시 이름 출력
plt.show() 


#%%그래프 저장하기
#현재 설정된 그래프의 크기 확인방법
import matplotlib as mpl
mpl.rcParams['figure.figsize']

#현재 설정된 그래프의 dpi값 확인방법
mpl.rcParams['figure.dpi']

#파이 그래프 example
import matplotlib.pyplot as plt

fruit=['사과','바나나','딸기','오렌지','포도']
result=[7,6,3,2,2]
explode_value = (0.1, 0, 0, 0, 0) 

plt.figure(figsize=(10,10)) #그래프의 크기 지정
plt.pie(result, labels= fruit, autopct='%.1f%%', explode=explode_value) 

# 그래프를 이미지 파일로 저장. dpi는 200으로 설정 
plt.savefig('C:/Users/choisungeun/Desktop/saveFigTest2.png', dpi = 200) 
plt.show() 


plt.figure(figsize=(10,10)) #그래프의 크기 지정
%matplotlib qt
plt.pie(result, labels= fruit, autopct='%.1f%%', explode=explode_value) 
plt.show() 


plt.figure(figsize=(10,10)) #그래프의 크기 지정
%matplotlib inline
plt.pie(result, labels= fruit, autopct='%.1f%%', explode=explode_value) 
plt.show() 







