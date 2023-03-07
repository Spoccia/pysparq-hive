from pyhive import hive


host_name = "127.0.0.1"
port = 10000
user = "scott"
password = "tiger"
database="default"

def hiveconnection(host_name, port, user,password, database):
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('select * from employee')
    result = cur.fetchall()

    return result

# Call above function
output = hiveconnection(host_name, port, user,password, database)
print(output)