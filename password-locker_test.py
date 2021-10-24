import unittest   #  Importing the unittest module
from password import User  #  Importing the contact class

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


if __name__ == '__main__':
    unittest.main()