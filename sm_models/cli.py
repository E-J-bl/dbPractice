import sqlalchemy as sa
import sqlalchemy.orm as so
import pyinputplus as pyip

from models import User,Post,Comment
from controler import Controller

class CLI:
    def __init__(self):
        self.controller = Controller()
        self.login()

    @staticmethod
    def show_title(title):
        print('\n'+title)
        print('-'*len(title)+'\n')


    def login(self):
        self.show_title('Login')
        users=self.controller.get_user_names()
        menu_items=users+['Create a new account','Exit']

        menu_choice=pyip.inputMenu(menu_items,prompt='Choose an account or create a new account\n',numbered=True)
        if menu_choice=='Create a new account':
            self.creat_account()
        elif menu_choice=='Exit':
            print('Goodbye')
        else:
            user_name=menu_choice
            self.controller.set_current_user(user_name)
            self.user_home()


    def creat_account(self,existing_user=None):
        self.show_title('Create a new account')
        print('Enter account details:')
        user_name=pyip.inputStr(prompt='Enter username:',blockRegexes=existing_user)
        age=pyip.inputInt(prompt='Enter age:',min=0,max=150,blank=True)
        gender=pyip.inputStr(prompt='Enter gender:',blank=True)
        nationality=pyip.inputStr(prompt='Enter nationality:')
        self.controller.create_user(user_name,age,gender,nationality)
        self.login()


