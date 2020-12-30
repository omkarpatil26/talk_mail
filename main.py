import smtplib
import speech_recognition as sr
import pyttsx3
import email
from email.message import EmailMessage
from email.mime.text import MIMEText


listener = sr.Recognizer()
engine=pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source :
            print('listening...')
            voice=listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sender@gmail.com','sender@123')
    #email ['From']='from@gmail.com'
    #email ['To'] = receiver
    #email ['Subject']=subject
    #email ['content']=message
    sender = 'sender@gmail.com'
    talk ( 'To whom you want to send email' )
    name = get_info ()
    receiver = email_list[name]
    print ( receiver )
    #talk ( 'What is the subject of your email?' )
    #subject = get_info ()

    talk ( 'Tell me the subject of your email' )
    Subject = get_info ()
    subject = Subject


    talk ( 'Tell me the text in your email' )
    message = get_info ()
    content = message

    #email.set_content(message, content_manager=None, **kw)
    #email.set_content(str(message))
    #server.sendmail('sender', 'receiver@gmail.com','Hi this is the mail')

    server.sendmail (  sender , receiver , subject,  content )
    # sending the mail
    #server.sendmail ( From , To , EmailMessage )



    #server.send_message(email)





email_list = {
  #list of mails

}

def get_email_info():
    '''
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()

    talk('Tell me the text in your email')
    message = get_info()
    '''

    send_email ()

    talk('Hey, Your email is sent')
    talk('if you want to send other email?  reply yes else anything')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    else:
        print('Thankyou!!')


get_email_info()



