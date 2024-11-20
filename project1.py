'''
Name- Abhijeet singh parmar
Enrollment- 0157CY221006
Problem statement- Project1
'''
import random
reg_uname=[]
reg_upass=[]
def username():
    while(True): 
        name=input("Create your username: ")   
        if name in reg_uname:
            print("Username already exists")
        else:
            if len(name)>0 and len(name)<=20:
                return name
            else:
                print("The length of username must be 0<username<20")

def password():
    while(True):
        pas=input("Create your password: ")
        l1=["@","#","%"]
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
                    if i not in l1:
                        special=1
                    else:
                        special=0
        if length>=8 and length<=20:
            if lower==0:
                print("Password should contain atleast 1 lower case alphabet")
            elif upper==0:
                print("Password should contain atleast 1 upper case alphabet")
            elif digit==0:
                print("Password should contain atleast 1 digit")
            elif special==0:
                print("Password should contain atleast 1 special character except(@,#,%)")
            else:
                return pas
        else:
             print("Length of the password must in between (8 to 20)")
        
def register():
    uname=username()
    upass=password()
    reg_uname.append(uname)
    reg_upass.append(upass)
    print(f"\n{uname} is registered successfully")

def login():
    while(True):
        uname=input("Enter your registered username: ")
        if uname not in reg_uname:
            print(f"\n{uname} is not registred\n")
        else:
            upass=input("Enter your password: ")
            a=int(reg_uname.index(uname))
            if reg_upass[a]==upass:
                print(f"\n Welcome {uname} to quiz")
                break
            else:
                print("\nEntered password is incorrect\n")

def python():
    dic_py={'What is the correct way to define a variable in Python?\na) variable = value\nb) value = variable\nc) var: value\nd) define variable = value':'a',
                    'Which data type is used to represent a sequence of characters in Python?\na) int\nb) float\nc) str\nd) bool':'c',
                    'How do you comment a single line in Python?\na) // This is a comment\nb) # This is a comment\nc) /* This is a comment */\nd) ; This is a comment':'b',
                    'Which operator is used for integer division in Python?\na) /\nb) //\nc) %\nd) **':'b',
                    'How do you create an if-else statement in Python?\na) if condition: statement1\nb) if condition: statement1 else: statement2\nc) if condition then statement1\nd) if condition { statement1; }':'b',
                    'What is the purpose of a while loop in Python?\na) To execute a block of code repeatedly until a condition becomes false.\nb) To execute a block of code a fixed number of times.\nc) To create functions.\nd) To define variables.':'a',
                    'How do you define a function in Python?\na) function name(): statements\nb) def name(): statements\nc) create function name(): statements\nd) function name(arguments): statements':'b',
                    'What is the purpose of the return statement in a Python function?\na) To define the function name.\nb) To end the function execution.\nc) To return a value from the function.\nd) To take input arguments for the function.':'c',
                    'How do you import a module named mymodule in Python?\na) import mymodule\nb) include mymodule\nc) use mymodule\nd) load mymodule':'a',
                    'How do you access the first element of a list named my_list in Python?\na) my_list[0]\nb) my_list.first()\nc) my_list(0)\nd) my_list[1]':'a',
                    'How do you get input from the user in Python?\na) input()\nb) get_input()\nc) read_input()\nd) input_value()':'a',
                    'How do you print a message to the console in Python?\na) print()\nb) display()\nc) show()\nd) output()':'a',
                    'What is the purpose of a try-except block in Python?\na) To handle errors that may occur during program execution.\nb) To define functions.\nc) To create loops.\nd) To import modules.':'a',
                    'What is the difference between a list and a tuple in Python?\na) Lists are mutable, while tuples are immutable.\nb) Lists are immutable, while tuples are mutable.\nc) Both lists and tuples are mutable.\nd) Both lists and tuples are immutable.':'a',
                    'How do you create a set in Python?\na) using curly braces\nb) using square brackets []\nc) using parentheses ()\nd) using the set() function':'a',
                    'What is the purpose of a dictionary in Python?\na) To store a sequence of elements.\nb) To store key-value pairs.\nc) To store a set of unique elements.\nd) To define functions.':'b',
                    'What is a class in Python?\na) A blueprint for creating objects.\nb) A collection of functions.\nc) A data type.\nd) A variable.':'a',
                    'What is a module in Python?\na) A collection of functions and classes.\nb) A data type.\nc) A variable.\nd) An object.':'a',
                    'What is a package in Python?\na) A collection of modules.\nb) A data type.\nc) A variable.\nd) An object.':'a',
                    'How do you import the math module in Python?\na) import math\nb) include math\nc) use math\nd) load math':'a'
                    } 
    count=0
    li=random.sample(list(dic_py.keys()), 5)
    for key in li:
        print(key)
        res=input("Enter your answer: ")
        res.lower()
        if dic_py[key]==res:
            print("Correct")
            count+=1
        else:
            print("Incorrect")
    if count>=3:
        print("\nPASS\n")
    else:
        print("\nFAIL\n")

