import os
import random
# enter number section
try:
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
except:
    print("please enter just number!")
# create new file section
if os.path.exists("c:\\users\ALI\desktop\Random.txt"):
    os.remove("c:\\users\ALI\desktop\Random.txt")
else:
    file=open("c:\\users\ALI\desktop\Random.txt","x")
for rand in range (5):
    random_num = random.randrange(num1,num2)
    rand=rand+1
    file=open("c:\\users\ALI\desktop\Random.txt","a")
    file.write(str(random_num)+"\n")