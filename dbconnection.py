
# Building a wrapper for opening a connection in this file

import mysql.connector;
import  sqlhost
def openconnection(**args):
    tablename=args.get('tablename',None);
    databasename=args.get('databasename','yourdefaultdb');
    # adding default database as users
    try:
        if(databasename ):
            cn=mysql.connector.connect(user=sqlhost.username,host=sqlhost.host,password=sqlhost.password,database=databasename,charset='utf8');
        return cn;
    except:
        print("connection error 101");
        return None


