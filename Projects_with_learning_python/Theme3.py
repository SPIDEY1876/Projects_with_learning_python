dic_menu={'�����̽� ������':8300,'������':8100,'��':7000,'���׸���':6500}
list_bread=["Honey oat","Hearty Italian","Wheat"]
list_cheeze=["American Cheese","Shredded Cheese","Mozzarella Cheese"]
dic_add={"Meat":1800,"Shrimp Double Up":1800,"Cheese":900,"No":0}
list_vegetable=["Lettuce","Tomatoes","Cucumbers","Peppers","No"]
list_sauce=["Ranch","Mayonnaise","Sweet Onion","No"]
list_cookie=["��Ʈ����","���� ����Ĩ","����Ĩ","��Ʈ�� ������","����� ġ������","ȭ��Ʈ ���� ��ī�ٹ̾�"]
list_drink=["��","����","Ŀ��","ź������"]
list_wedge=["���� ��������","cheesy ���� ��������","bacon Cheesy ���� ��������"]
list_soup=["����ݸ� ü�� ����","����ũ �������� ����"]
list_soda=["coke","soda","doctor pepper"]

class basic_for_single :
    def __init__(self,name="",size1="",menu1="",bread1="",cheese1="",sauce1=[],add1=[],vegetable_except1 = []):
     self.name = name
     self.menu1 = menu1
     self.bread1 = bread1
     self.sauce1 = sauce1
     self.size1 = size1
     self.add1 = add1
     self.vegetable_except1 = vegetable_except1
     self.cheese1 = cheese1
        
    def type(self):
      size = self.size1
      if size == 15:
        return "sandwich"+str(size)+"cm"
      elif size ==30:
        return "sandwich"+str(size)+"cm"

    def bread_and_cheeese (self): 
      bread = self.bread1
      cheese = self.cheese1
  
      choose_toasting=str(input("�佺���� �Ͻðڽ��ϱ�?(Yes/No�θ� ������ּ���):"))
      if choose_toasting=="Yes":#Yes or no�θ� �Է��ϰ� �� ����
        return "toasted "+bread+" include "+cheese
      elif choose_toasting=="No":
        return "Not toasted "+bread+" include "+cheese  
      else :
        print("�߸��Է�")
     
    def add_topping(self):
        add = self.add1
        setadd = set(dic_add.keys())
        set4 = [x for x in add if x not in setadd]
        
        if set4 != [] :
          print("�߸��Է�")
        else :
          if add[0] == "No":
            return "Not Added topping"
          else:
            return "�����߰�:" + ','.join(add)

    def veget (self):
      vegetable_except = self.vegetable_except1
      setvegetable = set(list_vegetable)
      set4 = [x for x in vegetable_except if x not in setvegetable ]

      if set4 != []:
        print("�߸� �Է�")
          
      else:
        return "��ä ����:" + ','.join(vegetable_except)     

    def sauce(self):
      sauce_choose = self.sauce1
      setlist_sauce = set(list_sauce)

      set3 = [x for x in sauce_choose if x not in setlist_sauce]
      if set3 != [] :
        print("�߸��Է�����")

      else :
        return "�ҽ�: "+','.join(sauce_choose)

    def price(self):
      price_1 = dic_menu[self.menu1]
      price_2 = 0
      for x in range(len(self.add1)):
        price_2 = price_2 + dic_add[self.add1[x]]

      price_3 = price_1 + price_2

      return ("<"+self.name+":"+self.menu1+"/���û���_"+str(self.size1)+"/"+str(self.bread_and_cheeese())+"/"+str(self.sauce())+"/"+
              "�߰� ��û-"+str(self.veget())+"/"+str(self.add_topping()) +"/�߰� �ݾ�:"+str(price_2)+"/�� �ݾ�:"+str(price_3)+">")
    def sum_price(self):
        price_1 = dic_menu[self.menu1]
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]

        price_3 = price_1 + price_2
        return price_3

