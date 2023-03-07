from configurations import hive_conf as h_conf
from connections import hive_utility as hive_u

# Call above function
conn = hive_u.hiveconnection(h_conf.host_name, h_conf.port, h_conf.user,h_conf.password, h_conf.database)
output = hive_u.hive_selectallfromtable(conn, 'employee')
print(output)