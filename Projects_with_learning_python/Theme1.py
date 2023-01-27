
m = int(input("저번 검사 인바디 근육량 ? : ",))
inbody_m = int(input("이번검사 인바디 근육량? :",))
w=0

while w<3 : 
  if (inbody_m - m ) > 0 :
    print("이대로 운동하세요")
    if w<3 :
      break
    
  else:
    ecr = int(input("계획을 몇% 실천했나요?"))

    if ecr != 100 :
      ecp = input ("현재 운동장소 ? :")
      rcp = input ("추천 운동장소? :")

      if ecp == rcp :
        print("운동 계획 완벽히 지키세요")
        w = int(w+1)
        print("누적 경고 수 : ",w)

      else:
        print("추천 장소와 계획 둘 다 지키세요")
        w = int(w+2)
        print("누적 경고 수 : ",w)

    else :
      ecp = input ("현재 운동장소 ? : ")
      rcp = input ("추천 운동장소? :")
      if ecp == rcp :
        print("pt 쌤과 상담")
        if w<3:
          break
         
      else :
         print("장소 지키세요")
         w = int(w+1)
         print("누적 경고 수 : ",w)

  if w<3 :
    m = inbody_m
    inbody_m = int(input("새롭게 검사한 인바디 근육량? : "))

if w >= 3 :
   print("당신은 운동을 할 생각이 없는 것 같습니다!")


