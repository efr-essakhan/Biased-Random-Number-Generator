import unittest

from rand_num_selector import RandomNumberSelector


class TestRandomNumberSelector(unittest.TestCase):
    """Testing RandomNumberSelector class in rand_num_selector.py
    """

    def setUp(self):
        """Method used to initilize our test (ran each time)
        """
        pass

    def tearDown(self):
        """Ran each time after the unit tests have been done."""
        pass

    def test_init_input_verification(self):
        """Testing all input verification methods in __input__(), checks
        if all exceptions are called correctly.
        """

        #Exprected result
        exception_exp1 = ValueError
        exception_exp2 = TypeError
        exception_exp3 = TypeError
        exception_exp4 = ValueError
        exception_exp5 = ValueError

        #TODO: try with message
        # Testing
        with self.assertRaises(exception_exp1):
            rand_selector1 = RandomNumberSelector([0,1,2,5], [0.4,0.3,0.1]) #Lists not equal length

        with self.assertRaises(exception_exp2):
            rand_selector2 = RandomNumberSelector([0,'', 2.0], [0.4,0.3,0.1]) #Population list not consisting of int or float

        with self.assertRaises(exception_exp3):
            rand_selector3 = RandomNumberSelector([0,1,2],  [1,0.3,0.1]) # List probabilities containing other than float

        with self.assertRaises(exception_exp4):
            rand_selector4 = RandomNumberSelector([0,1,2],  [-0.1,0.3,0.1]) #Probabilities being 0<=x<1

        with self.assertRaises(exception_exp5):
            rand_selector5 = RandomNumberSelector([0,1,2],  [0.1,0.3,0.1]) #Probabilities not adding to 1

    def test_next_num_change_of_num(self):
        """Tests next_num actually does select a different number eventually"""

        #Setup
        rand_selector = RandomNumberSelector([0,1,2,3],[0.25,0.25,0.25,0.25])

        # Method execution
        inital_selected = rand_selector.next_num() #we want a different selection to this
        number_changed = False #indicates if a new number is selected

        for i in range(20):

            new_selected = rand_selector.next_num()

            if inital_selected != new_selected:
                number_changed = True
                break

        # Test
        self.assertTrue(number_changed)




if __name__ == "__main__":
    unittest.main() #Calls Setup> all tests > tear-down