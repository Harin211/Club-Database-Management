# user


import mysql.connector as ms
from prettytable import PrettyTable
from prettytable import from_db_cursor as p
from admin import encrypt

mycon = ms.connect(host = 'localhost', user = 'root', passwd = 'sql password')



cur = mycon.cursor()


cur.execute('create database if not exists club')

cur.execute('use club')





physios = [[1,'Denis',300],
         [2,'Kimberly',350],
         [3,'Jordan',450],
           [4,'None',0]]


def physio_table():
    table = PrettyTable()
    table.field_names = ['Sl.no','Physio Name', 'Charge per week']
    for i in physios :
        table.add_row(i)
    print(table)
    print('\n')


private = [[1,'Lucy',340],
           [2,'Nathan', 300],
           [3,'keele',350],
           [4,'None', 0]]


def private_table():
    table = PrettyTable()
    table.field_names = ['Sl.no','Private session incharge', 'Charge per week']
    for i in private :
        table.add_row(i)
    print(table)
    print('\n')

'''
l1 = [(1, encrypt('Hello'), 'Mathew', 'Lee', True, 'Denis', 'Lucy' ),
      (2,encrypt('2008'),'Bob', 'Manny', False, 'Kimberly', 'Lucy' ),
      (3,encrypt('March'),'Ronnie', 'Shin', True, 'Kimberly', 'Nathan'),
      (4,encrypt('Choco'),'John', 'Doe', True, 'Mathew', 'Lucy' ),
      (5,encrypt('James_234'),'James', 'Smith', True, 'Jordan', 'Keele' ),
      (6, encrypt('1234'), 'Robert', 'Johnson', False, 'Jordan', 'Lucy' ),
       (7, encrypt('5678'), 'William', 'Brown', True, 'Kimberly', 'Nathan' ),
       (8, encrypt('apple'), 'Charles', 'Taylor', True, 'Jorsan', 'Keele' ),
        (9, encrypt('banana'), 'Richard', 'Wilson', False, 'Denis', 'Lucy' ),
       (10, encrypt('1984'), 'Joseph', 'Martin', True, 'Kimberly', 'Nathan' ),
       (11, encrypt('Hello'), 'Mathew', 'Leey', True, 'Denis', 'Lucy' ),
    ]

for i in l1:
    cur.execute(f'insert into user values {i}')
    mycon.commit()
'''

def view(id):
    print('\n')
    try:
        query = f'''
            SELECT 
                user.player_id, user.fname, user.lname, user.available, user.physio, user.private_sess,
                football_player.salary, football_player.green_points, football_player.red_points, football_player.years_left
            FROM 
                user
            JOIN 
                football_player ON user.player_id = football_player.player_id
            where user.player_id = {id}
        '''

        cur.execute(query)
        table = p(cur)
        print(table)
        print('\n')
    except Exception:
        print('There was an error,enter valid ID')

def change_up(name, password,id):
    print('\n')
    oldp = input(f'Hello {name} enter your current password:')
    if encrypt(oldp) == password:
        newp = input('enter your new password:')
        try:
            cur.execute(f'update user set password = "{encrypt(newp)}" where player_id = {id}')
            mycon.commit()
            print('Password successfully changed')
        except Exception:
            print('Ran into an error try again')
            mycon.rollback()
    else:
        print('Incorrect password try again')
        
    print('\n')


def physio(id):
    print('\n')
    print('AVAILABLE PHYSIOTHERAPISTS')
    physio_table()
    try:
        pid = int(input('Enter a physio specialist id from the above:'))
        new_physio = physios[pid-1][1]

        cur.execute(f'update user set physio= "{new_physio}" where player_id = {id}')
        mycon.commit()
        print('Chnages have been saved')
    except Exception:
        print('Ran into error try again')
        mycon.rollback()
    print('\n')
    
def pcoach(id):
    print('\n')
    print('AVAILABLE COACHES FOR PRIVATE SESSIONS')
    private_table()
    try:
        pid = int(input('Enter a Private coach id from the above:'))
        new_coach = private[pid-1][1]
        cur.execute(f'update user set private_sess= "{new_coach}" where player_id = {id}')
        mycon.commit()
        print('Changes have been saved')
    except Exception:
        print('Ran into an error try again')
        mycon.rollback()
    print('\n')





def user(name, password,id):
    while True:
        print(f'Hello {name} what would you like to do')
        print('1.View my details')
        print('2.Change my password')
        print('3.Select Physio')
        print('4.Select Private Coach')
        print('5.Exit')
        try:
            ch = int(input('enter choice:'))
            if ch == 1:
                print('\n')
                print('PLAYER DETAILS:')
                view(id)
            elif ch == 2:
                print('\n')
                change_up(name, password,id)
            elif ch == 3:
                print('\n')
                physio(id)
            elif ch == 4:
                pcoach(id)
                print('\n')
            elif ch == 5:
                print('\n')
                break
            else:
                print('Enter a valid choice')
        except Exception:
            print('Enter valid choice')
def user_login():
    try:
        id = int(input('enter player_id to login:'))
        print('\n')
        print('\n')
        cur.execute(f'select fname, password from user where player_id = {id}')
        k = cur.fetchone()
        pword = input(f'Hello {k[0]} please enter your password:')
        if encrypt(pword) == k[1]:
            print('Login succesful')
            print('\n')
            user(k[0],k[1],id)
        else:
            print('Invalid Password try again')
            print('\n')
    except Exception:
        print('Please enter a valid ID')


# starc pword-fish
#cur.execute('delete from user where player_id = 11')
# timothy - 2341

# daneil pwrod - Soccer123
        
