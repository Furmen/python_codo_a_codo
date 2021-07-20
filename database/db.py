from flask_mysqldb import MySQL

mysql = MySQL()

def getConnectionDB():
    return mysql

def configDB(app):
    app.secret_key = 'many random bytes'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'crud'
    
    mysql = MySQL(app)
    
    return mysql