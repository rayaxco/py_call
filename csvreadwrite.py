import csv

def read_csv_file():
    with open('c:/users/ravyp/PycharmProjects/py_call/ann-ent.csv',mode='r',encoding='utf-8') as file:
        x=csv.reader(file,delimiter=';')
        for i in x:
            print(i)
        # write=csv.writer(file,delimiter=';')
        # row='this is a me mario'
        # write.writerow(row)
read_csv_file()

def write_to_csv():
    with open('ann-ent.csv','w') as fl:
        x=csv.writer(fl)
        row=['2014','level 5','xx22','food','per','h55','return','fin',44,'fsad asdf asdf asdf ']
        x.writerow(row)
write_to_csv()