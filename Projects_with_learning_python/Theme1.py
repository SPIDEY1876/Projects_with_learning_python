
m = int(input("���� �˻� �ιٵ� ������ ? : ",))
inbody_m = int(input("�̹��˻� �ιٵ� ������? :",))
w=0

while w<3 : 
  if (inbody_m - m ) > 0 :
    print("�̴�� ��ϼ���")
    if w<3 :
      break
    
  else:
    ecr = int(input("��ȹ�� ��% ��õ�߳���?"))

    if ecr != 100 :
      ecp = input ("���� ���� ? :")
      rcp = input ("��õ ����? :")

      if ecp == rcp :
        print("� ��ȹ �Ϻ��� ��Ű����")
        w = int(w+1)
        print("���� ��� �� : ",w)

      else:
        print("��õ ��ҿ� ��ȹ �� �� ��Ű����")
        w = int(w+2)
        print("���� ��� �� : ",w)

    else :
      ecp = input ("���� ���� ? : ")
      rcp = input ("��õ ����? :")
      if ecp == rcp :
        print("pt �ܰ� ���")
        if w<3:
          break
         
      else :
         print("��� ��Ű����")
         w = int(w+1)
         print("���� ��� �� : ",w)

  if w<3 :
    m = inbody_m
    inbody_m = int(input("���Ӱ� �˻��� �ιٵ� ������? : "))

if w >= 3 :
   print("����� ��� �� ������ ���� �� �����ϴ�!")


