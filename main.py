import os


class User:
    def __init__(self):
        self.name = None
        self.nic_name = None
        self.age = None
        self.login = None
        self.password = None
        self.singl = True
        self.registr_or_login()

   #__________________________________________________ main function
    def registr_or_login(self):
        self.first_message()
        input_select_option = input(">>> ").strip()
        options = ['1', '2']
        while input_select_option not in options:
            self.clear_windov()
            self.first_message()
            print("invalid input !!!")
            input_select_option = input(">>> ").strip()





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











user = User()




