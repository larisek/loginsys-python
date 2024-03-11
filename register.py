def reg():
    import os
    import time
    with open('registersys/passwords.txt', 'w') as p:
        while True:
            os.system("cls")
            print("Registrace")
            name = input("Name: ")
            passwd = input("Password: ")
            reppass = input("Repeat password: ")
            print("Verifying")
            time.sleep(3)
            os.system("cls")
            if str(passwd) == str(reppass):
                wrote = f"{name}:{passwd}"
                p.write(wrote)
                p.flush()
                input("Registrace proběhla úspěšně...")
                break
            else:
                print("Něco se pokazilo")
                time.sleep(3)