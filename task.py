#Task:
#2*2=4
#3*3*3=27....


a=int(input("Enter a number:-"))

for j in range(2,a+1):
    sapmple="{}".format(j)*j
    print("*",join(sample),"=",j**j)
    

