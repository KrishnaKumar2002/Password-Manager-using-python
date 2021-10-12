##Hello guys Myself Krishna Kumar,

#  this is a passward manager program in which we are going to save our 
#           1)name of site
#           2)username
#           3)passward 
#           in our pc as a text file without storing it on the third party storage 
#           in a encryted cipher form so that when we open that text it is safe that our password and sensitive data 
#           will not be in a understandable format and we can authenticate 
#           and view our passwords username of multiple site at ease

def encrypt(data,shift):
    encrypted=""

    for i in range(len(data)):
        char=data[i]
        if(char.isupper()):
            encrypted+=char((ord(char)+shift-65)%26+65)

        elif(char.islower()):
            encrypted+=char((ord(char)+shift-97)%26+97)

        elif(char.isdigit()):
            number=(int(char)+shift)%10
            encrypted+=str(number)

        else:
            encrypted+=char

    return encrypted



def decrypt(data,shift):
    decrypted=""

    for i in range(len(data)):
        char=data[i]
        if(char.isupper()):
            decrypted+=char((ord(char)-shift-65)%26+65)

        elif(char.islower()):
            decrypted+=char((ord(char)-shift-97)%26+97)

        elif(char.isdigit()):
            number=(int(char)-shift)%10
            decrypted+=str(number)

        else:
            decrypted+=char

    return decrypted


menu=''
if menu!='1' or menu!='2':
    menu=input("would you like to save or view the login info \n 1)save new login info \n 2)view our login info \n 3)exit")

if menu=='1':
    softwareName=input("Enter the name of the software")
    username=input("Enter the Username for the software")
    password=input("Enter the password for the software")
    shift=6
    file=open("securePasswordData.txt",'a')
    file.write(encrypt(softwareName,shift)+";|"+encrypt(username,shift)+";|"+encrypt(password,shift)+"\n")
    file.close()

elif menu=='2':
    print("Displaying Login info")
    file=open("securePasswordData.txt",'r')
    print("Software \t Username \t Password\n")
    for i in file:
        shift=6
        data=i.split(";|")
        print(decrypt(data[0],shift)+'\t\t'+decrypt(data[1],shift)+'\t\t'+decrypt(data[2],shift))
        
else:
    exit()
