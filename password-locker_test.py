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


if __name__ == '__main__':
    unittest.main()