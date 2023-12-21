import pymysql

def createDB():
    # 데이터베이스에 테이블을 생성
    scriptStr = "CREATE TABLE userTable(id char(4), userName char(15), email char(20), birthYear int)"
    cur.execute(scriptStr)
    conn.commit()

def insertDB():
    while True:
        data1 = input("사용자ID==>")
        if data1 == "":
            break
        data2 = input("사용자이름==>")
        data3 = input("사용자이메일==>")
        data4 = input("사용자출생연도==>")

        insertSql = (
            "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','"
            + data3 + "'," + data4 + ")"
        )
        
        cur.execute(insertSql)
        
    conn.commit()

def readDB():
    cur.execute("SELECT * FROM soloDB.userTable")
    print("사용자ID         사용자이름         이메일    출생연도")
    print("------------------------------------------------------")
    
    while(True):
        row = cur.fetchone()
        if row==None:
            break
        # print(row)
        data1 = row[0]
        data2 = row[1]
        data3 = row[2]
        data4 = row[3]
        print("%5s %15s %20s %d" %(data1, data2, data3, data4))



# Step 1. DB 연결
conn = pymysql.connect(
    host="127.0.0.1", user="root", password="dongw2on", db="soloDB", charset="utf8"
)

# Step 2. 커서 생성
cur = conn.cursor()

# Step 3. 데이터베이스에서 읽어오기
readDB()

# Step 4. 연결 끊기
conn.close()
