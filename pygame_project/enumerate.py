'''
enumerate()
열거(enumerate)객체를 반환하는 함수.
시퀀스와 

'''
arrs = ["가", "나", "다"]
print("enumerate(list) = ", enumerate(arrs))
print("enumerate(list) = ", list(enumerate(arrs)))
for idx, val in enumerate(arrs): 
  print("idx = ", idx, "/ val = ", val)
