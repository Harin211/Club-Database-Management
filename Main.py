import mysql.connector as ms
from prettytable import PrettyTable
from prettytable import from_db_cursor as p
#import datetime
#import matplotlib.pyplot as plt

from football import *
from admin import *
from user import *
mycon = ms.connect(host = 'localhost', user = 'root', passwd = 'sql password')

#print(mycon.is_connected())

cur = mycon.cursor()


cur.execute('create database if not exists club')

cur.execute('use club')



#----------------------------------------------------------Initial-------------------------------------------------------------------------#



cur.execute('''create table if not exists user(
player_id int ,
password varchar(20),
fname varchar(20),
lname varchar(20),
available boolean,
physio varchar(20),
private_sess varchar(20),
primary key(player_id)
)
''')








f1 = '''
    CREATE TABLE IF NOT EXISTS football_player (
        player_id INT UNIQUE KEY,
        fname VARCHAR(20) NOT NULL,
        lname VARCHAR(20) NOT NULL,
        DOB DATE,
        nationality VARCHAR(20),
        salary INT,
        green_points INT,
        red_points INT,
        years_left INT,
        active BOOLEAN DEFAULT TRUE,
        FOREIGN KEY (player_id) REFERENCES user(player_id)
    )
'''


cur.execute(f1)



cur.execute(''' create table if not exists admins(
ad_id int primary key,
admin_name char(7),
password varchar(20))
''')

'''
player_1 = (1,'Mathew', 'Lee', '1999-02-13', 'English', 2300, 0,0,2,True)
player_2 = (2, 'Bob', 'Manny', '2000-05-20', 'America', 3000, 1, 2, 4, True)
player_3 = (3, 'Ronnie', 'Shin', '2001-01-12', 'Portugal', 3200, 0,1,1,True)
player_4 = (4, 'John', 'Doe', '1995-03-08', 'USA', 3000, 1, 2, 3, True)
player_5 = (5, 'James', 'Smith', '1997-09-15', 'Canada', 3200, 2, 0, 4, True)
player_6 = (6, 'Robert', 'Johnson', '1998-05-20', 'England', 2800, 1, 1, 2, True)
player_7 = (7, 'William', 'Brown', '1996-11-30', 'Australia', 3300, 0, 2, 3, True)
player_8 = (8, 'Charles', 'Taylor', '1994-04-05', 'Germany', 2900, 2, 1, 1, True)
player_9 = (9, 'Richard', 'Wilson', '1993-02-18', 'France', 2800, 1, 2, 2, True)
player_10 = (10, 'Joseph', 'Martin', '1992-09-22', 'Italy', 3100, 0, 1, 5, True)

list1 = [
    player_1,
    player_2,
    player_3,
    player_4,
    player_5,
    player_6,
    player_7,
    player_8,
    player_9,
    player_10
]


for i in list1:
  cur.execute(f'insert into football_player values {i}')
  mycon.commit()  
'''








#------------------------------------------------------usernamne password---
        
#admin login



                            


p1 = "sweet_987#"          #sweet_987#
newp1 = encrypt(p1)
p2 = "Banana_23"            #Banana_32         
newp2 = encrypt(p2)

'''
q1 = f'insert into admins values(1, "admin01", "{newp1}")'
q2 = f'insert into admins values(2, "admin02", "{newp2}")'
cur.execute(q1)
cur.execute(q2)
mycon.commit()
'''




#----------------------------------------others
'''
def greet():
    current_time = datetime.datetime.now().time()
    hour = current_time.hour

    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
greeting = greet()
'''

def create_acc():
    cur.execute('select max(player_id) from user')
    k = cur.fetchone()[0]
    fname = input('enter first name :\t')
    lname = input('enter last name:\t')
    passw = input('enter a secure password:\t')
    
    t2 = (k+1, encrypt(passw), fname, lname, True, 'None', 'None')

    
    dob = input('enter DOB:\t')
    nation = input('enter nationality \t')
   
    try:
        sal = int(input('enter salary (0 if you are new member):\t'))
        gp = int(input('enter green points(0 if you are new member):\t'))
        rp = int(input('enter red points (0 if you are new member):\t'))
        years = int(input('enter years left \t'))
    except Exception:
        print('Enter Valid inputs')
    

    t1 = (k+1,fname, lname, dob, nation, sal, gp, rp, years, True)

    try:
        cur.execute(f'insert into user values {t2}')
        cur.execute(f'insert into football_player values {t1}')
        mycon.commit()
        print('Succesfully added account')
        print('\n')
    except Exception:
        print('There was an error try again')
        mycon.rollback()
        print('\n')


def main():
    while True:
        print('        ==================             ')
        print('--------SPORTS CLUB SYSTEM-------------')
        print('        ==================             ')
        print(f'Hello what do you wish to do')
        print('1.User')
        print('2.Admin')
        print('3.exit')
        ch = input('enter choice(enter a number from above):')
        print('\n')
        if ch == '1':
            while True:
                print('Choose from the below')
                print('1.Create account')
                print('2.Login to account')
                print('3.Exit')
                var1 = input('enter choice (enter number):')
                if var1 == '1':
                    create_acc()
                elif var1 == '2':  
                    print('welcome to user')
                    user_login()
                elif var1 == '3':
                    break
                else:
                    print('Please enter a valid choice')
                    print('\n')
        elif ch == '2':
            admin_login()
        elif ch == '3':
            break
        else:
            print('Enter a valid choice')

main()


cur.close()
mycon.close()
