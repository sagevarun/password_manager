master_pwd = input("Enter Mater password to open list ")


def view():
    while True:
        pass_wrd = input("Enter Master PWD to view list ")
        if pass_wrd == master_pwd:
            with open('passwords.txt','r') as f:
                for line in f.readlines():
                    data = line.rstrip()
                    usr,pwd = data.split("->")
                    print(f"username: {usr}, password: {pwd}")
            break        
        else:
            print("Wrong master password, try again!!")
            continue

def add(usr_name,pwd):
    with open("passwords.txt",'a') as f:
        f.write(usr_name + "->" + pwd + '\n')

while True:
    mode = input("Would you want to view existing password or add a new password (view/add)? Press q to quit ")
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        usr_name = input("Enter username: ")
        pwd = input("Enter password: ")
        add(usr_name,pwd)
    else:
        print("Invalid mode!")
        continue