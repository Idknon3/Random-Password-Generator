import random
from os import system

characterPass = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j',
                 'k','l','z','x','c','v','b','n','m']
specialChar = ['.','/','?',':','\\','%','!','@','#','$','^','&','*','-','_','=','+']
upperCase = [cp.upper() for cp in characterPass]
integreal = [0,1,2,3,4,5,6,7,8,9]
length = 0

def generator():
    system("cls")
    randompass = ''.join(str(random.choice(characterPass+specialChar+upperCase+integreal))for i in range(length))
    file = open("password.txt",'w+')
    file.write("Password Length: "+str(length))
    #for i in range(0, length):
    print(str(randompass))
    file.write("\n"+str(randompass))
            
    return length

while True:
    print("Password Save in passowrd.txt ")
    try:
       length = int(input("Enter The Password Length:"))

    except ValueError:
            length = 0 
            print("Not Correct Value!")
            
    generator()