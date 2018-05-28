#_author:"Zoom"
#date: 2018/3/21
# for i in range(1,101,2):
#    print("loop:",i)

# for i in range(100):
#     if i < 50 or i > 70:
#         print(i)

_user = "alex"
_passwd = "abc123"
for i in range(3):
    username = input("Username:")
    password = input("Password:")

    if username == _user and password == _passwd:
        print("welcome %s login..." %_user)
        break
    else:
        print("Invalid username or password!")