def cpp():
    dic_cpp={'What is the correct syntax to declare a variable in C++?\na) variable = value\nb) value = variable\nc) var: value\nd) datatype variable_name;':'d',
             'Which data type is used to represent whole numbers in C++?\na) int\nb) float\nc) char\nd) string':'a',
             'What is the difference between int and long in C++?\na) int is used for smaller integers, long is used for larger integers\nb) int is used for larger integers, long is used for smaller integers\nc) There is no difference between int and long\nd) int is used for floating-point numbers, long is used for integers':'a',
             'How do you declare a constant variable in C++?\na) const variable_name = value;\nb) variable_name const = value;\nc) constant variable_name = value;\nd) define variable_name = value;':'a',
             'Which operator is used for logical AND in C++?\na) &&\nb) ||\nc) !\nd) ^':'a',
             'How do you increment the value of a variable x by 1 in C++?\na) x++\nb) x--\nc) ++x\nd) All of the above':'d',
             'How do you create an if-else statement in C++?\na) if (condition) { statement1; } else { statement2; }\nb) if condition then statement1 else statement2\nc) if condition: statement1 else: statement2\nd) if (condition) statement1 else statement2':'a',
             'What is the purpose of the break statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'a',
             'What is the purpose of the continue statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'b',
             'How do you define a function in C++?\na) function name() { statements; }\nb) def name(): statements\nc) void name() { statements; }\nd) function name(arguments) { statements; }':'c',
             'What is the purpose of the return statement in a function?\na) Exits the function\nb) Returns a value from the function\nc) Declares a new variable\nd) Defines a function':'b',
             'What is a pointer in C++?\na) A variable that stores the address of another variable\nb) A constant value\nc) A data type\nd) A function':'a',
             'How do you dereference a pointer in C++?\na) Using the * operator\nb) Using the & operator\nc) Using the -> operator\nd) Using the [] operator':'a',
             'How do you declare an array in C++?\na) array name[size];\nb) name array[size];\nc) size array name;\nd) array[size] name;':'a',
             'What is the index of the first element in a C++ array?\na) 0\nb) 1\nc) -1\nd) The size of the array':'a',
             'How do you access the third element of an array named arr in C++?\na) arr[3]\nb) arr(3)\nc) arr.3\nd) *arr[3]':'a',
             'What is a string in C++?\na) An array of characters\nb) A data type\nc) A function\nd) A constant value':'a',
             'What is a class in C++?\na) A blueprint for creating objects\nb) A data type\nc) A function\nd) A constant value':'a',
             'How do you define a class in C++?\na) class name { };\nb) struct name { };\nc) define name { };\nd) class name() { };':'a',
             'What is an object in C++?\na) An instance of a class\nb) A data type\nc) A function\nd) A constant value':'a',
             }
    count=0
    li=random.sample(list(dic_cpp.keys()),5)
    for key in li:
        print(key)
        res=input("Enter your answer: ")
        if dic_cpp[key]==res:
            print("Correct")
            count+=1
        else:
            print("Incorrect")
    if count>=3:
        print("\nPASS\n")
    else:
        print("\nFAIL\n")

