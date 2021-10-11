import os
import mysql.connector
import time


class User:
    def __init__(self):
        self.name = None
        self.nic_name = None
        self.age = None
        self.login = None
        self.password = None
        self.singl = '1'
        self.user_id = None


        self.registr_or_login()

        # self.create_table()

   #__________________________________________________ main function ________________________________________________
    def registr_or_login(self):
        self.first_message()
        input_select_option = input(">>> ").strip()
        options = ['1', '2']
        while input_select_option not in options:
            self.clear_windov()
            self.first_message()
            print("invalid input !!!")
            input_select_option = input(">>> ").strip()
        if input_select_option == '1':
            self.register()
        else:
            self.log_in()

    def register(self):
        self.clear_windov()
        input_name = input("Ismingizni kiriting: ").strip().capitalize()
        while not input_name.isalpha():
            self.clear_windov()
            print("Invalid input !!!")
            input_name = input("Ismingizni qayta kiriting: ").strip().capitalize()

        input_nic_name = input("Nic_name kiriting: ").strip()
        while not input_nic_name.isalpha() or self.bazadan_tekshirish("nic_name", input_nic_name):
            self.clear_windov()
            if self.bazadan_tekshirish("nic_name",input_nic_name):
                print("Bunday nic name mavjud ")
            else:
                print("invalid input !!! ")
            input_nic_name = input("Nic_name qayta kiriting: ").strip()

        input_age = input("yoshingizni kiriting: ").strip()
        while not input_age.isnumeric():
            self.clear_windov()
            print("invalid input !!!")
            input_age = input("yoshingizni qayta kiriting: ").strip()

        input_login = input("Login kiriting: ").strip()
        while not input_login.isalnum() or self.bazadan_tekshirish("login", input_login):
            self.clear_windov()
            if self.bazadan_tekshirish("login", input_login):
                print("Bunday login mavjud !!! ")
            else:
                print("Invalit input !!!")
            input_login = input("Login qayta kiriting: ").strip()

        input_password = input("Password kiriting: ").strip()
        check_password = input("Passwordni takroran kiriting: ").strip()
        while input_password != check_password or len(input_password) == 0:
            self.clear_windov()
            print("Passwordni qayta kiriting !!!")
            input_password = input("Password kiriting: ").strip()
            check_password = input("Passwordni takroran kiriting: ").strip()

        input_singl = input("Oilalimisiz [y/n]: ").strip()
        select_option = ['y', 'yes', 'n', 'no']
        while not input_singl in select_option:
            self.clear_windov()
            print("invalid input !!! ")
            input_singl = input("[y/n]: ").strip()


        self.name = input_name
        self.nic_name = input_nic_name
        self.age = input_age
        self.login = input_login
        self.password = input_password
        if input_singl == select_option[1:]:
            self.singl = '0'

        self.write_in_database()
        self.user_id = self.id(input_nic_name)
        self.clear_windov()
        print(f"\n\n\n\t\t Janob {self.name} siz muvofaqqiyatli ro'yxatdan o'tdingiz !!! ")
        time.sleep(2)
        self.clear_windov()
        self.registr_or_login()



        print("shoot")



    def log_in(self):
        print(self.user_id)
        input_login = input("login kiriting: ").strip()
        input_password = input("Password kiriting: ").strip()
        while self.bazadan_tekshirish("login", input_login) and self.bazadan_tekshirish("password", input_password):
            print("Login yoki password xato !!! ")



    # ______________________________________________ message function ______________________________________

    @staticmethod
    def first_message():
        print("""
            Tizimga kirish !!!
        
            register    [1]
            login       [2]
            
        """)



    # ______________________________________________ assistant function ____________________________________

    def bazadan_tekshirish(self, data_in_base, data):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="123456789",
            database="user_info"
        )
        mycursor = mydb.cursor()
        mycursor.execute(f"select {data_in_base} from user2 where {data_in_base}='{data}'")
        result = mycursor.fetchall()
        if len(result) == 0:
            return False
        return True


    @staticmethod
    def clear_windov():
        os.system("clear")

    def create_table(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="123456789",
            database="user_info"
        )
        mycursor = mydb.cursor()

        mycursor.execute("create table user2(id int(6) unsigned auto_increment primary key, "
                         "name varchar(30) not null, "
                         "nic_name varchar(30) not null, "
                         "age int(3) not null, "
                         "login varchar(30) not null, "
                         "password varchar(30) not null, "
                         "single varchar(1) not null)")

        mydb.commit()

    def write_in_database(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="123456789",
            database="user_info"
        )

        mycursor = mydb.cursor()
        mycursor.execute(f"insert into user2(name, nic_name, age, login, password, single) values('{self.name}', '{self.nic_name}', '{self.age}', '{self.login}', '{self.password}', '{self.singl}');")
        mydb.commit()

    def id(self, nicname):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="123456789",
            database="user_info"
        )

        mycursor = mydb.cursor()
        mycursor.execute(f"select id from user2 where nic_name='{nicname}'")
        result = mycursor.fetchall()[0][0]
        return result





user = User()




