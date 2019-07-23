print("ENter your name")
Name = input("Enter Your Name : ")
print("Enter your Email")
Email = input("Enter your Email: ")
print("Enter your age")
age = input("Enter you age: ")
print("Enter your Number")
number=input("Enter your Number: ")


def yes_or_no(question):
    reply = str(input( yes_or_no +' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    else:
        return False



f = open('File.txt', 'w')
f.write('Name: '+ Name)
f.write("\n")
f.write('Email: '+ Email)
f.write("\n")
f.write('Age: '+ age)
f.write("\n")
f.write('Number:'+ number)
f.write("\n")
f.close()
