import os
import mysql.connector


class User:
    def __init__(self):
        self.name = None
        self.nic_name = None
        self.age = None
        self.login = None
        self.password = None
        self.singl = True

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
            print("log in")

    def register(self):
        self.clear_windov()
        input_name = input("Ismingizni kiriting: ").strip().capitalize()
        while not input_name.isalpha():
            self.clear_windov()
            print("Invalid input !!!")
            input_name = input("Ismingizni kiriting: ").strip().capitalize()

        input_nic_name = input("Nic_name kiriting: ").strip()
        while not input_nic_name.isalpha():

        print("good")












    def log_in(self):
        pass



    # ______________________________________________ message function ______________________________________

    @staticmethod
    def first_message():
        print("""
            register    [1]
            login       [2]
            
        """)



    # ______________________________________________ assistant function _____________________________

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








user = User()




