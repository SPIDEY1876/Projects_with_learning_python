dic_menu={'스파이시 쉬림프':8300,'쉬림프':8100,'햄':7000,'에그마요':6500}
list_bread=["Honey oat","Hearty Italian","Wheat"]
list_cheeze=["American Cheese","Shredded Cheese","Mozzarella Cheese"]
dic_add={"Meat":1800,"Shrimp Double Up":1800,"Cheese":900,"No":0}
list_vegetable=["Lettuce","Tomatoes","Cucumbers","Peppers","No"]
list_sauce=["Ranch","Mayonnaise","Sweet Onion","No"]
list_cookie=["민트초코","더블 초코칩","초코칩","오트밀 레이즌","라즈베리 치즈케익","화이트 초코 마카다미아"]
list_drink=["물","우유","커피","탄산음료"]
list_wedge=["웨지 포테이토","cheesy 웨지 포테이토","bacon Cheesy 웨지 포테이토"]
list_soup=["브로콜리 체다 수프","베이크 포테이토 수프"]
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
  
      choose_toasting=str(input("토스팅을 하시겠습니까?(Yes/No로만 대답해주세요):"))
      if choose_toasting=="Yes":#Yes or no로만 입력하게 할 예정
        return "toasted "+bread+" include "+cheese
      elif choose_toasting=="No":
        return "Not toasted "+bread+" include "+cheese  
      else :
        print("잘못입력")
     
    def add_topping(self):
        add = self.add1
        setadd = set(dic_add.keys())
        set4 = [x for x in add if x not in setadd]
        
        if set4 != [] :
          print("잘못입력")
        else :
          if add[0] == "No":
            return "Not Added topping"
          else:
            return "토핑추가:" + ','.join(add)

    def veget (self):
      vegetable_except = self.vegetable_except1
      setvegetable = set(list_vegetable)
      set4 = [x for x in vegetable_except if x not in setvegetable ]

      if set4 != []:
        print("잘못 입력")
          
      else:
        return "야채 제외:" + ','.join(vegetable_except)     

    def sauce(self):
      sauce_choose = self.sauce1
      setlist_sauce = set(list_sauce)

      set3 = [x for x in sauce_choose if x not in setlist_sauce]
      if set3 != [] :
        print("잘못입력했음")

      else :
        return "소스: "+','.join(sauce_choose)

    def price(self):
      price_1 = dic_menu[self.menu1]
      price_2 = 0
      for x in range(len(self.add1)):
        price_2 = price_2 + dic_add[self.add1[x]]

      price_3 = price_1 + price_2

      return ("<"+self.name+":"+self.menu1+"/선택사항_"+str(self.size1)+"/"+str(self.bread_and_cheeese())+"/"+str(self.sauce())+"/"+
              "추가 요청-"+str(self.veget())+"/"+str(self.add_topping()) +"/추가 금액:"+str(price_2)+"/총 금액:"+str(price_3)+">")
    def sum_price(self):
        price_1 = dic_menu[self.menu1]
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]

        price_3 = price_1 + price_2
        return price_3

