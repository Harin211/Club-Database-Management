#football
import mysql.connector as ms
from prettytable import PrettyTable
from prettytable import from_db_cursor as p



mycon = ms.connect(host = 'localhost', user = 'root', passwd = 'sql password')


cur = mycon.cursor()
cur.execute('create database if not exists club')
cur.execute('use club')


def encrypt(string):
    old = string
    new = ""
    for i in old:
        new += chr(ord(i)+4)
    return new[::-1]







def display_table():
    cur.execute('select * from football_player')
    table = p(cur)
    print(table)

    
def delete():
    try:
        cur.execute('select player_id from football_player')
        ids = cur.fetchall()

        fid = []
        for i in ids:
            fid.append(i[0])
        var1 = int(input('Which record would you like to delete(enter player id):'))
        if var1 in fid:
            cur.execute('SET FOREIGN_KEY_CHECKS=0')
            cur.execute(f'delete from user where player_id = {var1}')
            cur.execute(f'delete from football_player where player_id = {var1}')
            mycon.commit()
            cur.execute('SET FOREIGN_KEY_CHECKS=0')
            print('Succesfully deleted record ')
        else:
            print('ID is inavlid try again')
    except Exception:
        print('There was an error')
        mycon.rollback()
    
    

def total_sal():
    cur.execute('select sum(salary) as total_salary from football_player')
    total = cur.fetchone()[0]
    table = PrettyTable()
    table.field_names = ['Player', 'Salary']
    cur.execute('select fname, salary from football_player')
    var1 = cur.fetchall()
    for i in var1:
        table.add_row(i)
    rec = ('Total salary', total)    
    table.add_row(rec)
    print(table)



def green():
    try:
        display_table()
        l1 = eval(input('enter player id to increase green points (in list):\t'))
        for i in l1:
            cur.execute(f'select Player_id, fname as first_name, green_points from football_player where player_id = {i}')
            table  = p(cur)
            print(table)
            inc = int(input('How much do you want to set green points to?:\t'))
            cur.execute(f'update football_player set green_points = {inc} where player_id = {i}')
            mycon.commit()
            print('Update is successful')
    except Exception:
            print('There was an error')
            mycon.rollback()
        

def red():
    try:
        display_table()
        l1 = eval(input('enter player id to increase red points (in list):\t'))
        for i in l1:
            cur.execute(f'select Player_id, fname as first_name, red_points from football_player where player_id = {i}')
            table  = p(cur)
            print(table)
            inc = int(input('How much do you want to set red points to?:\t'))
            cur.execute(f'update football_player set red_points = {inc} where player_id = {i}')
            mycon.commit()
            print('Update is successful')
    except Exception:
        print('There was an error')
        mycon.rollback()


'''
def graph():
    cur.execute('select player_id, fname, green_points, red_points from football_player')
    playerid = []
    names = []
    gp = []
    rp =[]
    records = cur.fetchall()
    for i in records:
        playerid.append(i[0])
        names.append(i[1])
        gp.append(i[2])
        rp.append(i[3])
    bar_width = 0.35
    index = playerid[:]
    index_r = []
    for i in index:
        index_r.append(bar_width+i)
    plt.bar(index, gp, bar_width, label = 'green points', color ='g')
    plt.bar(index_r, rp, bar_width, label = 'red points', color ='r')
    plt.xlabel('player')
    plt.ylabel('Points')
    plt.title('Red and Green points of each player')

    plt.xticks([i + bar_width / 2 for i in index], names, rotation=45, ha='right')

    plt.legend()
    plt.tight_layout()
    plt.show()
'''

def change_sal():
    try:
        fid = int(input('Enter player_id whose salary needs to be changed:'))
        new_sal = int(input('Enter new salary:'))
        cur.execute(f'update football_player set salary = {new_sal} where player_id = {fid}')
        mycon.commit()
        print('Succesfully changed salary')
        print('\n')
    except Exception:
        print('There was an error, try again')
        mycon.rollback()
        


def football():
    while True:
        print('What would you like to do?\t')
        print('1.Display Table')
        print('2.Delete record')
        print('3.Edit green points ')
        print('4.Edit red points')
        print('5.Display Total salary per week')
        print('6. Change salary of a player')
        print('7.Exit')
        ch = input('enter choice:\t')
        if ch == '1':
            display_table()
        elif ch == '2':
            delete()
            display_table()
        elif ch == '3':
            green()
            display_table()
        elif ch == '4':
            red()
            display_table()
        elif ch == '5':
            total_sal()
        elif ch == '6':
            change_sal()
        elif ch == '7':
            break
        else:
            print('Enter a valid choice')



