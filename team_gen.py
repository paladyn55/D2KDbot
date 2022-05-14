import csv
def team_create():
    lobby = open("lobby.txt", 'r', encoding='utf-8')
    c = open('statsT.csv', 'r', encoding='utf-8')
    cr = csv.reader(c)
    arr_usrs = []
    for usr in lobby:
        print(usr)
    for row in cr:
        print(row)
    for u in lobby:
        for row in cr:
            print(row[0])
            if row[0] == u:
                arr_usrs.append(row)
    return arr_usrs