def java():
    dic_java={'What is the default data type for integer literals in Java?\na) int\nb) long\nc) short\nd) byte':'a',
              'Which data type is used to represent a single character in Java?\na) char\nb) string\nc) byte\nd) boolean':'a',
              'How do you declare a constant variable in Java?\na) final variable_name = value;\nb) constant variable_name = value;\nc) const variable_name = value;\nd) define variable_name = value;':'a',
              'Which operator is used for logical OR in Java?\na) &&\\nb) ||\nc) !\nd) ^':'b',
              'How do you increment the value of a variable x by 1 in Java?\na) x++\nb) x--\nc) ++x\nd) All of the above':'d',
              'How do you create an if-else statement in Java?\na) if (condition) { statement1; } else { statement2; }\nb) if condition then statement1 else statement2\nc) if condition: statement1 else: statement2\nd) if (condition) statement1 else statement2':'a',
              'What is the purpose of the break statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'a',
              'What is the purpose of the continue statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'b',
              'How do you define a function in Java?\na) function name() { statements; }\nb) def name(): statements\nc) void name() { statements; }\nd) function name(arguments) { statements; }':'c',
              'What is the purpose of the return statement in a function?\na) Exits the function\nb) Returns a value from the function\nc) Declares a new variable\nd) Defines a function':'b',
              'How do you declare an array in Java?\na) array name[size];\nb) name array[size];\nc) size array name;\nd) array[size] name;':'a',
              'What is the index of the first element in a Java array?\na) 0\nb) 1\nc) -1\nd) The size of the array':'a',
              'How do you access the third element of an array named arr in Java?\na) arr[3]\nb) arr(3)\nc) arr.3\nd) *arr[3]':'a',
              'What is a class in Java?\na) A blueprint for creating objects\nb) A data type\nc) A function\nd) A constant value':'a',
              'How do you define a class in Java?\na) class name { };\nb) struct name { };\nc) define name { };\nd) class name() { };':'a',
              'What is an object in Java?\na) An instance of a class\nb) A data type\nc) A function\nd) A constant value':'a',
              'How do you create an object of a class in Java?\na) class_name object_name;\nb) object_name = class_name;\nc) new class_name;\nd) create object_name':'a',
              'What is the purpose of the this keyword in Java?\na) Points to the current object\nb) Points to the base class\nc) Points to the derived class\nd) Points to the function':'a',
              'Which keyword is used to inherit properties from a base class in Java?\na) extends\nb) inherits\nc) public\nd) implements':'a',
            }
    count=0
    li=random.sample(list(dic_java.keys()),5)
    for key in li:
        print(key)
        res=input("Enter your answer: ")
        if dic_java[key]==res:
            print("Correct")
            count+=1
        else:
            print("Incorrect")
    if count>=3:
        print("\nPASS\n")
    else:
        print("\nFAIL\n")

def con():
    con=input("If you want to exit press: (N/n) \nElse press any key to continue: ")
    con.lower()
    if con=='n':
        return False
    
def quiz():
    while(True):
        print("\npress 1: Python")
        print("press 2: c++")
        print("press 3: java")
        n=int(input("choose a laguage: "))
        if n==1:
            print("\nPython\n")
            python()
            if con()==False:
                break
        elif n==2:
            print("\nC++\n")
            cpp()
            if con()==False:
                break
        elif n==3:
            print("\nJava\n")
            java()
            if con()==False:
                break
        else:
            print("Kindly enter a valid choice")

    
while(True):
    print("\nPress 1: To register new user")
    print("Press 2: To login")
    print("Press 3: To exit")
    n=int(input("Enter your choice: "))
    if n==1:
        register()
    elif n==2:
        login()
        quiz()
    elif n==3:
        print("You have exit the quiz")
        break
    else:
        print("Kindly enter a valid choice")

