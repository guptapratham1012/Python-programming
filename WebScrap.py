import requests
from bs4 import BeautifulSoup
import pandas
import sqlite3
n=['PAC','SHO','PAS','DRI','DEF','PHY']
f=int(input("Enter your page number: "))
q={1:'x',2:'y',3:'z',4:'0',5:'1',6:'2',7:'3',8:'4',9:'5'}
scrapped_list=[]
dbname=input("Enter the database name:  ")
csv=input("Enter the CSV file name: ")
def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS PLAYERS(NAME TEXT,DETAILS TEXT,PAC INT,SHO INT,PAS INT,DRI INT,DEF INT,PHY INT)")
    print("CREATED TABLE SUCCESSFULLY!!")
    conn.close()
def insert_into_table(dbname,values):
    conn = sqlite3.connect(dbname)
    insert_sql="INSERT INTO PLAYERS(NAME,DETAILS,PAC,SHO,PAS,DRI,DEF,PHY)VALUES(?,?,?,?,?,?,?,?)"
    conn.execute(insert_sql,values)
    conn.commit()
    conn.close()
def get_player_info(dbname):
    conn = sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM PLAYERS")
    table_data=cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()

connect(dbname)
for a in q[f]:
    req=requests.get('https://fifarenderz.com/21/players?f=bHZsPTAmcGFnZT0'+a+'Jm9CeT1yYXRpbmd8REVTQ3xOJmdrUz1O')
    content=req.content
    soup=BeautifulSoup(content,'html.parser')
    all_plays=soup.find_all('a',{'class': 'flex justify-start items-center player-list-item'})
    for play in all_plays:
        play_dict={}
        play_dict["NAME"]=play.find('p',{'class': 'text-xl'}).text
        play_dict["DETAILS"]=play.find('p',{'class':'text-sm flex items-center'}).text     
        az=play.find('div',{'class': 'player-stats'}).text
        s=''
        ct=0
        for c in az:
            if c in '0123456789':
                s+=c
                continue
            if c in ' ':
                play_dict[n[ct]]=s
                ct=ct+1
                s=''
        
        scrapped_list.append(play_dict)
        insert_into_table(dbname,tuple(play_dict.values()))
dataframe=pandas.DataFrame(scrapped_list)
dataframe.to_csv(csv+'.csv')
get_player_info(dbname)