class basic_for_set(basic_for_single): #cookie ���� ó�� ��Ʈ �޴� �� �͵� ��� �߰� ���Ѽ� �ϸ� �� �� ���ƿ�
    def __init__(self,name="",size1="",menu1="",bread1="",cheese1="",sauce1=[],add1=[],vegetable_except1 = [],choose ="",drink=""):
        super().__init__(name,size1,menu1,bread1,cheese1,sauce1,add1,vegetable_except1)
        self.choose =choose
        self.drink = drink

    def Choose_drink(self):
        drink=self.drink
        if drink=="��":
            return drink
        elif drink=="����":
            return drink
        elif drink=="Ŀ��":
            return drink
        elif drink=="ź������":
            print(','.join(list_soda))
            soda=input("ź�������� ������ ���� �����ϴ�. � ������ �Ͻðھ��?:")
            return soda
  
    
    def price(self):
        price_1 = dic_menu[self.menu1]+2000
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]
            price_3 = price_1 + price_2
        return ("<"+self.name+":"+self.menu1+"/���û���_"+str(self.size1)+"/��Ʈ������� ���� 2000�� �߰��Դϴ�./"+str(self.bread_and_cheeese())+"/"+str(self.sauce())+"/��Ʈ�޴�: "+str(self.choose)+"/"+str(self.Choose_drink())+"/"+
              "�߰� ��û-"+str(self.veget())+"/"+str(self.add_topping())+"/�߰� �ݾ�:"+str(price_2)+"/�� �ݾ�: "+str(price_3)+">")
    def sum_price(self):
        price_1 = dic_menu[self.menu1]+2000
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]

        price_3 = price_1 + price_2
        return price_3

class basic_for_salad(basic_for_single):
    def __init__(self,name="",menu1="",cheese1="",sauce1=[],add1=[],vegetable_except1 = []):
        self.name = name
        self.menu1 = menu1
        self.cheese1 = cheese1
        self.sauce1 = sauce1
        self.add1 = add1
        self.vegetable_except1 = vegetable_except1
    def price(self):
        price_1 = dic_menu[self.menu1]+1700
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]
        price_3 = price_1 + price_2
        return ("<"+self.name+":"+self.menu1+"/salad(���� 15cm ��ǰ���� 1700�� �߰��Դϴ�)/"+str(self.sauce())+"/"+
              "�߰� ��û-"+str(self.veget())+"/"+str(self.add_topping()) +"/�߰� �ݾ�:"+str(price_2)+"/�� �ݾ�:"+str(price_3)+">")    
    def sum_price(self):
        price_1 = dic_menu[self.menu1]+1700
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]
        price_3 = price_1 + price_2
        return price_3 
class basic_for_salad_set(basic_for_salad):
    def __init__(self,name="",menu1="",cheese1="",sauce1=[],add1=[],vegetable_except1 = [],choose ="",drink=""):
        super().__init__(name,menu1,cheese1,sauce1,add1,vegetable_except1)
        self.choose=choose
        self.drink=drink
    def Choose_drink(self):
        drink=self.drink
        if drink=="��":
            return drink
        elif drink=="����":
            return drink
        elif drink=="Ŀ��":
            return drink
        elif drink=="ź������":
            print(','.join(list_soda))
            soda=input("ź�������� ������ ���� �����ϴ�. � ������ �Ͻðھ��?:")
            return soda
    def price(self):
        price_1 = dic_menu[self.menu1]+3700
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]
            price_3 = price_1 + price_2
        return ("<"+self.name+":"+self.menu1+"/salad (���� 15cm ��ǰ���� 1700��,��Ʈ��� 2000�� �߰��Դϴ�.)/"+str(self.sauce())+"/��Ʈ�޴�: "+str(self.choose)+"/"+str(self.Choose_drink())+"/"+
              "�߰� ��û-"+str(self.veget())+"/"+str(self.add_topping())+"/�߰� �ݾ�:"+str(price_2)+"/�� �ݾ�: "+str(price_3)+">")
    def sum_price(self):
        price_1 = dic_menu[self.menu1]+3700
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]
        price_3 = price_1 + price_2
        return price_3 
## �����
def input_size_de(x) :
  a = ['15','30']
  if x not in a :
    raise ValueError

def input_menu_de(x) :
  if x not in dic_menu :
    raise ValueError

