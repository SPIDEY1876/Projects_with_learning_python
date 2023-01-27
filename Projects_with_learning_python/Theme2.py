
# '선수이름' : [골, 어시스트, 키, 포지션, 나이, 점수]
# 'son':[14,9,183,'공격수',28,0]
import random
cm=random.randrange(160,201,10)
p = ['공격수','수비수','골키퍼','미드필더']
position = random.choice(p)
age=random.randrange(20,41,5)
print("감독이 좋아하는 선수 성향:","키",cm,"이상","&",position,"포지션","&",age,"세 미만","(감독의 성향에 만족하지 못한다고 해서 감점이 되지는 않습니다. 단, 선수의 나이가",age+5,"세 이상일 경우 감점 발생)")
n=int(input('fa상태인 선수는 몇명인가요??:'))#선수 입력
profile={}
a=0
while a<n :
  key=input("선수이름:")
  val1=int(input('골 점수 :'))
  if val1 <0 :
  	raise ValueError("0이상의 정수만 입력하세요")
  val2=int(input('어시스트 점수 :'))
  if val2 <0 :
  	raise ValueError("0이상의 정수만 입력하세요")  
  val3=int(input('키 :'))
  val4=input('포지션 :')
  val5=int(input('나이 :'))
  l=[val1,val2,val3,val4,val5,0]
  profile[key]=l
  a=a+1

#골, 어시스트
def G (a) :
  """선수의 골점수x2+선수의 어시스트점수를 계산해 각 선수의 점수에 추가 """
  for i in a:
    a[i][5] = a[i][5] + a[i][0]*2 + a[i][1]
  return a

#키
def T (a) :
  """선수의 키가 감독이 원한는 키 이상일 경우 각 선수의 점수에 3점 추가, 미만일 경우 pass"""
  for i in a:
    if a[i][2]>=cm:
     a[i][5] = a[i][5] + 3
  return a

#포지션
def P (a) :
  """ 선수의 포지션이 감독이 원하는 포지션일 경우 각 선수의 점수에 5점 추가, 아닐 경우 pass"""
  for i in a:
    if a[i][3]==position:
     a[i][5] = a[i][5] + 5
  return a

#나이
def A (a) :
  """선수의 나이가 감독이 원하는 나이보다 아래일 경우 각 선수의 점수에 곱5/4, 아닐경우 곱1/2"""
  for i in a:
    assert a[i][4]!=0,"나이를 제대로 입력했나요?"
    if a[i][4] >= age+5 :
      a[i][5] = int(a[i][5]*(1/2))
    elif a[i][4] < age:
      a[i][5] = a[i][5]*(5/4)
  return a

new_List=A( P( T( G(profile))))

point=0
man=[]
for i in new_List:
  if new_List[i][5]>point:
    man.clear()
    point = new_List[i][5]
    man.append(i)
  elif new_List[i][5]==point:
    point = new_List[i][5]
    man.append(i)

k = list( map(str , man))
result = ','.join(k)
print("")
print(result)
print("")
answer=input('각 함수에 대한 상세 설명이 필요한가요?(입력은 "예" or "아니요"만 입력가능):')
assert answer=='예'or answer=='아니요', '예,아니요만 입력해주세요!'
if answer=='예':
  print(help(G),help(T),help(P),help(A))