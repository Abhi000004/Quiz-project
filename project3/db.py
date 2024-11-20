'''
Name- Abhijeet singh parmar
Enrollment- 0157CY221006
Quiz Project2(File Handling)
'''
import time
import mysql.connector as my
con=my.connect(host="localhost",user="root",passwd="Abhijeet@12",database="pro")
cur=con.cursor()

def username():
    while(True):
        uname=input("Create username: ")
        sql="SELECT EXISTS(SELECT 1 FROM user WHERE username = %s)"
        val=(uname,)
        cur.execute(sql,val)
        exists=cur.fetchone()[0]
        length=len(uname)
        if exists:
            print(f"Username {uname} is already occupied")
            print()
        elif length>20 or length<4:
            print('Length of Username must be in between 4 to 20 words')
            print()
        elif uname.isalnum()==False:
            print('Username can not contain any special characters')
            print()
        else:
            return uname
        con.commit()

def password():
    while(True):
        pas=input("Create your password: ")
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
                    special=1
        if length>=8 and length<=20:
            if lower==0:
                print("Password should contain atleast 1 lower case alphabet")
                print()
            elif upper==0:
                print("Password should contain atleast 1 upper case alphabet")
                print()
            elif digit==0:
                print("Password should contain atleast 1 digit")
                print()
            elif special==0:
                print("Password should contain atleast 1 special character")
                print()
            else:
                return pas
        else:
             print("Length of the password must in between (8 to 20)")
             print()

def register():
    name=input("Enter your name: ")
    print()
    uname=username()
    upass=password()
    print()
    print(f"user {name} has registered successfully")
    print()
    sql=f"insert into user(username,password,name) values (%s,%s,%s)"
    val=(uname,upass,name,)
    cur.execute(sql,val)
    con.commit()

def login():
    while(True):
        uname=input("Enter your registered username: ")
        sql="SELECT EXISTS(SELECT 1 FROM user WHERE username = %s)"
        val=(uname,)
        cur.execute(sql,val)
        exists=cur.fetchone()[0]
        if exists:
            while(True):
                upass=input("Enter your password: ")
                sql="SELECT password FROM user WHERE username = %s"
                val=(uname,)
                cur.execute(sql,val)
                result=cur.fetchone()
                spass=result[0]
                if spass == upass:
                    return uname
                else:
                     print("Incorrect Password!")
                     print()
                con.commit()
        else:
            print(f"username {uname} is not registered")
            print()

def cpp(uname):
    uname=uname
    sql="select * from cpp order by rand() limit 5"
    cur.execute(sql)
    res=cur.fetchall()
    count=0
    for i in res:
        temp=str(i)
        temp1=temp.split(",")
        qs=str(temp1[1])
        print(qs[2:-1])
        op1=str(temp1[2])
        print('A)',op1[2:-1])
        op2=str(temp1[3])
        print('B)',op2[2:-1])
        op3=str(temp1[4])
        print('C)',op3[2:-1])
        op4=str(temp1[5])
        print('D)',op4[2:-1])
        tempans=str(temp1[6])
        ans=tempans[2:-2]
        result=input("Enter your answer: ")
        res=result.upper()
        if res==ans:
            print("Correct")
            count+=1
        else:
            print(f"Incorrect!, correct option is {tempans}")
    print(f'Your score is {count}/5')
    print()
    result1=f"CPP {count}/5 "
    current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sql=f"insert into result(uname,results,datetime) values (%s,%s,%s)"
    val=(uname,result1,current_datetime,)
    cur.execute(sql,val)
    con.commit()
    con.commit()
    
def java(uname):
    uname=uname
    sql="select * from java order by rand() limit 5"
    cur.execute(sql)
    res=cur.fetchall()
    count=0
    for i in res:
        temp=str(i)
        temp1=temp.split(",")
        qs=str(temp1[1])
        print(qs[2:-1])
        op1=str(temp1[2])
        print('A)',op1[2:-1])
        op2=str(temp1[3])
        print('B)',op2[2:-1])
        op3=str(temp1[4])
        print('C)',op3[2:-1])
        op4=str(temp1[5])
        print('D)',op4[2:-1])
        tempans=str(temp1[6])
        ans=tempans[2:-2]
        result=input("Enter your answer: ")
        res=result.upper()
        if res==ans:
            print("Correct")
            count+=1
        else:
            print(f"Incorrect!, correct option is {tempans}")
    print(f'Your score is {count}/5')
    print()
    result1=f"Java {count}/5 "
    current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sql=f"insert into result(uname,results,datetime) values (%s,%s,%s)"
    val=(uname,result1,current_datetime,)
    cur.execute(sql,val)
    con.commit()
    con.commit()

def python(uname):
    uname=uname
    sql="select * from python order by rand() limit 5"
    cur.execute(sql)
    res=cur.fetchall()
    count=0
    for i in res:
        temp=str(i)
        temp1=temp.split(",")
        qs=str(temp1[1])
        print(qs[2:-1])
        op1=str(temp1[2])
        print('A)',op1[2:-1])
        op2=str(temp1[3])
        print('B)',op2[2:-1])
        op3=str(temp1[4])
        print('C)',op3[2:-1])
        op4=str(temp1[5])
        print('D)',op4[2:-1])
        tempans=str(temp1[6])
        ans=tempans[2:-2]
        result=input("Enter your answer: ")
        res=result.upper()
        if res==ans:
            print("Correct")
            count+=1
        else:
            print(f"Incorrect!, correct option is {tempans}")
    print(f'Your score is {count}/5')
    print()
    result1=f"Python {count}/5 "
    current_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sql=f"insert into result(uname,results,datetime) values (%s,%s,%s)"
    val=(uname,result1,current_datetime,)
    cur.execute(sql,val)
    con.commit()
    con.commit()

def display(uname):
      uanme=uname
      sql=f" SELECT * FROM result WHERE uname='{uanme}'"
      cur.execute(sql)
      res=cur.fetchall()
      for i in res:
          temp=str(i)
          temp1=temp.split(",")
          dt=temp1[3]
          print('DateTime->',dt[2:-2])
          score=temp1[2]
          print('Score->',score[2:-2])
      con.commit()
      print()

def quiz():
    uname=login()
    print()
    print(f'Welcome {uname} to the quiz')
    print()
    while(True):
        print("Press 1: To C++")
        print("Press 2: To Java")
        print("Press 3: To Python")
        print("Press 4: To display past result")
        print("Press 5: To Logout")
        n=input("Enter your choice: ")
        print()
        if n=='1':
            cpp(uname)
        elif n=='2':
            java(uname)
        elif n=='3':
            python(uname)
        elif n=='4':
            display(uname)
        elif n=='5':
            print(f'User {uname} has logged out!!')
            break
        else:
            print("Kindly enter a valid choice!!")

while(True):
    print('Press 1: To Register')
    print('Press 2: To Login')
    print('Press 3: To Exit')
    print()
    choice=input("Enter your choice: ")
    print()
    if choice=='1':
        register()
    elif choice=='2':
        quiz()

    elif choice=='3':
        break
    else:
        print('Kindly enter a valid choice')
print('You have exit the Quiz')

