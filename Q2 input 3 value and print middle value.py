# input 3 value and print middle value

a = float(input("Enter Value A:"))
b = float(input("Enter Value B:"))
c = float(input("Enter Value C:"))

if((a<b) and (a>c) or (a>b) and (a<c) ):
    print(a)

elif(((b<a) and (b>c)) or ((b>a) and (b<c))):
    print(b)

elif((c<b) and (c>a) or (c>b) and (c<a)):
    print(c)

else:
    print("error")
   


    