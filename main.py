print("Register system")
while True:
    print("Login")
    print("Register")
    choos = input().lower()
    if choos == str("login"):
        from login import login
        login()
        break
    elif choos == str("register"):
        from register import reg
        reg()
print("Všechno je ok")