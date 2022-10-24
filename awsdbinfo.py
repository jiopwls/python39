import pymysql

url = 'bigdata.ctt0fqp5aqua.ap-northeast-2.rds.amazonaws.com'
userid = 'admin'
passwd = '1q2w3e4r'
dbname = 'BigData'

def openConn():
    conn = pymysql.connect(host=url, user=userid, passwd=passwd, database=dbname,charset='utf8')

    cur = conn.cursor()

    return conn,cur

def closeConn(cur, conn):
    cur.close()
    conn.close()