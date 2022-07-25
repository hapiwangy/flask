import sqlite3
# 讀出資料
con = sqlite3.connect("database/test.db")
cur = con.cursor()
# 新增一行資料(新加一行資料，不一定要有對應數列的欄位，未設定的話欄位預設為None)
# .execute裡面給定的式SQL的指令
cur.execute("INSERT INTO testOWO(id, email) VALUES ('11', 'GGGGG@GMAIL.COM')")
# 最後要記得commit
con.commit()
# 讀資料
querydata = cur.execute('SELECT * FROM testOWO ORDER BY id')
for row in querydata:
    print(row)
con.close()