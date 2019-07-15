words=['HARSHA','DHANASHREE','SARANG','PIYUSH']
for w in words:
    print(w,len(w))
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
print("FRUIT ADDED")
for w in fruits[:]:
    if(len(w)>2):
        fruits.insert(0,w)
        print(w)
        
        
