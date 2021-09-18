"""Unit test for RandomNumberSelector class"""

import unittest

from rand_num_selector import RandomNumberSelector


class TestRandomNumberSelector(unittest.TestCase):
    """
    Testing RandomNumberSelector class in rand_num_selector.py
    """
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

        # Testing
        with self.assertRaises(exception_exp1) as error:
            rand_selector1 = RandomNumberSelector([0,1,2,5], [0.33,0.33,0.34]) #Lists not equal length

        self.assertEqual( #Testing thrown message
            "Both list probabilities & population should have the same number of elements",
            str(error.exception)
        )

        with self.assertRaises(exception_exp2) as error:
            rand_selector2 = RandomNumberSelector([0,'', 2.0], [0.4,0.3,0.1]) #Population list not consisting of int or float
        self.assertEqual( #Testing thrown message
            "List population can only contain elements of type int or float.",
            str(error.exception)
        )

        with self.assertRaises(exception_exp3) as error:
            rand_selector3 = RandomNumberSelector([0,1,2],  [1,0.3,0.1]) # List probabilities containing other than float
        self.assertEqual( #Testing thrown message
            "List probabilities can only contain elements of type float.",
            str(error.exception)
        )

        with self.assertRaises(exception_exp4) as error:
            rand_selector4 = RandomNumberSelector([0,1,2],  [-0.1,0.3,0.1]) #Probabilities being 0<=x<1
        self.assertEqual( #Testing thrown message
            "List probabilities can only contain elements X that are: 0 <= X < 1.",
            str(error.exception)
        )

        with self.assertRaises(exception_exp5) as error:
            rand_selector5 = RandomNumberSelector([0,1,2],  [0.1,0.3,0.1]) #Probabilities not adding to 1
        self.assertEqual( #Testing thrown message
            "List probabilities' elements must sum up to 1.00 (to 2dp).",
            str(error.exception)
        )

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

    def test_next_num_tracker_k_verification(self):
        """
        Testing k parameter verification in next_num_tracker(), checks
        if all exceptions are called correctly.
        """
        #Expected result
        exception_exp1 = TypeError
        exception_exp2 = ValueError

        #Setup
        rand_selector = RandomNumberSelector([0,1,2], [0.33,0.33,0.34])

        # Testing
        with self.assertRaises(exception_exp1) as error:
            rand_selector.next_num_tracker(k='lll') #k not an int
        self.assertEqual( #Testing thrown message
            "k should be of type int",
            str(error.exception)
        )

        with self.assertRaises(exception_exp2) as error:
            rand_selector.next_num_tracker(k=-1) #k<1
        self.assertEqual( #Testing thrown message
            "k should be atleast >= 1",
            str(error.exception)
        )

    def test_next_num_tracker_probability_weights(self):
        """
        Tests if next_num_tracker select different numbers whilst taking probability bias in account.
        """

        #Exprected result
        estimates = [1000,2000,3000,4000] #expect the selections by next_num (list_tot_selections) to not be +/-10% outside these estimates

        #Setup
        rand_selector = RandomNumberSelector([1,2,3,4], [0.1, 0.2, 0.3, 0.4])
        test_fail = True


        #Test execution
        tot_selections = rand_selector.next_num_tracker(10000)
        for estimate in [1000,2000,3000,4000]:

            for tot_selection in tot_selections:

                diff = abs(tot_selection-estimate) # abs -> always positive

                perc_diff = diff/estimate

                if 0 <= perc_diff <= 0.10 == False:
                    #Since the difference is > 10%, the selection rate is not right by next_num()
                    test_fail = True


        self.assertTrue(test_fail)


        pass

if __name__ == "__main__":
    unittest.main() #Calls Setup> all tests > tear-down