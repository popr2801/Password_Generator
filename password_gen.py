import string, random

def generate_password(lenght,mode):
    if(mode=="letters"):
        characters = string.ascii_letters
    elif(mode=="digits"):
        characters = string.digits
    else:
        characters = string.ascii_letters + string.digits
    
    password = ''.join(random.choice(characters) for i in range(lenght))
    return password

lenght = int(input("Hello!Please enter the number of characters for your password:\n"))
mode = input("Now select between letters/digits/both:\n")
while(lenght > 30):
    lenght = int(input("Password can't be longer than 30 characters:\n"))

password = generate_password(lenght,mode)          
print(f"Your password is: {password}")  
print("Nice")   
