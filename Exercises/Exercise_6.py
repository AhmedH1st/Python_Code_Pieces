

#Python Code that Handles Login System

login_sys = {
    "Ahmed": "1394",
    "Ali" : "6078",
    "Amr" : "9345"
}

UserName = input("Enter Your User name : ")
Password = input("Enter Your Password : " )

if login_sys.get(UserName) == Password:
    print("Welcome Sir")
else:
    print("Access Denied") 
