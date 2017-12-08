import unittest
from inspect import getargspec
from build import q04_weightage as student
from greyatomlib.recommendor_system_project.q04_weightage.build import q04_weightage as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        print('setup')
        with open('q04_weightage/tests/user_sol.pkl', 'wb') as f:
            dill.dump(student, f)

        with open('q04_weightage/tests/test_sol.pkl', 'wb') as f:
            dill.dump(original, f)
        with open('q04_weightage/tests/user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('q04_weightage/tests/test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/subreddit-interactions-for-25000-users.zip'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_polynomial(self):
        # Input parameters tests
        args = getargspec(student)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args)))
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")


    def test_return_dataframe(self):
        assert_frame_equal(self.student_return, self.original_return,
                           obj="The return values do not match expected values")

   
