import json
#from cryptography import fernet




def load_password():
    with open ("text2.json", "r") as f :
        return json.load(f)    

def save_password(passwords):
    with open ("text2.json", "w") as f :
        json.dump(passwords, f) 
            
def add_password():
    site = input("whats the site: ")
    user = input("user name : ")
    pw = input("whats the password? ")
    passwords = load_password()
    passwords.append({"site": site, "user": user, "password": pw})
    save_password(passwords)
    print("password saved :)")
        
        
def view_passwords():
    passwords = load_password()
    for i, p in enumerate(passwords):
        print(f"{i+1}. {p['site']} - {p['user']}")
                
        
        
##def encryption():
  #  load_password()
   # key = fernet.generate_key(f)
    #f = fernet(key)
    #token = f.encrypt(b"A really secret message. Not for prying eyes.")
    #token


while True:
    masssge = input("add / view / q: ")
    if masssge == "add" :
        add_password()
    elif masssge == "view":
        view_passwords()
        
    else:
        break
        
