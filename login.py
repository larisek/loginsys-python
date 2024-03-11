def login():
    import os
    import time
    with open('registersys/passwords.txt', 'r') as p:
        while True:
            os.system("cls")
            print("Login")
            name = input("Name: ")
            passwd = input("Password: ")
            print("Verifying")
            time.sleep(3)
            os.system("cls")
            x = p.read()
            y = name + ":" + passwd
            if f"{y}" in x:
                break