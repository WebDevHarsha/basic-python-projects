import string
import random

def pw_generator(length_pw):
    special=input("do u want special characters in the password? (y/n)  ")
    numb=input("do u want numbers in the password? (y/n)  ")
    
    ch=string.ascii_letters
    n=string.digits
    speci=string.punctuation
    
    pw=""
    # numb_in=False
    # char_in=False
    # spec_in=False
    
    whole=ch+n+speci
    
    if special=="y" and numb=="y":
        if len(pw)<length_pw:
            for i in range(length_pw):
                rand=random.choice(whole)
                pw=pw+rand
                
    print(pw)
            
    
pw_generator(10)