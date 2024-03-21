# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 05:47:54 2022

@author: choisungeun
"""

#%% bool()
%clear
bool(True)
bool(1)
bool(45)
bool(-45)

bool(False)
bool(0)
bool(0.0)

#%% integer
5

0

05

#%%교재 지수 example
3*10**8  #접근법 1


3.0*10**8

3.0*(10**8)


3e8    #접근법 2

1e15

1e16

1e-4

1e-5

#%%숫자 자리수(_) 표시
1,000,000

million=1_000_000
million

1_2_3


#%% 실수 1
5

5.

type(5)

type(5.)
5.0

05

05.0

05.5


#%% 실수 3
million=1_000_000.0
million

1.0_0_1
1_0_1


#%% float() 사용 1
%clear
type(True)
type(False)

float(True)
float(False)

type(float(True))
type(float(False))


#%% float() 사용 2
int(98)
float(98)

type(int(98))
type(float(98))

'99'
type('99')


float('99')
type(float('99'))

#%% float() 사용 3
type('1.0e4')

float('98.6')
float('-1.5')
float('1.0e4')


type(float('1.0e4'))


a='1.0e4'
type(a)
float(a)
type(float(a))

#%% float() 사용 4
43+2.

43+2


#%%타입 변환 :int() 1
%clear
type(True)
type(False)

float(True)
float(False)

type(float(True))
type(float(False))

int(True)
int(False)

type(int(True))
type(int(False))

bool(1)
bool(0)

int(98.6)
int(1.0e4)


int('99')
int('-23')
int('+12')
int('1_000_000')

float('1_000_000')

#%%타입 변환 :int() 예외사항
%clear
int('99 bottles of bear on the wall')

int('98.6')

int('1.0e4')

float('98.6')
float('1.0e4')


#%%example
abc=12340
print(abc)

abc

print(abc*1/2)
print(abc*1/4)
print(abc*1/5)

a=123
print(a)
a
#%% 예약어 확인
help("keywords")  # method 1

import keyword   # method 2
keyword.kwlist


#%%할당
x=5
y=x+12
y


%reset -sf

y=x+12


#%%변수 복사
a=7
print(a)

b=a
print(b)


#%% 변수타입 혹은 리터럴 값 확인방법
%clear
type(7)
type(7.5)

type(7)==int
type(7)==float
type(7)==bool


isinstance(7, int)
isinstance(7, float)
isinstance(7, bool)


#%%example

a=7
b=a

type(a)

type(b)

type(58)

type(99.9)

type('abc')

isinstance(58,float)

isinstance(58,float)

isinstance(58,int)


isinstance("abc",str)
isinstance('abc',str)


#%%여러 이름 할당하기
two=deux=zwei=2

two
deux
zwei

a=b=c=d=4
a
b
c
d

print(two)
print(deux)
print(zwei)
#%% 정수와 변수 1
a=95
a
a-3

a

a=a-3
a

#%% 정수와 변수 2
#case 1
a=95
a
a-3

#case 2
a=95
a -=3   #a=a-3
a

#%% 문자열 생성 1
"String Test"
'String Test'

print("String Test")
print('String Test')

#%%
string3='This is a "double" quotation test'
string4="This is a 'single' quotation test"

print(string3)
print(string4)


type(string3)
type(string4)

#%% 문자열 변수 생성
string1="String Test 1"
string2="String Test 2"

print(string1)
print(string2)

type(string1)
type(string2)

#%% str()
type(98.6)

type(1.0e4)

type(True)


str(98.6)

str(1.0e4)

str(True)


type(str(98.6))

type(str(1.0e4))

type(str(True))


#%% 문자열 생성 2 : 따옴표 문자열 생성 ' & "
'Snap'

"Crackle"


print("Nay!' said the naysayer. 'Neigh?' said the horse.")

print('The rare double quote in captivity: ". ')

'A "two by four" is actually 1 1/2" x 3 1/2". '

print("'There's the man that shot my paw!' cried the limping hound.")


#%% 문자열 생성 3 : ''' & """
long_string1='''[삼중 작은따옴표를 사용한 예]
파이썬에는 삼중 따옴표로 여러 행의 문자열을 입력할 수 있습니다.
큰따옴표("")와 작은따옴표('')도 입력할 수 있습니다.'''

long_string2="""[삼중 큰따옴표를 사용한 예]
파이썬에는 삼중 따옴표로 여러 행의 문자열을 입력할 수 있습니다.
큰따옴표(")와 작은따옴표(')도 입력할 수 있습니다."""

print(long_string1)
print(long_string2)

#%% 문자열 생성 3 : ''' & """

poem='''There was a Young Lady of Norway,
Who casually sat in a doorway;
When the door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway.'''

poem 

print(poem)


poem='There was a Young Lady of Norway,


