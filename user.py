user=input("username:")
if user.isalnum() and 6<=len(user)<=15:
    print("valid usename")
else:
    print("invalid username")