
# '�����̸�' : [��, ��ý�Ʈ, Ű, ������, ����, ����]
# 'son':[14,9,183,'���ݼ�',28,0]
import random
cm=random.randrange(160,201,10)
p = ['���ݼ�','�����','��Ű��','�̵��ʴ�']
position = random.choice(p)
age=random.randrange(20,41,5)
print("������ �����ϴ� ���� ����:","Ű",cm,"�̻�","&",position,"������","&",age,"�� �̸�","(������ ���⿡ �������� ���Ѵٰ� �ؼ� ������ ������ �ʽ��ϴ�. ��, ������ ���̰�",age+5,"�� �̻��� ��� ���� �߻�)")
n=int(input('fa������ ������ ����ΰ���??:'))#���� �Է�
profile={}
a=0
while a<n :
  key=input("�����̸�:")
  val1=int(input('�� ���� :'))
  if val1 <0 :
  	raise ValueError("0�̻��� ������ �Է��ϼ���")
  val2=int(input('��ý�Ʈ ���� :'))
  if val2 <0 :
  	raise ValueError("0�̻��� ������ �Է��ϼ���")  
  val3=int(input('Ű :'))
  val4=input('������ :')
  val5=int(input('���� :'))
  l=[val1,val2,val3,val4,val5,0]
  profile[key]=l
  a=a+1

#��, ��ý�Ʈ
def G (a) :
  """������ ������x2+������ ��ý�Ʈ������ ����� �� ������ ������ �߰� """
  for i in a:
    a[i][5] = a[i][5] + a[i][0]*2 + a[i][1]
  return a

#Ű
def T (a) :
  """������ Ű�� ������ ���Ѵ� Ű �̻��� ��� �� ������ ������ 3�� �߰�, �̸��� ��� pass"""
  for i in a:
    if a[i][2]>=cm:
     a[i][5] = a[i][5] + 3
  return a

#������
def P (a) :
  """ ������ �������� ������ ���ϴ� �������� ��� �� ������ ������ 5�� �߰�, �ƴ� ��� pass"""
  for i in a:
    if a[i][3]==position:
     a[i][5] = a[i][5] + 5
  return a

#����
def A (a) :
  """������ ���̰� ������ ���ϴ� ���̺��� �Ʒ��� ��� �� ������ ������ ��5/4, �ƴҰ�� ��1/2"""
  for i in a:
    assert a[i][4]!=0,"���̸� ����� �Է��߳���?"
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
answer=input('�� �Լ��� ���� �� ������ �ʿ��Ѱ���?(�Է��� "��" or "�ƴϿ�"�� �Է°���):')
assert answer=='��'or answer=='�ƴϿ�', '��,�ƴϿ丸 �Է����ּ���!'
if answer=='��':
  print(help(G),help(T),help(P),help(A))