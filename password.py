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

    def delete_credentials(self):
        '''
        Method to delete a credentials object from the credentials_list.
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        Method that returns a credentials_list.
        '''
        return cls.credentials_list

    @classmethod
    def find_credentials(cls,name):
        '''
        Method to find a credentials object by name.
        '''
        for credential in cls.credentials_list:
            if credential.account == name:
                return credential

    @classmethod
    def credentials_exists(cls,name):
        '''
        Method to check whether a credential exists in the credentials_list.
        '''
        for credential in cls.credentials_list:
            if credential.account == name:
                return True

