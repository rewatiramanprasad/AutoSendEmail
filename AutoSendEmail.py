import  smtplib
import webbrowser
def get_useremail():
    while True:
        useremail=input('enter user e-mail id:')
        if '@' in useremail and useremail.endswith('.com'):
            service=['gmail','outlook','yahoo']
            count=0
            for i in service:
                if i in useremail:
                    return useremail,i
                

                else:
                    count+=1


                if count==len(service):
                    print('we only provide gmail,outlook,yahoo service ')
                    print("Re-enter your usermail again ")
                    continue
        else:
            print("your useremail is invalid")
            continue





def set_smtp(service):
    serviceprovider='smtp.'+service+'.com'
    return serviceprovider



if __name__ == "__main__":
    print('welcome  you can send your email through this python program')
    usermail,service=get_useremail()
    password=input('enter your Password:')
    smtpdomain=set_smtp(service)
    print(smtpdomain)
    connection=smtplib.SMTP(smtpdomain,587)
    connection.ehlo
    connection.starttls()
    while True:
        try:
            print(usermail,password)
            connection.login(usermail,password)
            print('hola')
            
        except:
            if service=='gmail':
                print("Login Unsucessful,There are probably 2 reason:\n 1:your input email id or  password is wrong\n2:you dont turn on allow less secure option")
                print("wanna check 2nd option once")
                answer=input("yes or no?")
                if answer =='yes':
                    webbrowser.open("https://myaccount.google.com//lesssecureapps")
                else:
                    print('go to https://myaccount.google.com//lesssecureapps and turn on the option')
                    print('Re-enter your email')
                    usermail,service=get_useremail()
                    password=input('enter your Password:')
                    continue
        else:
            print('Login Succesful')
            break
    print('Enter your receiver email')
    receivermail,st=get_useremail()
    subject=input('Subject:')
    message=input('message:')
    connection.sendmail(usermail,receivermail,'Subject:'+str(subject)+'\n\n'+str(message))
    print('E-mail Send Successful')
    connection.quit()
    
