import sqlite3
import ipdb

class DataBase:

    class __DataBase:

        conn = None;

        def __init__(self):
            self.conn = sqlite3.connect('./resources/test.db');
            print ("Opened database successfully");
            self.message = "Default message";
            self.conn.execute('''
            CREATE TABLE IF NOT EXISTS 'Users'
            (
                ID INT IDENTITY(1,1) PRIMARY KEY,
                USERNAME TEXT NOT NULL,
                PASSWORD TEXT NOT NULL

            );''')

        def addUser(self, uname, upasswd):
            print("INSERT INTO Users (USERNAME, PASSWORD) VALUES ('"+uname+"','"+upasswd+"');");
            self.conn.execute("INSERT INTO Users (USERNAME, PASSWORD) VALUES ('"+uname+"','"+upasswd+"');");
            self.conn.commit();

        def debug_showAllUsers(self):
            cursor = self.conn.execute("SELECT * FROM Users");
            for col in cursor:
                print(col[0])
                print(col[1])
                print(col[2])
                print("=======")

        def validateUser(self, uname, upasswd):
            cursor = self.__readUser(uname);
            item = cursor.fetchone();
            if(item is None):
                return False;
            else:
                cond1 = item[1] == uname
                cond2 = item[2] == upasswd
                return True if cond1 and cond2 else False

        def __readUser(self, uname):
            return self.conn.execute("SELECT * FROM Users WHERE USERNAME='"+uname+"';")

        def whoAmI(self):
            return self.message;

        def setMessage(self, msg):
            self.message = msg;

    instance = None;

    def __init__(self):
        if(DataBase.instance is None):
            DataBase.instance = DataBase.__DataBase()
        else:
            print("Warning: DataBase is a singleton class !");

    def __getattr__(self, name):
        print("Get DataBase attr : " + name);
        return getattr(DataBase.instance, name)

# d = DataBase();
# d.addUser("Roland","1234");
# print(d.validateUser("Roland","1234"));