import  smtplib
def get_useremail():
    useremail=input('enter user email')
    if '@' in useremail and '.com' in useremail:
        service=['gmail','outlook','yahoo']
        count=0
        for i in service:
            if i in useremail:
                return useremail,i
            else:
                count+=1
            if count==len(service):
                print('we only provide gmail,outlook,yahoo service ')
    else:
        print("your useremail is invalid")
        useremail=input("again enter user email")

usermail,service=get_useremail()
print(usermail,service)









# connection=smtplib.SMTP('smtp.gmail.com',587)
# connection.ehlo
# connection.starttls()
# connection.login('ramanprasad.0203@gmail.com','Raman@123')
# connection.sendmail('ramanprasad.0203@gmail.com','rewatiraman.0203@gmail.com','subject:this is subject \n\n\t hello Raman ')
# connection.quit()