class basic_for_set(basic_for_single): #cookie 변수 처럼 세트 메뉴 할 것들 계속 추가 시켜서 하면 될 거 같아요
    def __init__(self,name="",size1="",menu1="",bread1="",cheese1="",sauce1=[],add1=[],vegetable_except1 = [],choose ="",drink=""):
        super().__init__(name,size1,menu1,bread1,cheese1,sauce1,add1,vegetable_except1)
        self.choose =choose
        self.drink = drink

    def Choose_drink(self):
        drink=self.drink
        if drink=="물":
            return drink
        elif drink=="우유":
            return drink
        elif drink=="커피":
            return drink
        elif drink=="탄산음료":
            print(','.join(list_soda))
            soda=input("탄산음료의 종류는 위와 같습니다. 어떤 것으로 하시겠어요?:")
            return soda
  
    
    def price(self):
        price_1 = dic_menu[self.menu1]+2000
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]
            price_3 = price_1 + price_2
        return ("<"+self.name+":"+self.menu1+"/선택사항_"+str(self.size1)+"/세트비용으로 인해 2000원 추가입니다./"+str(self.bread_and_cheeese())+"/"+str(self.sauce())+"/세트메뉴: "+str(self.choose)+"/"+str(self.Choose_drink())+"/"+
              "추가 요청-"+str(self.veget())+"/"+str(self.add_topping())+"/추가 금액:"+str(price_2)+"/총 금액: "+str(price_3)+">")
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
        return ("<"+self.name+":"+self.menu1+"/salad(기존 15cm 단품에서 1700원 추가입니다)/"+str(self.sauce())+"/"+
              "추가 요청-"+str(self.veget())+"/"+str(self.add_topping()) +"/추가 금액:"+str(price_2)+"/총 금액:"+str(price_3)+">")    
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
        if drink=="물":
            return drink
        elif drink=="우유":
            return drink
        elif drink=="커피":
            return drink
        elif drink=="탄산음료":
            print(','.join(list_soda))
            soda=input("탄산음료의 종류는 위와 같습니다. 어떤 것으로 하시겠어요?:")
            return soda
    def price(self):
        price_1 = dic_menu[self.menu1]+3700
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]
            price_3 = price_1 + price_2
        return ("<"+self.name+":"+self.menu1+"/salad (기존 15cm 단품에서 1700원,세트비용 2000원 추가입니다.)/"+str(self.sauce())+"/세트메뉴: "+str(self.choose)+"/"+str(self.Choose_drink())+"/"+
              "추가 요청-"+str(self.veget())+"/"+str(self.add_topping())+"/추가 금액:"+str(price_2)+"/총 금액: "+str(price_3)+">")
    def sum_price(self):
        price_1 = dic_menu[self.menu1]+3700
        price_2 = 0
        for x in range(len(self.add1)):
            price_2 = price_2 + dic_add[self.add1[x]]
        price_3 = price_1 + price_2
        return price_3 
## 디버깅
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

## 주문 시작
n = int(input("몇명의 단체 주문 인가요?:"))
if n <=0 :
  raise ValueError("0이상의 정수만 입력하세요")
