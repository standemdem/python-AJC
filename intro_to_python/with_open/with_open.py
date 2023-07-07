import datetime

def login():
    a = input("user name : ")
    return a

def addition():
    a = int(input("number 1 : "))
    b = int(input("number 2 : "))

    print(a+b)
    return f"{a} + {b} = {a+b}"

def save_modification(text):
    with open("file.txt", "a") as f:
        if f :
            print("open file.txt")
            f.write(text)

if __name__=='__main__':

    name = login()
    sum =  addition()
    time = (datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M"))

    txt = f"user name : {name}\n : {addition}\n date et heure : {time}\n"

    save_modification(txt)
    pass