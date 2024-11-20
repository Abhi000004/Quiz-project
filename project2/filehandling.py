from random import*
import time

def username(unamefile,unameread,reg):
     while(True):
        uname=input("Create your Username: \n")
        length=int(len(uname))
        if uname in reg:
            print(f'{uname} is already occupied\n')
        elif length>20 or length<4:
            print('Length of Username must be in between 4 to 20 words\n')
        elif uname.isalnum()==False:
            print('Username can not contain special characters\n')
        else:
            unamefile.write(f'\n{uname}')
            unamefile.close()
            unameread.close()
            return uname

def password(upassfile,name):
    while(True):
            uname=name
            pas=input("Create your password: \n")
            length=len(pas)
            lower=0
            upper=0
            digit=0
            special=0
            for i in pas:
                    if i.isdigit():
                        digit=1
                    elif i.isalpha():
                        if i.isupper():
                            upper=1
                        elif i.islower():
                            lower=1
                    else:        
                        if i.isalnum()==False:
                            special=1
            if length>=8 and length<=20:
                if lower==0:
                    print("Password should contain atleast 1 lower case alphabet\n")
                elif upper==0:
                    print("Password should contain atleast 1 upper case alphabet\n")
                elif digit==0:
                    print("Password should contain atleast 1 digit")
                elif special==0:
                    print("Password should contain atleast 1 special character \n")
                else:
                    upassfile.write(f'\n{uname}{pas}')
                    upassfile.close()
                    break
            else:
                print("Length of the password must in between (8 to 20)\n")

    with open(f'{uname}.txt','w')as user:
        user.write(f"Username={uname}\nPassword={pas}")
        user.close()

def registration():
    unamefile=open('uname.txt','a')
    unameread=open('uname.txt','r')
    upassfile=open('password.txt','a')
    reguname=unameread.readlines()
    reg=str(reguname)
    name=username(unamefile,unameread,reg)
    password(upassfile,name)
    print(f'\nUsername {name} has registered sccessfully\n')

def login():
    filen=open('uname.txt','r')
    filep=open('password.txt','r')
    storedn=filen.readlines()
    storedp=filep.readlines()
    stored_pass=str(storedp)
    stored_uname=str(storedn)

    while(True):  
        input_uname=input("Enter your registered Username: \n") 
        if input_uname in stored_uname:
            while(True):
                input_password=input("Enter your password: \n")
                res=''
                res=input_uname+input_password
                if res in stored_pass:
                    print(f'{input_uname} has logged in\n')
                    filen.close()
                    filep.close()
                    return input_uname
                else:
                    print('Wrong password\n')
        else:
            print(f'{input_uname} is not registered\n')         

def python():
    sub='PYTHON'
    with open('python.txt','r') as file:
        stored=file.readlines()
        python=choices(stored,k=5)
        count=0
        for i in python:
            str1=i.replace("$","\n")
            trim=str1.rstrip()
            ans=trim[-1]
            print(trim[:-2])
            ans1=input("\nEnter your answer: ")
            if ans1==ans:
                count+=1
                print("Correct\n")
            else:
                print("Incorrect\n")
    if count>2:
        print('Your score is: ',count)
        file.close()
        return count,sub
    else:
        print('Your score is: ',count)
        file.close()
        return count,sub

def cpp():
    sub='CPP'
    with open('cpp.txt','r') as file:
        stored=file.readlines()
        cpp=choices(stored,k=5)
        count=0
        for i in cpp:
            str1=i.replace("$","\n")
            trim=str1.rstrip()
            ans=trim[-1]
            print(trim[:-2])
            ans1=input("\nEnter your answer: ")
            if ans1==ans:
                count+=1
                print("Correct\n")
            else:
                print("Incorrect\n")
    if count>2:
        print('Your score is: ',count)
        file.close()
        return count,sub
    else:
        print('Your score is: ',count)
        file.close()
        return count,sub

def java():
    sub='JAVA'
    with open('java.txt','r') as file:
        stored=file.readlines()
        java=choices(stored,k=5)
        count=0
        for i in java:
            str1=i.replace("$","\n")
            trim=str1.rstrip()
            ans=trim[-1]
            print(trim[:-2])
            ans1=input("\nEnter your answer: ")
            if ans1==ans:
                count+=1
                print("Correct\n")
            else:
                print("Incorrect\n")
    if count>2:
        print('Your score is: ',count)
        file.close()
        return count,sub
    else:
        print('Your score is: ',count)
        file.close()
        return count,sub

def quiz(name):
    while(True):
        uname=name
        print("Press 1: To Python")
        print("Press 2: To c++")
        print("Press 3: To java")
        print("Press 4: To Show past result")
        print("Press 5: To Logout")
        n=int(input("Enter your choice: "))

        if n==1:
            print("\nPython\n")
            res,sub=python()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            file=open(f'{uname}.txt','a')
            file.write(f'\n{sub} Your score was {res}/5 at  {current_time}')
            file.close()
        elif n==2:
            print("\nC++\n")
            res,sub=cpp()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            file=open(f'{uname}.txt','a')
            file.write(f'\n{sub} Your score was {res}/5 at {current_time}')
            file.close()
        elif n==3:
            print("\nJava\n")
            res,sub=java()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            file=open(f'{uname}.txt','a')
            file.write(f'\n{sub} Your score was {res}/5 at  {current_time}')
            file.close()
        elif n==4:
           file1=open(f'{uname}.txt','r')
           for i in file1:
               print(i)
           file1.close()
        elif n==5:
            print(f'{uname} has logout\n')
            break
        else:
            print("Kindly enter a valid choice")


print('Welcome to the Quiz\n')
while(True):
    print('Press 1: To Register\n')
    print('Press 2: To Login\n')
    print('Press 3: To Exit\n')
    choice=int(input("Enter your choice: "))
    print('\n')
    if choice==1:
        registration()
    elif choice==2:
        name=login()
        quiz(name)

    elif choice==3:
        break
    else:
        print('Kindly enter a valid choice\n')
print('You have exit the Quiz')