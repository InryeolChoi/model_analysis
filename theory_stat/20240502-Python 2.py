# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:19:26 2021

@author: choisungeun
"""

#%%데이터 시각화
import matplotlib.pyplot as plt
import numpy as np



#%%pandas를 이용한 그래프 그리기 : 선 그래프
# Series : index, values 따로 지정하지 않는 경우
import pandas as pd
import matplotlib.pyplot as plt

s1=pd.Series([1,2,3,4,5,6,7,8,9,10])
s1

s1.plot()
plt.show()

# Series : index, values 따로 지정하는 경우
s2 = pd.Series([1,2,3,4,5,6,7,8,9,10], index = pd.date_range('2019-01-01', periods=10)) 
s2 

s2.plot()
plt.show()

s2.plot(grid=True) #격자 추가
plt.show()

#%%pandas를 이용한 그래프 그리기 : 선 그래프
#DataFrame
df_rain=pd.read_csv('C:/Users/choisungeun/Desktop/sea_rain1_space.txt',sep=" ", index_col="연도")
df_rain 

#그래프 그리기
import matplotlib
matplotlib.rcParams['font.family'] = 'NanumGothic'  #'맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

df_rain.plot() 
plt.show() 

#grid=True 옵션
rain_plot = df_rain.plot(grid = True, style = ['r--*', 'g-o', 'b:*', 'm-.p']) 
rain_plot.set_xlabel("연도") 
rain_plot.set_ylabel("강수량") #rotation='horizontal', fontsize=15
rain_plot.set_title("연간 강수량") 
plt.show() 

#example
#데이터 생성
year = [2006, 2008, 2010, 2012, 2014, 2016] # 연도 
area = [26.2, 27.8, 28.5, 31.7, 33.5, 33.2] # 1인당 주거면적 
table = {'연도':year, '주거면적':area} 
df_area = pd.DataFrame(table, columns=['연도', '주거면적']) 
df_area 

#그래프 그리기
df_area.plot(x='연도', y='주거면적', grid = True, 
title = '연도별 1인당 주거면적') 
plt.show()


#%%pandas를 이용한 막대그래프
#데이터 생성
import matplotlib.pyplot as plt 
import pandas as pd 

grade_num = [5, 14, 12, 3] 
students = ['A', 'B', 'C', 'D'] 

df_grade = pd.DataFrame(grade_num, index=students, columns = ['Student']) 
df_grade 

#그래프 그리기
grade_bar = df_grade.plot.bar(grid = True) 
grade_bar.set_xlabel("학점") 
grade_bar.set_ylabel("학생수") 
grade_bar.set_ylim(0,15)
grade_bar.set_title("학점별 학생 수 막대 그래프") 
plt.show() 


#%%pandas를 이용한 파이그래프

#데이터 생성
fruit = ['사과', '바나나', '딸기', '오렌지', '포도'] 
result = [7, 6, 3, 2, 2] 

df_fruit = pd.Series(result, index = fruit, name = '선택한 학생수') 
df_fruit 

#그래프 그리기
plt.figure(figsize=(10,5)) 
df_fruit.plot.pie() 
plt.show() 


#%%pandas를 이용한 히스토그램
#데이터 생성
math = [76,82,84,83,90,86,85,92,72,71,100,87,81,76,94,78,81,60,79,69,74,87,82,68,79] 

df_math = pd.DataFrame(math, columns = ['Student']) 
df_math

math_hist = df_math.plot.hist(bins=8, grid = True) 
math_hist.set_xlabel("시험 점수") 
math_hist.set_ylabel("도수(frequency)") 
math_hist.set_title("수학 시험의 히스토그램") 
plt.show() 


#%%pandas를 이용한 산점도
#데이터 생성
temperature = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1] 
Ice_cream_sales = [236500, 357500, 203500, 365200, 446600, 574200, 453200, 675400, 598400,  463100] 
dict_data = {'기온':temperature, '아이스크림 판매량':Ice_cream_sales} 
df_ice_cream = pd.DataFrame(dict_data, columns=['기온', '아이스크림 판매량']) 
df_ice_cream
df_ice_cream['아이스크림 판매량']
df_ice_cream['기온']
df_ice_cream['기온'].mean()
df_ice_cream['아이스크림 판매량'].mean()
df_ice_cream.plot.scatter(x='기온', y='아이스크림 판매량', grid=True, title='최고 기온과 아이스크림 판매량') 
plt.show() 




#%%원하는 한글 폰트 변경 방법
import matplotlib
matplotlib.rcParams['font.family'] = 'NanumGothic' 
matplotlib.rcParams['axes.unicode_minus'] = False


matplotlib.rcParams['font.family'] = 'NanumMyeongjo' 
matplotlib.rcParams['axes.unicode_minus'] = False

matplotlib.rcParams['font.family'] = 'gulim' #굴림
matplotlib.rcParams['axes.unicode_minus'] = False



matplotlib.rcParams['font.family'] = 'batang' #궁서
matplotlib.rcParams['axes.unicode_minus'] = False

matplotlib.rcParams['font.family'] = 'Hancom Gothic' 
matplotlib.rcParams['axes.unicode_minus'] = False


