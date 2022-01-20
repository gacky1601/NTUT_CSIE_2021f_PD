import pymysql
def connectDb():
    db_settings = {
    "host": "192.168.56.102",
    "port": 3306,
    "user": "db_dev",
    "password": "1234",
    "db": "company0324",
    "charset": "utf8"
    }
    conn = None
    try:
        conn = pymysql.connect(**db_settings)
    except Exception as ex:
        print(ex)
    finally:
        return conn,db_settings
def checkUser(conn, account,passwd)->bool:
    result=""
    #please write your code here
    return False
def getSalary(conn,first_name,last_name,auth_token)->str:
    salary=''
        #please write your code here
    return str(result[0])

def main():
    #please develop the new step of the salary system
    conn,db= connectDb()
    if(conn is None):
        print('connect db fail')
    else:
        print('connect db success!'+'db: ',db)
main()