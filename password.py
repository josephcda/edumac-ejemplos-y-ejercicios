user_password = "445455454454555"
password = "jaja"
count = 0
while user_password != password:
    password = raw_input("Dame tu password ")
    if user_password == password :
        print "Entraste"
    else :
        print "You shall not pass"
    count +=1
    if count == 10:
        break
