class user:
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