sum_money=0
for x in range(n):
  input_name = input(str(x+1)+"번째 이름:")
  print(dic_menu)
  input_menu =input("위와 같은 메뉴가 있습니다 어떤 것으로 하시겠어요?:")
  try :
    input_menu_de(input_menu)
  except ValueError :
    print("입력 제대로 하세요")
    break
  decision = input("Choose one of set, single, salad, salad set:")
  try :
    decision_de(decision)
  except :
    print("입력을 제대로 하세요")
    break

  if decision == "single":
    input_size =str(input("choose length(15/30):"))
    try:
        input_size_de(input_size)
    except ValueError :
        print("입력 제대로 하세요")
        break 
    print(','.join(list_bread))
    input_bread =str(input("위와 같은 빵 종류가 있습니다. 무엇으로 하시겠습니까 ?:"))
    print(','.join(list_cheeze))
    input_cheese=str(input("위와 같은 치즈 종류가 있습니다.어떤 것을 빵에다가 넣어드릴까요?(하나만 선택):"))
    print(dic_add)  
    input_add=str(input("위와 같은 토핑이 있습니다.토핑을 추가할 생각이 없으시면 No를 입력해주세요.), 어떤 것으로 하시겠습니까??:")).split(',')            
    print(','.join(list_vegetable))
    input_vegetable_except =input("위와 같은 종류의 야채가 있습니다.어떤 야채를 제외 할까요?(여러개 선택시 각 야채사이 ,로 적어주세요, 없으면 No 입력):").split(',')            
    print(','.join(list_sauce))
    input_sauce=input("위와 같은 소스가 있습니다.어떤 소스로 드릴까요?(원하는 소스를 ,로 입력하여 주세요!,없으면 No 입력):").split(',')
    
    de_single = basic_for_single(input_name,input_size,input_menu,input_bread,input_cheese,input_sauce,input_add,input_vegetable_except)
    print(de_single.price())
    sum_money+=de_single.sum_price()

  elif decision == "set":
    input_size =str(input("choose length(15/30):"))
    try:
        input_size_de(input_size)
    except ValueError :
        print("입력 제대로 하세요")
        break
    print(','.join(list_bread))
    input_bread =str(input("위와 같은 빵 종류가 있습니다. 무엇으로 하시겠습니까 ?:"))
    print(','.join(list_cheeze))
    input_cheese=str(input("위와 같은 치즈 종류가 있습니다.어떤 것을 빵에다가 넣어드릴까요?(하나만 선택):"))
    print(dic_add)  
    input_add=str(input("위와 같은 토핑이 있습니다.토핑을 추가할 생각이 없으시면 No를 입력해주세요.), 어떤 것으로 하시겠습니까??:")).split(',')            
    print(','.join(list_vegetable))
    input_vegetable_except =input("위와 같은 종류의 야채가 있습니다.어떤 야채를 제외 할까요?(여러개 선택시 각 야채사이 ,로 적어주세요.):").split(',')            
    print(','.join(list_sauce))
    input_sauce=input("위와 같은 소스가 있습니다.어떤 소스로 드릴까요?(원하는 소스를 ,로 입력하여 주세요!):").split(',')
    input_choose_set_menu=str(input("세트 매뉴에는 cookie,chip,wedge가 있습니다.어떤 것으로 하시겠어요?:"))
    if input_choose_set_menu == "cookie" :
      print(','.join(list_cookie))
      choose=str(input("쿠키의 종류는 위와 같습니다.어떤 쿠키로 하시겠어요?:"))    
    elif input_choose_set_menu=="wedge":
      print(','.join(list_wedge))
      choose=str(input("웨지의 종류는 위와 같습니다.어떤 것으로 하시겠어요?:"))
    elif input_choose_set_menu == "chip" :
      choose="chip"          
    print(','.join(list_drink))
    input_drink=str(input("음료의 종류는 위와 같습니다.어떤 것으로 하시겠어요?:"))
    de_set = basic_for_set(input_name,input_size,input_menu,input_bread,input_cheese,input_sauce,input_add,input_vegetable_except,choose,input_drink)
    print(de_set.price())
    sum_money+=de_set.sum_price()

  elif decision=="salad":
    input_size ="salad"
    print(','.join(list_cheeze))
    input_cheese=str(input("위와 같은 치즈 종류가 있습니다.어떤 것을 빵에다가 넣어드릴까요?(하나만 선택):"))      
    print(dic_add)  
    input_add=str(input("위와 같은 토핑이 있습니다.토핑을 추가할 생각이 없으시면 No를 입력해주세요.), 어떤 것으로 하시겠습니까??:")).split(',')            
    print(','.join(list_vegetable))
    input_vegetable_except =input("위와 같은 종류의 야채가 있습니다.어떤 야채를 제외 할까요?(여러개 선택시 각 야채사이 ,로 적어주세요, 없으면 No 입력):").split(',')        
    print(','.join(list_sauce))
    input_sauce=input("위와 같은 소스가 있습니다.어떤 소스로 드릴까요?(원하는 소스를 ,로 입력하여 주세요!,없으면 No 입력):").split(',')
    de_salad=basic_for_salad(input_name,input_menu,input_cheese,input_sauce,input_add,input_vegetable_except)
    print(de_salad.price())
    sum_money+=de_salad.sum_price()
  elif decision=="salad set":
    input_size ="salad"
    print(','.join(list_cheeze))
    input_cheese=str(input("위와 같은 치즈 종류가 있습니다.어떤 것을 빵에다가 넣어드릴까요?(하나만 선택):"))      
    print(dic_add)  
    input_add=str(input("위와 같은 토핑이 있습니다.토핑을 추가할 생각이 없으시면 No를 입력해주세요.), 어떤 것으로 하시겠습니까??:")).split(',')            
    print(','.join(list_vegetable))
    input_vegetable_except =input("위와 같은 종류의 야채가 있습니다.어떤 야채를 제외 할까요?(여러개 선택시 각 야채사이 ,로 적어주세요, 없으면 No 입력):").split(',')        
    print(','.join(list_sauce))
    input_sauce=input("위와 같은 소스가 있습니다.어떤 소스로 드릴까요?(원하는 소스를 ,로 입력하여 주세요!,없으면 No 입력):").split(',')
    input_choose_set_menu=str(input("세트 매뉴에는 cookie,chip,wedge가 있습니다.어떤 것으로 하시겠어요?:"))
    if input_choose_set_menu == "cookie" :
      print(','.join(list_cookie))
      choose=str(input("쿠키의 종류는 위와 같습니다.어떤 쿠키로 하시겠어요?:"))    
    elif input_choose_set_menu=="wedge":
      print(','.join(list_wedge))
      choose=str(input("웨지의 종류는 위와 같습니다.어떤 것으로 하시겠어요?:"))
    elif input_choose_set_menu == "chip" :
      choose="chip"          
    print(','.join(list_drink))
    input_drink=str(input("음료의 종류는 위와 같습니다.어떤 것으로 하시겠어요?:"))
    de_salad_set=basic_for_salad_set(input_name,input_menu,input_cheese,input_sauce,input_add,input_vegetable_except,choose,input_drink)
    print(de_salad_set.price())
    sum_money+=de_salad_set.sum_price()
print("총 주문금액:"+str(sum_money))
