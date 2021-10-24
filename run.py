#!/usr/bin/env python3.6

from password import User, Credentials

def create_user(user_name,user_password):
    '''
    Function to create a new User.
    '''
    new_user = User(user_name,user_password)
    return new_user