def decision_de(x):
  a = ['set','single','salad','salad set']
  if x not in a :
    raise ValueError

## �ֹ� ����
n = int(input("����� ��ü �ֹ� �ΰ���?:"))
if n <=0 :
  raise ValueError("0�̻��� ������ �Է��ϼ���")
sum_money=0
for x in range(n):
  input_name = input(str(x+1)+"��° �̸�:")
  print(dic_menu)
  input_menu =input("���� ���� �޴��� �ֽ��ϴ� � ������ �Ͻðھ��?:")
  try :
    input_menu_de(input_menu)
  except ValueError :
    print("�Է� ����� �ϼ���")
    break
  decision = input("Choose one of set, single, salad, salad set:")
  try :
    decision_de(decision)
  except :
    print("�Է��� ����� �ϼ���")
    break

  if decision == "single":
    input_size =str(input("choose length(15/30):"))
    try:
        input_size_de(input_size)
    except ValueError :
        print("�Է� ����� �ϼ���")
        break 
    print(','.join(list_bread))
    input_bread =str(input("���� ���� �� ������ �ֽ��ϴ�. �������� �Ͻðڽ��ϱ� ?:"))
    print(','.join(list_cheeze))
    input_cheese=str(input("���� ���� ġ�� ������ �ֽ��ϴ�.� ���� �����ٰ� �־�帱���?(�ϳ��� ����):"))
    print(dic_add)  
    input_add=str(input("���� ���� ������ �ֽ��ϴ�.������ �߰��� ������ �����ø� No�� �Է����ּ���.), � ������ �Ͻðڽ��ϱ�??:")).split(',')            
    print(','.join(list_vegetable))
    input_vegetable_except =input("���� ���� ������ ��ä�� �ֽ��ϴ�.� ��ä�� ���� �ұ��?(������ ���ý� �� ��ä���� ,�� �����ּ���, ������ No �Է�):").split(',')            
    print(','.join(list_sauce))
    input_sauce=input("���� ���� �ҽ��� �ֽ��ϴ�.� �ҽ��� �帱���?(���ϴ� �ҽ��� ,�� �Է��Ͽ� �ּ���!,������ No �Է�):").split(',')
    
    de_single = basic_for_single(input_name,input_size,input_menu,input_bread,input_cheese,input_sauce,input_add,input_vegetable_except)
    print(de_single.price())
    sum_money+=de_single.sum_price()

  elif decision == "set":
    input_size =str(input("choose length(15/30):"))
    try:
        input_size_de(input_size)
    except ValueError :
        print("�Է� ����� �ϼ���")
        break
    print(','.join(list_bread))
    input_bread =str(input("���� ���� �� ������ �ֽ��ϴ�. �������� �Ͻðڽ��ϱ� ?:"))
    print(','.join(list_cheeze))
    input_cheese=str(input("���� ���� ġ�� ������ �ֽ��ϴ�.� ���� �����ٰ� �־�帱���?(�ϳ��� ����):"))
    print(dic_add)  
    input_add=str(input("���� ���� ������ �ֽ��ϴ�.������ �߰��� ������ �����ø� No�� �Է����ּ���.), � ������ �Ͻðڽ��ϱ�??:")).split(',')            
    print(','.join(list_vegetable))
    input_vegetable_except =input("���� ���� ������ ��ä�� �ֽ��ϴ�.� ��ä�� ���� �ұ��?(������ ���ý� �� ��ä���� ,�� �����ּ���.):").split(',')            
    print(','.join(list_sauce))
    input_sauce=input("���� ���� �ҽ��� �ֽ��ϴ�.� �ҽ��� �帱���?(���ϴ� �ҽ��� ,�� �Է��Ͽ� �ּ���!):").split(',')
    input_choose_set_menu=str(input("��Ʈ �Ŵ����� cookie,chip,wedge�� �ֽ��ϴ�.� ������ �Ͻðھ��?:"))
    if input_choose_set_menu == "cookie" :
      print(','.join(list_cookie))
      choose=str(input("��Ű�� ������ ���� �����ϴ�.� ��Ű�� �Ͻðھ��?:"))    
    elif input_choose_set_menu=="wedge":
      print(','.join(list_wedge))
      choose=str(input("������ ������ ���� �����ϴ�.� ������ �Ͻðھ��?:"))
    elif input_choose_set_menu == "chip" :
      choose="chip"          
    print(','.join(list_drink))
    input_drink=str(input("������ ������ ���� �����ϴ�.� ������ �Ͻðھ��?:"))
    de_set = basic_for_set(input_name,input_size,input_menu,input_bread,input_cheese,input_sauce,input_add,input_vegetable_except,choose,input_drink)
    print(de_set.price())
    sum_money+=de_set.sum_price()

  elif decision=="salad":
    input_size ="salad"
    print(','.join(list_cheeze))
    input_cheese=str(input("���� ���� ġ�� ������ �ֽ��ϴ�.� ���� �����ٰ� �־�帱���?(�ϳ��� ����):"))      
    print(dic_add)  
    input_add=str(input("���� ���� ������ �ֽ��ϴ�.������ �߰��� ������ �����ø� No�� �Է����ּ���.), � ������ �Ͻðڽ��ϱ�??:")).split(',')            
    print(','.join(list_vegetable))
    input_vegetable_except =input("���� ���� ������ ��ä�� �ֽ��ϴ�.� ��ä�� ���� �ұ��?(������ ���ý� �� ��ä���� ,�� �����ּ���, ������ No �Է�):").split(',')        
    print(','.join(list_sauce))
    input_sauce=input("���� ���� �ҽ��� �ֽ��ϴ�.� �ҽ��� �帱���?(���ϴ� �ҽ��� ,�� �Է��Ͽ� �ּ���!,������ No �Է�):").split(',')
    de_salad=basic_for_salad(input_name,input_menu,input_cheese,input_sauce,input_add,input_vegetable_except)
    print(de_salad.price())
    sum_money+=de_salad.sum_price()
  elif decision=="salad set":
    input_size ="salad"
    print(','.join(list_cheeze))
    input_cheese=str(input("���� ���� ġ�� ������ �ֽ��ϴ�.� ���� �����ٰ� �־�帱���?(�ϳ��� ����):"))      
    print(dic_add)  
    input_add=str(input("���� ���� ������ �ֽ��ϴ�.������ �߰��� ������ �����ø� No�� �Է����ּ���.), � ������ �Ͻðڽ��ϱ�??:")).split(',')            
    print(','.join(list_vegetable))
    input_vegetable_except =input("���� ���� ������ ��ä�� �ֽ��ϴ�.� ��ä�� ���� �ұ��?(������ ���ý� �� ��ä���� ,�� �����ּ���, ������ No �Է�):").split(',')        
    print(','.join(list_sauce))
    input_sauce=input("���� ���� �ҽ��� �ֽ��ϴ�.� �ҽ��� �帱���?(���ϴ� �ҽ��� ,�� �Է��Ͽ� �ּ���!,������ No �Է�):").split(',')
    input_choose_set_menu=str(input("��Ʈ �Ŵ����� cookie,chip,wedge�� �ֽ��ϴ�.� ������ �Ͻðھ��?:"))
    if input_choose_set_menu == "cookie" :
      print(','.join(list_cookie))
      choose=str(input("��Ű�� ������ ���� �����ϴ�.� ��Ű�� �Ͻðھ��?:"))    
    elif input_choose_set_menu=="wedge":
      print(','.join(list_wedge))
      choose=str(input("������ ������ ���� �����ϴ�.� ������ �Ͻðھ��?:"))
    elif input_choose_set_menu == "chip" :
      choose="chip"          
    print(','.join(list_drink))
    input_drink=str(input("������ ������ ���� �����ϴ�.� ������ �Ͻðھ��?:"))
    de_salad_set=basic_for_salad_set(input_name,input_menu,input_cheese,input_sauce,input_add,input_vegetable_except,choose,input_drink)
    print(de_salad_set.price())
    sum_money+=de_salad_set.sum_price()
print("�� �ֹ��ݾ�:"+str(sum_money))
