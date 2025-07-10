'''student marks analyzer
Input dictionary:
{"Amit": 76, "Riya": 89, "Raj": 56, "Pooja": 92}
Print names of students who scored above 75.'''

# "Amit": 76, "Riya": 89, "Raj": 56, "Pooja": 92


dict1 = {}
a = int(input("Enter Number of Students:"))


for dict2 in range(0,a):
    dict2 = {input("Enter Name:"):int(input("Enter Marks:"))}
    dict1.update(dict2)

# dict2={"Amit": 76, "Riya": 89, "Raj": 56, "Pooja": 92}

# dict1.update(dict2)

name = dict1.keys()
marks = dict1.values()

x = tuple(marks)
y = tuple(name)
# print(x,y)
b = -1
for i in x:
    b +=1
    if i < 75:
        continue
    print(y[b]) 
    
# for i in range(0,b)