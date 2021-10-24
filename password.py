class User:
    '''
    Class that generates a new user instance
    '''
    user_list = []

    def __init__(self, user_name, user_password) -> None:
        '''
        Method that defines the properties of a user
        '''
        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)


class Credentials():
    '''
    Class that generates new credentials instances.
    '''
    credentials_list = []

    def __init__(self, account, user_name, user_password):
        '''
        Method that defines the properties of credentials object.
        '''
        self.account = account
        self.user_name = user_name
        self.user_password = user_password

    def save_credentials(self):
        '''
        Method to save a credentials object to the credentials list.
        '''
        Credentials.credentials_list.append(self)

