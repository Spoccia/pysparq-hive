from pyhive import hive


host_name = "192.168.0.38"
port = 10000
user = "admin"
password = "password"
database="test_db"

def hiveconnection(host_name, port, user,password, database):
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('select item_sk,reason_sk, account_credit from returns limit 5')
    result = cur.fetchall()

    return result

# Call above function
output = hiveconnection(host_name, port, user,password, database)
print(output)