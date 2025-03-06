#admin
import mysql.connector as ms
from prettytable import PrettyTable
from prettytable import from_db_cursor as p
import datetime
import matplotlib.pyplot as plt

from football import *

mycon = ms.connect(host = 'localhost', user = 'root', passwd = 'sql password')

#print(mycon.is_connected())

cur = mycon.cursor()

cur.execute('create database if not exists club')

cur.execute('use club')




def encrypt(string):
    old = string
    new = ""
    for i in old:
        new += chr(ord(i)+4)
    return new[::-1]



                            #6969123

p1 = "sweet_987#"          #sweet_987#
newp1 = encrypt(p1)
p2 = "Banana_23"            #Apple_23         
newp2 = encrypt(p2)


q1 = f'insert into admins values(1, "admin01", "{newp1}")'
q2 = f'insert into admins values(2, "admin02", "{newp2}")'
cur.execute(q1)
cur.execute(q2)



def add_admin():
    try:
        id = int(input('enter primary id:'))
        name = input('enter admin name (7 characters long):')
        password = input('enter a secure password:')
        newp = encrypt(password)
        t1 = (id, name, newp)
        cur.execute(f'insert into admins values {t1}')
        mycon.commit()
        print('succesfful')
        print('\n')
    except Exception:
        print('there waa an error')
        mycon.rollback()



def disp_admin():
    cur.execute('select ad_id, admin_name from admins')
    table = p(cur)
    print(table)
    
def change_password(admin_name, password):
    
    current = input(f'{admin_name} enter current password:')
    if encrypt(current) == password:
        p = input(f'{admin_name} Enter your new password:')
        encp = encrypt(p)
        try:
            cur.execute(f'update admins set password = "{encp}" where admin_name = "{admin_name}"')
            mycon.commit()
            print('Succesfully changed password')
            print('\n')
        except Exception:
            print('There was an error')
            mycon.rollback()
    else:
        print('Incorrect password try again')
        print('\n')



def user_table():
    cur.execute('select * from user')
    table = p(cur)
    print(table)


        
def admin(t1):
    while True:
        print('Hello what would you like to do?')
        print('1.Access football database')
        print('2.Display admin table')
        print('3.Add another admin')
        print('4.Change Passowrd')
        print('5.View User table')
        print('6.Exit')
        ch = input('Enter choice:')
        if ch == '1':
            print('\n')
            football()
        elif ch == '2':
            disp_admin()
        elif ch == '3':
            add_admin()
        elif ch == '4':
            change_password(t1[1],t1[2])
        elif ch =='5':
            user_table()
        elif ch == '6':
            print('Goodbye')
            break
        else:
            print('Enter a valid input')

def admin_login():
    try:
        var1 = input('enter admin name:')
        cur.execute('select admin_name from admins')
        k = cur.fetchall()
        l2 = []
        for i in k:
            l2.append(i[0])
        if var1 in l2:
            cur.execute(f'select * from admins where admin_name = "{var1}"')
            pword = cur.fetchone()
            password = input('enter password:')
            if pword is not None and encrypt(password) == pword[2]:
                print('--LOGIN SUCCESSFUL--')
                print('\n')
                admin(pword)
            else:
                print('--Wrong password or admin name, try again--')
        else:
            print('Admin is not available, try again')
    except Exception:
        print('\n')
        print('There was an error, try again')
        print('\n')
        


