import unittest   #  Importing the unittest module
from password import User, Credentials  #  Importing the user and credentials classes

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
            unittest.TestCase: TestCase class that helps in creating cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Ian', '12345')  #  Create new User object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name, 'Ian')
        self.assertEqual(self.new_user.user_password, '12345')

    def tearDown(self) -> None:
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_user(self):
        '''
        test_save_user  test case to test if the contact object is saved into the user_list
        '''
        self.new_user.save_user()  #  Saving the new user
        self.assertEqual(len(User.user_list), 1)

class TestCredentials(unittest.TestCase):
    '''
    test case that defines test cases for credentials class.
    '''
    def setUp(self) -> None:
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials('Gmail', 'Ian', '12345')

    def tearDown(self) -> None:
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_credential.account, 'Gmail')
        self.assertEqual(self.new_credential.user_name, 'Ian')
        self.assertEqual(self.new_credential.user_password, '12345')

    def test_save_credentials(self):
        '''
        test to check if credentials object can be saved.
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test to check if multiple credentials objects can be saved into the credentials_list.
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials('Twitter', 'Logan', '6789')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        test to check whether a credentials object can be deleted and removed from the 
        credentials_list.
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials('Instagram', 'Maureen', '23456')
        test_credentials.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_display_all_credentials(self):
        '''
        test to check whether all credentials from the credentials_list can be displayed.
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_find_credentials_by_name(self):
        '''
        test to check whether credentials can be located based on the account name
        and display information.
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials('test', 'user', '1234')
        test_credentials.save_credentials()

        found_credentials = Credentials.find_credentials('test')

        self.assertEqual(found_credentials.account, test_credentials.account)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean if  we cannot find the credentials.
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials('user1', 'name', 'password')
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exists('user1')
        self.assertTrue(credentials_exists)


if __name__ == '__main__':
    unittest.main()