''' Q1. Password Strength Checker

Take a password input from the user.
Check if the password is strong based on this logic:

Length ≥ 8
Contains @ or #
Does not start with a number

 If all are true, print: "Strong Password"
Otherwise, print: "Weak Password" '''

psw = input("Enter a password:")

a=len(psw)
b = psw.count("@")
c = psw.count("#")
x = b+c
d = psw[0]


if(a<8):
    print("requre minimum Password lenth 8")
elif(x == 0):
    print("Must have # or @ in password")
elif(d.isdigit()):
    print("Password can't start with Numbers")
else:
    print("Strong Password")

    
