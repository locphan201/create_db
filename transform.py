import random

queries = ''
col = 0
postion = ['Clerk', 'Sale']
filename = 'Staffs.csv'
table = filename.split('.')[0]
c = "INSERT INTO " + table + " ("
with open(filename, 'r', encoding='UTF-8') as f:
    line = f.readline()
    line = line.split(',')
    col = len(line)-1
    for i in range(len(line)-1):
        c += line[i] + ', '
    c += line[len(line)-1].replace('\n','') + ") VALUES ('"
    line = f.readline()
    while line != '':
        if line.count(',') != col:
            line = f.readline()
            continue
        queries += c
        line = line.split(',')
        #Name
        queries += line[0] + "','"
        #Phone
        phone = line[1].replace('(', '').replace(') ', '').replace('-', '')
        queries += phone + "','"
        #Salary
        queries += line[2] + "','"
        #Email
        queries += line[3] + "','"
        #Position
        queries += random.choice(postion) + "','"
        #Password
        queries += line[5].replace('\n','') + "');\n"
        line = f.readline()
        
with open(table+'.txt', 'w', encoding='UTF-8') as f:
    f.write(queries)
        