poem2="""I do not Like thee, Doctor Fell.
    The reason why, I cannot tell.
            But this I know, and know full well:
I do not like thee, Doctor Fell.
"""

poem2

print(poem2)

poem3="""I do not Like thee, Doctor Fell.
    The reason why, I cannot tell.
            But this I know,      and know full well!*##:
I do not like thee, Doctor Fell.
"""

print(poem3)

#%% print()

print('Give', "us", '''some''', """space""")

print('Give', "us", '''''', """space""")


#%% 이스케이프 문자 : \n
palindrome='A man, \nA plan, \nA canal: Panama.'  
print(palindrome)    


palindrome='A man, \n A plan, \nA canal: Panama.'  
print(palindrome)    

   
#%% 이스케이프 문자 : \t
print("\tabc")  
print("a\tbc") 

print("ab\tc")     

print("abc\t")   

#%% 이스케이프 문자 : 작은따옴표나 큰따옴표 표현
testimony1="\"I did nothing!\" he said. \"Or that other thing.\""
print(testimony1)

fact1="The world's largest rubber duck was 54'2\" by 65'7\" by 105'"    
print(fact1)


testimony2="\'I did nothing!\' he said. \'Or that other thing.\'"
print(testimony2)

fact2="The world's largest rubber duck was 54'2\' by 65'7\' by 105'"    
print(fact2)





#%% 이스케이프 문자 : 백슬래시 입력

speech='The backslash \ bends over backwards to please you.'
print(speech)


speech='The backslash (\\) bends over backwards to please you.'
print(speech)

speech='The backslash \\ bends over backwards to please you.'
print(speech)


#%% 문자열 반복하기 : * 

a='Hellow World'
a
a*2
print(a*2)
print(a,a)

#%% 문자열 추출하기 : [ ] 
#indexing
a='Python'
a
a[0]
a[-6]

a[5]
a[-1]

name='Henny'
name[0]='P'

name.replace('H','P')
name

v=name.replace('H','P')
v

name[1:]
'P'+name[1:]

a='P'+name[1:]
a
name


#%% slicing example
letters='abcdefghijklmnopqrstuvwxyz'

letters[:]   #전체 문자열 지정 = letters[0:]

letters[20:]  #20번째 문자열부터 끝까지 추출

letters[12:15] #12번째부터 14번째까지 문자열 추출

letters[-3:]  # 마지막 세 문자 추출

letters[18:-3] # 18번째 문자열부터 마지막 네 번째 문자까지 추출

letters[-6:-2] # 끝에서 여섯 번째 문자부터 끝에서 세 번째 문자까지 추출

letters[::7]  # 처음부터 끝까지 7씩 간격으로 문자 추출

letters[4:20:3] # 4번째부터 19번째까지 3씩 간격으로 문자 추출

letters[19::4] # 19번째 부터 끝까지 4씩 간격으로 문자 추출

#%% Python vs R 비교
a='Hello World'
print(a)

a[1]

a[1:4]

a[1:]

a[10]

a[-1]



#%% 튜플 만들기 1
empty_tuple = ()
empty_tuple

type(empty_tuple)

#%% 튜플 만들기 2
one_marx='Groucho',   # method 1
one_marx

one_marx=('Groucho',)  # method 2
one_marx

type(one_marx)


one_marx1=('Groucho')
one_marx1

type(one_marx1)


one_marx2=(56789)
one_marx2

type(one_marx2)

one_marx3=(56789,)
one_marx3

type(one_marx3)



#%% 튜플 만들기 3
# 교재 example
tuple1=(1,2,3,4)
tuple1

tuple2=1,2,3,4   #  tuple2=1,2,3,4,   도 가능
tuple2

type(tuple1)
type(tuple2)

# case 1
marx_tuple1='Groucho', 'Chico', 'Harpo'   #method 1
marx_tuple1

marx_tuple2=('Groucho', 'Chico', 'Harpo')  #method 2
marx_tuple2

type(marx_tuple1)
type(marx_tuple2)


# 주의사항
one_marx='Groucho',

('Groucho',)

type(one_marx)

type('Groucho',)

type( ('Groucho',)  ) 

# case 2
a = ('abc', 123, 3.14, ['edf', 5678], ('Hf', 'ch'))
a
type(a)

b=(['edf', 5678], (('Hf', 'ch'), 'ch'))
b
type(b)



#%% 튜플의 각 요소 출력하기
tuple1

tuple1[0]
tuple1[2]
tuple1[-1]

tuple1[:]
tuple1[0:2]
tuple1[-3:-1]

#%% indexing, slicing
tup=(1, 2, 3, 4, 5, 6, 7)
tup

tup[:]
tup[0]
tup[0:1]
tup[0:3]
tup[1:]
tup[3:]
tup[-1]

tup[-1:]
tup[-3:-1]
tup[-1:]
tup[-3:]


