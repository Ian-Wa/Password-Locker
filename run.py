#!/usr/bin/env python3.6

from password import User, Credentials

def create_user(user_name,user_password):
    '''
    Function to create a new User.
    '''
    new_user = User(user_name,user_password)
    return new_user

def save_user(user):
    '''
    Function to save user.
    '''
    user.save_user()

def display_user():
    '''
    Function to display user.
    '''
    return User.display_user()

def login_user(user_name, user_password):
    '''
    Function to check whether a user exists and then logs in the user.
    '''
    check_user = Credentials.verify_user(user_name, user_password)
    return check_user

def create_new_credentials(account, user_name, user_password):
    '''
    Function that creates new credentials for given user account
    '''
    new_credentials = Credentials(account, user_name, user_password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials.
    '''
    credentials.save_credentials()

def display_account_details():
    '''
    Function to display all saved credentials.
    '''
    return Credentials.display_credentials()

def delete_credentials(credentials):
    '''
    Function to delete credentials from credentials_list.
    '''
    credentials.delete_credentials()

def find_credential(account):
    '''
    Function to find credentials by account name and return credentials belonging to the account.
    '''
    return Credentials.find_credentials(account)

def check_credentials(account):
    '''
    Function that checks if credentials exists within the account and returns a boolean value.
    '''
    return Credentials.credentials_exists(account)

def generate_password():
    '''
    Function to generate random password for user.
    '''
    auto_password = Credentials.generatePassword()
    return auto_password


def main():
    print("Hello welcome to Password-Locker. \n  Please enter one of these short codes :\n CA ----  Create New Account \n LI ----  Login\n")
    short_code = input().lower().strip()

    if short_code == 'ca':
        print('Sign Up')
        print('*' * 40)
        user_name = input("User Name: ")

        while True:
            print(' Enter one of these short codes : \n TP ---  Type own password: \n GP ---  Generate random Password')
            password_choice = input().lower().strip()
            if password_choice == 'tp':
                password = input('Enter Password: ')
                break
            elif password_choice == 'gp':
                password = generate_password()
                break
            else:
                print('Invalid Password try again')
        save_user(create_user(user_name,password))
        print('*' * 80)
        print(f'Hello {user_name}, Your account has been created successfully! Your password is: {password}')
        print('*' * 80)
    elif short_code == 'li':
        print('*' * 50)
        print('Enter Username and Password to login: ')
        print('*' * 50)
        user_name = input('Username: ')
        password = input('Password: ')
        login = login_user(user_name, password)
        if login_user == login:
            print(f'Hello {user_name}, welcome to Password Locker')
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create  new credentials \n DC - Display Credentials \n FC - Find  credentials \n GP - Generate random password \n D - Delete credentials \n EX - Exit  application \n")
        short_code = input().lower().strip()
        if short_code == 'cc':
            print('Create New Credentials')
            print('*' * 20)
            print('Account name: ')
            account = input().lower()
            user_name = input('Account Username: ')
            while True:
                print('TP -- Type password if you already have an account: \n GP -- Generate random Password')
                password_choice = input().lower().strip()
                if password_choice == 'tp':
                    password = input('Enter Password: ')
                    break
                elif password_choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print('Invalid Password try again')
            save_credentials(create_new_credentials(account, user_name,password))
            print('\n')
            print(f'Account Credentials for : {account} - - User Name: {user_name} -- Password: {password} created successfully')
            print('\n')
        elif short_code == 'dc':
            if display_account_details():
                print('List of your accounts: ')
                print('*' * 30)
                print('*' * 30)
                for account in display_account_details():
                    print(f'Account: {account.account} \n User Name: {user_name} \n Password: {password}' )
                    print('-' * 30)
                print('-' * 30)
            else:
                print('You do not have any credentials saved yet')
        elif short_code == 'fc':
            search_name = input('Enter account name you want to search for: ').lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.user_name} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print('Credential does not exist')
                print('\n')
        elif short_code == 'd':
            search_name = input('Enter the account name of the credentials you want to delete: ').lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print('-' * 50)
                search_credential.delete_credentials()
                print('\n')
                print(f'Your stored credentials for : {search_credential.account} successfully deleted!')
                print('\n')
            else:
                print('Credential you want to delete does not exist in your store')
        elif short_code == 'gp':
            password = generate_password()
            print(f'{password} has been generated successfully')
        elif short_code == 'ex':
            print('Thank you for choosing password  store.')
            break
        else:
            print('Wrong entry')
    else:
        print('Enter valid input to continue')
        


if __name__ == '__main__':
    main()
