from Main import main
import hashlib as hl   

def register():
    username = input("Enter A Username")
    password = input("Enter A Password")
    password = hl.sha256(password.encode('utf')).hexdigest()
    with open("login_info.txt", "a") as f:
        f.write(f"{username},{password}\n")

def login():
    with open("login_info.txt", "r") as f:
        username = input("Enter A Username: ")
        lines = f.readlines()
        for line in lines:
          if line.startswith(username):
            password = input("Enter A Password: ")
            password = hl.sha256(password.encode('utf')).hexdigest()
            if line == username+","+password+"\n":
                menu(True, username)
            else:
                print("Password Incorrect")
                menu(False, 0)
    print("Couldn't Find Username")
    menu(False, 0)
            
        

def menu(logged_in, username):
    while True:
        if logged_in:
            print(f"LOGGED IN AS: {username}")
        else:
            print("LOG IN OR REGISTER:")
        print("1) Start\n2) Register\n3) Login\n4) Quit")
        option = input(">>> ")
        if option == "1":
          if logged_in == True:
            start()
          else:
            print("You Need To Login. If You Don't Have An Account Then Register")
        elif option == "2":
          register()
        elif option == "3":
          login()
        elif option == "4":
          quit()
        else:
          print("Invalid Option")

menu(False, 0)
