#Basics of conditonal statements
age=24
if(age>=18):
    print("can vote")
    print("can apply for licence")

light="pink"
if(light=="green"):
    print("go")
elif(light=="red"):
    print("STOP!")
elif(light=="yellow"):
    print("wait")
else:
    print("light is broken!!")

#WAP input marks from user & print their grade

marks = int(input("enter your marks:"))
if(marks >= 80):
    print("your grade is A+",marks)
elif(marks >=70 and marks <80):
    print("your grade is A" ,marks)
elif(marks <69 and marks >65):
    print("your grade is A-" , marks)
elif(marks <=65 and marks >60):
    print("your grade is B+" , marks)
elif(marks >55 and marks <=60):
    print("your grade is B" ,marks)
elif(marks >50 and marks <=55):
 print("your grade is C",marks)
elif(marks >40 and marks <=50):
 print("your grade is D" ,marks)
else:
    print("You have failed in exam.")
