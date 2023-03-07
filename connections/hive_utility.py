from pyhive import hive


""" Library for  connecting to hive and perform query """

def hiveconnection(host_name, port, user,password, database):
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth='CUSTOM')
    return conn


def hive_selectallfromtable(conn, tablename):
    cur = conn.cursor()
    cur.execute('select * from '+tablename)
    result = cur.fetchall()

    return result