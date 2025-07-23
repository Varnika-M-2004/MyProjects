import mysql.connector
import pandas as pd
import mysql.connector as sqltor
import pymysql
from sqlalchemy import create_engine
engine=create_engine('mysql+pymysql://root:root123@localhost/clientinfo')
con=sqltor.connect(host='localhost', user='root', passwd='root123', database='clientinfo')
mycon=engine.connect()
display1=print('WELCOME TO PERFECT JODI MATCHMAKING SERVICE')
display2=print('1. Register')
display3=print('2. Login')
name=[]
surname=[]
username=[]
password=[]
age=[]
gender=[]
profession=[]
address=[]
contact=[]
email=[]
religion=[]
hobbies=[]
p_age=[]
p_job=[]
p_religion=[]
p_looks=[]

choice=int(input('Enter your choice no.: '))
if choice==1:
    print('Login session started')
    for i in range(1):
        cursor=con.cursor()
        Username=input('Enter username: ')
        query = """Select Username from clientinfo where Username = %s;"""
        cursor.execute(query, (Username,))
        record=cursor.fetchone()
        user=record[0]
        if Username in user:
            print('Username already exists')

        else:
            print('Valid username')

        con.commit()
        con.close()

        pw=input('Enter your password: ')
        upper='false'
        lower='false'
        digit='false'
        if len(pw)>=8 and len(pw)<=14:
            for i in range(len(pw)):
                if pw[i].isupper:
                    upper='True'
                if pw[i].islower:
                    lower='True'
                if pw[i].isdigit:
                    digit='True'
            print('Valid Password')
        else:
            print('Password should be between 8 to 14 char having U,L and digits')
            re=input('re-enter the password: ')
        nm=input('Enter your First Name: ')
        sm=input('Enter your Last Name: ')
        ag=int(input('Enter your Age: '))
        gen=input('Enter your Gender: ')
        pr=input('Enter your Email: ')
        username.append(un)
        password.append(pw)
        name.append(nm)
        surname.append(sm)
        age.append(ag)
        gender.append(gen)
        email.append(pr)
    dict1={'Username':username, 'Password':password}
    dict2={'Username':username, 'Name':name, 'Surname':surname, 'Age':age, 'Gender':gender, 'Email':email}
    df1=pd.DataFrame.from_dict(dict1, orient='index').transpose()
    df2=pd.DataFrame.from_dict(dict2, orient='index').transpose()
    df1.to_sql('clientinfo', mycon, index=False, if_exists='append')
    df2.to_sql('profile', mycon, index=False, if_exists='append')
    print('Thank you for registering with us')

choice2=input('Do you want to continue? (yes/no): ')

if choice2=='yes' or choice==2:
    user=input('Enter username: ')
    if user==Username:
        print('Valid')
    else:
        print('Re-enter')
        reuser=input('Re enter username: ')
    passw=input('Enter password: ')
    if passw==password:
        print('Valid')
        print('Logged in')
    else:
        print('Re-enter')
        repass=input('Re enter password: ')


if gen=='M':
    print('Enter your profile details: ')
    for i in range(1):
        nm=input('Enter your First Name: ')
        sm=input('Enter your Last Name: ')
        ag=int(input('Enter your Age: '))
        gen=input('Enter your Gender: ')
        pr=input('Enter your Profession: ')
        ad=input('Enter your address: ')
        ph=int(input('Enter your mobile number: '))
        em=input('Enter your email id: ')
        re=input('Enter your religion: ')
        lk=input('Enter your hobbies: ')
        ip=input("Expected partner's age: ")
        fm=input("Expected partner's job: ")
        hm=input("Expected partner's religion: ")
        jm=input("Expected partner's looks: ")
        username.append(un)
        name.append(nm)
        surname.append(sm)
        age.append(ag)
        gender.append(gen)
        profession.append(pr)
        address.append(ad)
        contact.append(ph)
        email.append(em)
        religion.append(re)
        hobbies.append(lk)
        p_age.append(ip)
        p_job.append(fm)
        p_religion.append(hm)
        p_looks.append(jm)

    dict3={'Username':username, 'Name':name, 'Surname':surname, 'Age':age, 'Gender':gender, 'Profession':profession, 'Address':address, 'Mobile_no':contact, 'Email':email, 'Religion':religion, 'Hobbies':hobbies, 'Partner_age':p_age, 'partner_job':p_job, 'Partner_religion':p_religion, 'Partner_looks':p_looks}
    df3=pd.DataFrame.from_dict(dict3, orient='index').transpose()
    df3.to_sql('profile', mycon, index=False, if_exists='append')
    print('Profile made')
    choice3=input('Do you want to continue looking for bride profiles? (yes/no):')
    if choice3=='yes':
        print('Bride Profiles: ')
        x=pd.read_sql("Select * from profile where Gender='F';", mycon)
        print(x)
    if choice3=='no':
        print('Please look for bride details')

if gen=='F':
    print('Enter your profile details: ')
    for i in range(1):
        nm=input('Enter your First Name: ')
        sm=input('Enter your Last Name: ')
        ag=int(input('Enter your Age: '))
        gen=input('Enter your Gender: ')
        pr=input('Enter your Profession: ')
        ad=input('Enter your address: ')
        ph=int(input('Enter your mobile number: '))
        em=input('Enter your email id: ')
        re=input('Enter your religion: ')
        lk=input('Enter your hobbies: ')
        ip=input("Expected partner's age: ")
        fm=input("Expected partner's job: ")
        hm=input("Expected partner's religion: ")
        jm=input("Expected partner's looks: ")
        username.append(un)
        name.append(nm)
        surname.append(sm)
        age.append(ag)
        gender.append(gen)
        profession.append(pr)
        address.append(ad)
        contact.append(ph)
        email.append(em)
        religion.append(re)
        hobbies.append(lk)
        p_age.append(ip)
        p_job.append(fm)
        p_religion.append(hm)
        p_looks.append(jm)

    dict4={'Username':username, 'Name':name, 'Surname':surname, 'Age':age, 'Gender':gender, 'Profession':profession, 'Address':address, 'Mobile_no':contact, 'Email':email, 'Religion':religion, 'Hobbies':hobbies, 'Partner_age':p_age, 'partner_job':p_job, 'Partner_religion':p_religion, 'Partner_looks':p_looks}
    df4=pd.DataFrame.from_dict(dict4, orient='index').transpose()
    df4.to_sql('profile', mycon, index=False, if_exists='append')
    print('Profile made')

    choice4=input('Do you want to continue looking for groom profiles? (yes/no):')
    if choice4=='yes':
        print('Groom Profiles: ')
        y=pd.read_sql("Select * from profile where Gender='M';", mycon)
        print(y)
    if choice4=='no':
        print('Please look for Groom details')


        
