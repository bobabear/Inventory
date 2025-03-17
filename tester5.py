# Based on testing harness dated 2017-06-02.

# STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
# 
#   python3 <thisfile.py> <your_one_file.py>
# 
# 
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1 and func2, run this command:
# 
#   python3 <thisfile.py> <your_one_file.py> func1 func2
# 
# You really don't need to read the file any further, except that when
# a specific test fails, you'll get a line number - and it's certainly
# worth looking at those areas for details on what's being checked. This would
# all be the indented block of code starting with "class AllTests".


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
# be precise - to test a function named foobar, the test must be named "test_foobar_#"
# where # may be any digits at the end, such as "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS, and all extra credit functions
#   in EXTRA_CREDIT_DEFNS. Do not include any unofficial helper functions. If you want
#   to make helper definitions to use while testing, those can also be added there for
#   clarity.
# 
# - to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
#   python3 <thisfile.py> .                    # current directory
# 
# A work in progress by Mark Snyder, Oct. 2015.
#  Edited by Yutao Zhong, Spring 2016.
#  Edited by Raven Russell, Spring 2017.
#  Edited by Mark Snyder, June 2017.


import unittest
import shutil
import sys
import os
import time


############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
    
REQUIRED_DEFNS = [
                    'update_inventory', 'merge_inventory', 'products_info', 'digits_summation', 'vowel_counts'
                 ]

# for method names in classes that will be tested
SUB_DEFNS = [
                
            ]

# definitions that are used for extra credit
EXTRA_CREDIT_DEFNS = []

# how many points are test cases worth?
weight_required = 1
weight_extra_credit = 0

# don't count extra credit; usually 100% if this is graded entirely by tests.
# it's up to you the instructor to do the math and add this up!
# TODO: auto-calculate this based on all possible tests.
total_points_from_tests = 40

# how many seconds to wait between batch-mode gradings? 
# ideally we could enforce python to wait to open or import
# files when the system is ready but we've got a communication
# gap going on.
DELAY_OF_SHAME = 1


# set it to true when you run batch mode... 
CURRENTLY_GRADING = False



# what temporary file name should be used for the student?
# This can't be changed without hardcoding imports below, sorry.
# That's kind of the whole gimmick here that lets us import from
# the command-line argument without having to qualify the names.
RENAMED_FILE = "student"




# END SPECIALIZATION SECTION
############################################################################
############################################################################


# enter batch mode by giving a directory to work on as the only argument.
BATCH_MODE = len(sys.argv)==2 and (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):

    ############################################################################

    '''update_invetory tests -- x1 pts each'''

    def test_update_inventory_1(self):

        inventory = {
        'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']], 
        'Milk': [['dairy','sugar-free', 1.0], [2500, '11A']],
        'Bread': [['bakery','organic','whole wheat',0.5], [ 120, '21C']], 
        'Ice cream':[['dairy', 0.75],[3120, '9D']], 
        'salmon': [['frozen foods', 'wild cut', 3.0], [456, '6E']]}

        restock = [['Apple',['sweet'], [100,'']], ['Bread',['gluten-free'], [520, '21D']], ['Chicken', ['butchery', 'farm-raised', 4.5], [974, '50A']]]

        self.assertEqual(update_inventory(inventory, restock), 
        {'Apple': [['fruits', 'non-GMO', 'sweet', 5.0],[1640, '37B']],
        'Milk': [['dairy', 'sugar-free', 1.0], [2500, '11A']],
        'Bread': [['bakery', 'organic', 'whole wheat', 'gluten-free', 0.5],[640, '21C 21D']],
        'Ice cream': [['dairy', 0.75], [3120, '9D']],
        'salmon': [['frozen foods', 'wild cut', 3.0], [456, '6E']],
        'Chicken': [['butchery', 'farm-raised', 4.5], [974, '50A']]})

    def test_update_inventory_2(self):

        inventory = {
        'Mango': [['fruits', 'organic', 0.55], [410, '38C']], 
        'Bread': [['bakery','gluten-free', 2.5], [ 130, '21C']], 
        'Ice cream':[['dairy', 'non-GMO', 0.25],[215, '9E']]} 

        self.assertEqual(update_inventory(inventory), 
        {'Mango': [['fruits', 'organic', 0.55], [410, '38C']], 
        'Bread': [['bakery','gluten-free', 2.5], [ 130, '21C']], 
        'Ice cream':[['dairy', 'non-GMO', 0.25],[215, '9E']]})

    def test_update_inventory_3(self):
        
        inventory = {
        'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']], 
        'Milk': [['dairy','sugar-free', 1.0], [2500, '11A']],
        'Bread': [['bakery','organic','whole wheat',0.5], [ 120, '21C']], 
        'Ice cream':[['dairy', 0.75],[3120, '9D']], 
        'salmon': [['frozen foods', 'wild cut', 3.0], [456, '6E']]}
        
        restock = [['Potato',['sweet', 9.0], [230,'26D']], ['Shrimp', ['farm-raised', 'large', 3.0], [75, '51A']], ['Ice cream',['dairy', 'choclate', 0.25],[215, '9E']]]
        
        self.assertEqual(update_inventory(inventory), 
        {'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']], 
        'Milk': [['dairy','sugar-free', 1.0], [2500, '11A']],
        'Bread': [['bakery','organic','whole wheat',0.5], [ 120, '21C']], 
        'Ice cream':[['dairy', 0.75],[3120, '9D']], 
        'salmon': [['frozen foods', 'wild cut', 3.0], [456, '6E']]})

    def test_update_inventory_4(self):

        restock = [['Potato',['sweet', 9.0], [230,'26D']], ['Shrimp', ['farm-raised', 'large', 3.0], [75, '51A']], ['Ice cream',['dairy', 'choclate', 0.25],[215, '9E']]]
        
        self.assertEqual(update_inventory({}, restock), 
        {'Potato':[['sweet', 9.0], [230,'26D']], 
        'Shrimp': [['farm-raised', 'large', 3.0], [75, '51A']], 
        'Ice cream':[['dairy', 'choclate', 0.25],[215, '9E']]})

    def test_update_inventory_5(self):

        inventory ={
        'Potato':[['sweet', 9.0], [230,'26D']], 
        'Bread': [['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
        'Shrimp': [['farm-raised', 'large', 3.0], [75, '51A']], 
        'Ice cream':[['dairy', 'choclate', 0.25],[215, '9E']],
        'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']]
        }

        restock = []
        
        self.assertEqual(update_inventory(inventory, restock), 
        {
        'Potato':[['sweet', 9.0], [230,'26D']], 
        'Bread': [['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
        'Shrimp': [['farm-raised', 'large', 3.0], [75, '51A']], 
        'Ice cream':[['dairy', 'choclate', 0.25],[215, '9E']],
        'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']]})
    
    def test_update_inventory_6(self):

        inventory ={
        'Potato':[['sweet', 9.0], [230,'26D']], 
        'Bread': [['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
        'Shrimp': [['frozen foods', 'large', 3.0], [75, '51A']], 
        'Ice cream':[['dairy', 'choclate', 0.25],[215, '9E']],
        'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']]
        }

        restock = [['Shrimp', ['farm-raised'], [80, '50A 50B']], ['Bread', [''], [135, '']]]

        self.assertEqual(update_inventory(inventory, restock), 
        {
        'Potato':[['sweet', 9.0], [230,'26D']], 
        'Bread': [['bakery','organic','whole wheat',0.5], [ 935, '21C']], 
        'Shrimp': [['frozen foods', 'large','farm-raised', 3.0], [155, '51A 50A 50B']], 
        'Ice cream':[['dairy', 'choclate', 0.25],[215, '9E']],
        'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']]})

    def test_update_inventory_6(self):

        inventory ={
        'Potato':[['sweet', 9.0], [230,'26D']], 
        'Bread': [['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
        'Shrimp': [['frozen foods', 'large', 3.0], [75, '51A']], 
        'Ice cream':[['dairy', 'choclate', 0.25],[215, '9E']],
        'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']]
        }

        restock = [['Shrimp', ['farm-raised'], [80, '50A 50B']], ['Bread', [''], [135, '']]]

        self.assertEqual(update_inventory(inventory, restock), 
        {
        'Potato':[['sweet', 9.0], [230,'26D']], 
        'Bread': [['bakery','organic','whole wheat',0.5], [ 935, '21C']], 
        'Shrimp': [['frozen foods', 'large','farm-raised', 3.0], [155, '51A 50A 50B']], 
        'Ice cream':[['dairy', 'choclate', 0.25],[215, '9E']],
        'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']]})

    def test_update_inventory_7(self):

        inventory = {
        'Mango': [['fruits', 'organic', 0.55], [410, '38C']], 
        'Bread': [['bakery','gluten-free', 2.5], [ 130, '21C']], 
        'Ice cream':[['dairy', 'non-GMO', 0.25],[215, '9E']]}
        
        restock = [['Bread', [''], [135, '39A']]]

        self.assertEqual(update_inventory(inventory, restock),
        {
        'Mango': [['fruits', 'organic', 0.55], [410, '38C']], 
        'Bread': [['bakery','gluten-free', 2.5], [ 265, '21C 39A']], 
        'Ice cream':[['dairy', 'non-GMO', 0.25],[215, '9E']]})

    def test_update_inventory_8(self):

        self.assertEqual(update_inventory({}), {})

    ###########################################################################

    '''update_progress tests -- x1 pts each'''

    def test_merge_inventory_1(self):

        inventory = (['Apple', ['fruits', 'non-GMO', 5.0], [1540, '37B']], ['Milk', ['dairy','sugar-free', 1.0], [2500, '11A']], ['Bread', ['bakery','organic','whole wheat',0.5], [ 120, '21C']], ['Ice cream', ['dairy', 0.75], [3120, '9D']], ['salmon', ['frozen foods', 'wild cut', 3.0], [456, '6E']])

        new_inventory = {'Apple':[['sweet'], [100,'']], 'Bread': [['gluten-free'], [520, '21D']], 'Chicken': [['butchery', 'farm-raised', 4.5], [974, '50A']]}

        self.assertEqual(merge_inventory(inventory, new_inventory),
        {
        'Apple': [['fruits', 'non-GMO', 'sweet', 5.0], [1640, '37B']],
        'Milk': [['dairy', 'sugar-free', 1.0], [2500, '11A']],
        'Bread': [['bakery', 'organic', 'whole wheat', 'gluten-free', 0.5],[640, '21C 21D']],
        'Ice cream': [['dairy', 0.75], [3120, '9D']],
        'salmon': [['frozen foods', 'wild cut', 3.0], [456, '6E']],
        'Chicken': [['butchery', 'farm-raised', 4.5], [974, '50A']]})

    def test_merge_inventory_2(self):

        inventory =(['Potato',['sweet', 9.0], [230,'26D']], 
                ['Bread', ['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
                ['Shrimp', ['frozen foods', 'large', 3.0], [75, '51A']], 
                ['Ice cream',['dairy', 'choclate', 0.25],[215, '9E']],
                ['Apple', ['fruits', 'non-GMO', 5.0], [1540, '37B']])

        new_inventory = {'Apple':[['sweet'], [100,'']], 'Bread': [['gluten-free'], [520, '21D']], 'Chicken': [['butchery', 'farm-raised', 4.5], [974, '50A']]}

        self.assertEqual(merge_inventory(inventory),
        {
        'Potato':[['sweet', 9.0], [230,'26D']], 
        'Bread': [['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
        'Shrimp': [['frozen foods', 'large', 3.0], [75, '51A']], 
        'Ice cream':[['dairy', 'choclate', 0.25],[215, '9E']],
        'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']]})

    def test_merge_inventory_3(self):
        inventory =()
        new_inventory = {'Shrimp': [['farm-raised', 'small', 2.5], [180, '50A 50B']], 'Bread':[[''], [135, '']],'Mango': [['fruits', 'organic', 0.55], [410, '38C']]}
        
        self.assertEqual(merge_inventory(inventory, new_inventory),
            {'Shrimp': [['farm-raised', 'small', 2.5], [180, '50A 50B']], 
            'Bread': [[''], [135, '']],
            'Mango': [['fruits', 'organic', 0.55], [410, '38C']]})

    def test_merge_inventory_4(self):
        inventory =()
        new_inventory = {'Shrimp': [['farm-raised', 'small', 2.5], [180, '50A 50B']], 'Bread':[[''], [135, '']],'Mango': [['fruits', 'organic', 0.55], [410, '38C']]}
        
        self.assertEqual(merge_inventory(inventory),{})

    def test_merge_inventory_5(self):
        inventory =()
        new_inventory = {}

        self.assertEqual(merge_inventory(inventory, new_inventory),{})
    
    def test_merge_inventory_6(self):
        inventory =(
        ['Potato',['sweet', 9.0], [230,'26D']], 
        ['Bread', ['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
        ['Shrimp', ['frozen foods', 'large', 3.0], [75, '51A']], 
        ['Ice cream',['dairy', 'choclate', 0.25],[215, '9E']],
        ['Apple', ['fruits', 'non-GMO', 5.0], [1540, '37B']])
        
        new_inventory = {'Potato':[['a', 'e'], [120,'E F']],
        'Ice cream':[['d', 'v', 'c', 0.35],[45, 'P']]
        }

        self.assertEqual(merge_inventory(inventory, new_inventory),
            {'Potato': [['sweet', 'a', 'e', 9.0], [350, '26D E F']],
            'Bread': [['bakery', 'organic', 'whole wheat', 0.5], [800, '21C']],
            'Shrimp': [['frozen foods', 'large', 3.0], [75, '51A']],
            'Ice cream': [['dairy', 'choclate', 'd', 'v', 'c', 0.35, 0.25],[260, '9E P']],
            'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']]})

    def test_merge_inventory_7(self):
        inventory =(['Bread', [''], [135, '']],)
        new_inventory = {'Bread': [[''], [90, '']]}

        self.assertEqual(merge_inventory(inventory, new_inventory),{'Bread': [[''], [225, '']]})

    def test_merge_inventory_8(self):
        inventory = (['Potato',['a', 'e', 'r', 9.0], [250,'E F C']],
        ['Ice cream',['d','o', 'v', 'c', 0.35],[45, 'P']],
        ['Bread', ['b', 's', 'w', 0.5], [12, '21C']])
        
        new_inventory = {'Potato':[['a', 'e', 'r'], [250,'E F C']], 
        'Bread':[['w'],[13,'']],
        'Apple': [['t', 'n', 8.0], [120, '37B']]
        }

        self.assertEqual(merge_inventory(inventory, new_inventory),
        {'Potato': [['a', 'e', 'r', 'a', 'e', 'r', 9.0], [500, 'E F C E F C']],
        'Ice cream': [['d', 'o', 'v', 'c', 0.35], [45, 'P']],
        'Bread': [['b', 's', 'w', 'w', 0.5], [25, '21C']],
        'Apple': [['t', 'n', 8.0], [120, '37B']]})

 
	############################################################################

    '''products_info tests -- x1 pts each'''

    def test_products_info_1(self):
        products = ('Apple', 'Milk', 'Bread', 'Salmon')
        products_detail =([['fruits', 'non-GMO', 5.0], [1540, '37B']], [['dairy','sugar-free', 1.0], [2500, '11A']], [['bakery','organic','whole wheat',0.5], [120, '21C']], [['frozen foods', 'wild cut', 3.0], [456, '6E']])
        new_products_detail = ([['sweet'], [100,'']], [], [['gluten-free'], [520, '21D']], [])

        self.assertEqual(products_info(products, products_detail,new_products_detail),
            {'Apple': [['fruits', 'non-GMO', 'sweet', 5.0], [1640, '37B']],
            'Milk': [['dairy', 'sugar-free', 1.0], [2500, '11A']],
            'Bread': [['bakery', 'organic', 'whole wheat', 'gluten-free', 0.5],[640, '21C 21D']],
            'Salmon': [['frozen foods', 'wild cut', 3.0], [456, '6E']]})

    def test_products_info_2(self):
        products = ('Apple', 'Milk', 'Bread', 'Salmon')
        products_detail =([['fruits', 'non-GMO', 5.0], [1540, '37B']], [['dairy','sugar-free', 1.0], [2500, '11A']], [['bakery','organic','whole wheat',0.5], [ 120, '21C']], [['frozen foods', 'wild cut', 3.0], [456, '6E']])
        new_products_detail = ([['sweet'], [100,'']], [], [['gluten-free'], [520, '21D']], [])


        self.assertEqual(products_info(products, products_detail),
            {'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']],
            'Milk': [['dairy', 'sugar-free', 1.0], [2500, '11A']],
            'Bread': [['bakery', 'organic', 'whole wheat', 0.5], [120, '21C']],
            'Salmon': [['frozen foods', 'wild cut', 3], [456, '6E']]})

    def test_products_info_3(self):
        products = ('Apple', 'Milk', 'Bread', 'Salmon')
        products_detail =([['fruits', 'non-GMO', 5.0], [1540, '37B']], [['dairy','sugar-free', 1.0], [2500, '11A']], [['bakery','organic','whole wheat',0.5], [ 120, '21C']], [['frozen foods', 'wild cut', 3.0], [456, '6E']])
        new_products_detail = ([], [], [['gluten-free'], [520, '21D']], [[''],[0,'12D']])

        self.assertEqual(products_info(products, products_detail,new_products_detail),
            {'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']],
            'Milk': [['dairy', 'sugar-free', 1.0], [2500, '11A']],
            'Bread': [['bakery', 'organic', 'whole wheat', 'gluten-free', 0.5],[640, '21C 21D']],
            'Salmon': [['frozen foods', 'wild cut', 3.0], [456, '6E 12D']]})

    def test_products_info_4(self):
        products = ('Apple', 'Milk', 'Bread', 'Salmon')
        products_detail =([['', 5.0], [1, '']], [['dairy', 1.0], [31, '11A']], [['bakery','organic','whole wheat',0.5], [ 120, '21C']], [['frozen foods', 'wild cut', 3.0], [456, '6E']])
        new_products_detail = ([], [[['r', 'non-GMO']],[1,'']], [['c','j', 'k'], [3,'']], [['organic'],[0,'40']])

        self.assertEqual(products_info(products, products_detail,new_products_detail),
            {'Apple': [['', 5.0], [1, '']],
            'Milk': [['dairy', ['r', 'non-GMO'], 1.0], [32, '11A']],
            'Bread': [['bakery', 'organic', 'whole wheat', 'c', 'j', 'k', 0.5],[123, '21C']],
            'Salmon': [['frozen foods', 'wild cut', 'organic', 3.0], [456, '6E 40']]})

    def test_products_info_5(self):
        products = ('Apple',)
        products_detail =([['',90.0],[0,'']],)
        new_products_detail = ([['c','j', 'k'], [33,'15F']],)

        self.assertEqual(products_info(products, products_detail,new_products_detail),
        {'Apple': [['', 'c', 'j', 'k', 90.0], [33, ' 15F']]})

    def test_products_info_6(self):
        products = ('Apple',)
        products_detail =([['',0.0],[0,'']],)
        new_products_detail = ([['c','j', 'k'], [33,'15F']],)

        self.assertEqual(products_info(products, products_detail),{'Apple': [['', 0], [0, '']]})
    
    def test_products_info_7(self):
        products = ('Apple',)
        products_detail =([['',0.0],[0,'']],)
        new_products_detail = ([['c','j', 'k'], [33,'15F']],)

        self.assertEqual(products_info(products, products_detail,new_products_detail), 
            {'Apple': [['', 'c', 'j', 'k', 0.0], [33, ' 15F']]})

    def test_products_info_8(self):
        products = ('Apple',)
        products_detail =([['',0.0],[0,'']],)
        new_products_detail = ([],)

        self.assertEqual(products_info(products, products_detail,new_products_detail), 
            {'Apple': [['', 0.0], [0, '']]})

    ############################################################################

    # '''digits_summation tests -- x1 pts each'''
    
    def test_digits_summation_1(self):
        self.assertEqual(digits_summation(12345), 15)

    def test_digits_summation_2(self):
        self.assertEqual(digits_summation(109637495), 44)

    def test_digits_summation_3(self):
        self.assertEqual(digits_summation(10101), 3)

    def test_digits_summation_4(self):
        self.assertEqual(digits_summation(1234567899876543210), 90)

    def test_digits_summation_5(self):
        self.assertEqual(digits_summation(4), 4)

    def test_digits_summation_6(self):
        self.assertEqual(digits_summation(0), 0)

    def test_digits_summation_7(self):
        self.assertEqual(digits_summation(24), 6)

    def test_digits_summation_8(self):
        self.assertEqual(digits_summation(100000), 1)

    ############################################################################

    # '''vowel_counts tests -- x1 pts each'''

    
    def test_vowel_counts_1(self):
        self.assertDictEqual(vowel_counts("This is a test string!") , {'a': 1, 'e': 1, 'i': 3})

    def test_vowel_counts_2(self):
        self.assertDictEqual(vowel_counts("thjdgfrwmli")  , {'i': 1})

    def test_vowel_counts_3(self):
        self.assertDictEqual(vowel_counts("******")  , {})

    def test_vowel_counts_4(self):
        self.assertDictEqual(vowel_counts("Hello Everyone, welcomE to coursE cs 112")  , {'e': 4, 'o': 5, 'E': 3, 'u': 1})
    
    def test_vowel_counts_5(self):
        self.assertDictEqual(vowel_counts("Fox Jumps Over The Lazy Dog, And Both Animals Enjoy A Peaceful Sunrise.")  , {'o': 4, 'u': 3, 'O': 1, 'e': 5, 'a': 3, 'A': 3, 'i': 2, 'E': 1})
    
    def test_vowel_counts_6(self):
        self.assertDictEqual(vowel_counts("thkrlwqpmncv")  , {})

    def test_vowel_counts_7(self):
        self.assertDictEqual(vowel_counts("iIIeEeEeEuUUUuOOOOOOOAAAAAAAaaaa")  , {'i': 1, 'I': 2, 'e': 3, 'E': 3, 'u': 2, 'U': 3, 'O': 7, 'A': 7, 'a': 4})
    
    def test_vowel_counts_8(self):
        self.assertDictEqual(vowel_counts("Youuuuuuuuuuuuuuu"), {'o': 1, 'u': 15})   

    ############################################################################

# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
    # constructor.
    def __init__(self,wants):
        self.num_req = 0
        self.num_ec = 0
        # find all methods that begin with "test".
        fs = []
        for w in wants:
            for func in AllTests.__dict__:
                # append regular tests
                # drop any digits from the end of str(func).
                dropnum = str(func)
                while dropnum[-1] in "1234567890":
                    dropnum = dropnum[:-1]
                
                if dropnum==("test_"+w+"_") and (not (dropnum==("test_extra_credit_"+w+"_"))):
                    fs.append(AllTests(str(func)))
                if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
                    fs.append(AllTests(str(func)))
        
#       print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
        # call parent class's constructor.
        unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
        # constructor.
        def __init__(self,wants):
            # find all methods that begin with "test_extra_credit_".
            fs = []
            for w in wants:
                for func in AllTests.__dict__:
                    if str(func).startswith("test_extra_credit_"+w):
                        fs.append(AllTests(str(func)))
        
#           print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
            # call parent class's constructor.
            unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
    this_file = __file__
    if dir==".":
        dir = os.getcwd()
    info = os.walk(dir)
    filenames = []
    for (dirpath,dirnames,filez) in info:
#       print(dirpath,dirnames,filez)
        if dirpath==".":
            continue
        for file in filez:
            if file==this_file:
                continue
            filenames.append(os.path.join(dirpath,file))
#       print(dirpath,dirnames,filez,"\n")
    return filenames

def main():
    if len(sys.argv)<2:
        raise Exception("needed student's file name as command-line argument:"\
            +"\n\t\"python3 testerX.py gmason76_2xx_Px.py\"")
    
    if BATCH_MODE:
        print("BATCH MODE.\n")
        run_all()
        return
        
    else:
        want_all = len(sys.argv) <=2
        wants = []
        # remove batch_mode signifiers from want-candidates.
        want_candidates = sys.argv[2:]
        for i in range(len(want_candidates)-1,-1,-1):
            if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
                del want_candidates[i]
    
        # set wants and extra_credits to either be the lists of things they want, or all of them when unspecified.
        wants = []
        extra_credits = []
        if not want_all:
            for w in want_candidates:
                if w in REQUIRED_DEFNS:
                    wants.append(w)
                elif w in SUB_DEFNS:
                    wants.append(w)
                elif w in EXTRA_CREDIT_DEFNS:
                    extra_credits.append(w)
                else:
                    raise Exception("asked to limit testing to unknown function '%s'."%w)
        else:
            wants = REQUIRED_DEFNS + SUB_DEFNS
            extra_credits = EXTRA_CREDIT_DEFNS
        
        # now that we have parsed the function names to test, run this one file.    
        run_one(wants,extra_credits)    
        return
    return # should be unreachable! 

# only used for non-batch mode, since it does the printing.
# it nicely prints less info when no extra credit was attempted.
def run_one(wants, extra_credits):
    
    has_reqs = len(wants)>0
    has_ec   = len(extra_credits)>0
    
    # make sure they exist.
    passed1 = 0
    passed2 = 0
    tried1 = 0
    tried2 = 0
    
    # only run tests if needed.
    if has_reqs:
        print("\nRunning required definitions:")
        (tag, passed1,tried1) = run_file(sys.argv[1],wants,False)
    if has_ec:
        print("\nRunning extra credit definitions:")
        (tag, passed2,tried2) = run_file(sys.argv[1],extra_credits,True)
    
    # print output based on what we ran.
    if has_reqs and not has_ec:
        print("\n%d/%d Required test cases passed (worth %.1f each)" % (passed1,tried1,weight_required) )
        # print("\nScore based on test cases: %.2f/%d (%.2f*%.1f) " % (
#                                                                 passed1*weight_required, 
#                                                                 total_points_from_tests,
#                                                                 passed1,
#                                                                 weight_required
#                                                              ))
    elif has_ec and not has_reqs:
        print("%d/%d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
    else: # has both, we assume.
        print("\n%d / %d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
        print("%d / %d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
        print("\nScore based on test cases: %.2f / %d ( %d * %d + %d * %d) " % (
                                                                passed1*weight_required+passed2*weight_extra_credit, 
                                                                total_points_from_tests,
                                                                passed1,
                                                                weight_required,
                                                                passed2,
                                                                weight_extra_credit
                                                             ))
    if CURRENTLY_GRADING:
        print("( %d %d %d %d )\n%s" % (passed1,tried1,passed2,tried2,tag))

# only used for batch mode.
def run_all():
        filenames = files_list(sys.argv[1])
        #print(filenames)
        
        wants = REQUIRED_DEFNS + SUB_DEFNS
        extra_credits = EXTRA_CREDIT_DEFNS
        
        results = []
        for filename in filenames:
            print(" Batching on : " +filename)
            # I'd like to use subprocess here, but I can't get it to give me the output when there's an error code returned... TODO for sure.
            lines = os.popen("python3 tester1p.py \""+filename+"\"").readlines()
            
            # delay of shame...
            time.sleep(DELAY_OF_SHAME)
            
            name = os.path.basename(lines[-1])
            stuff =lines[-2].split(" ")[1:-1]
            print("STUFF: ",stuff, "LINES: ", lines)
            (passed_req, tried_req, passed_ec, tried_ec) = stuff
            results.append((lines[-1],int(passed_req), int(tried_req), int(passed_ec), int(tried_ec)))
            continue
        
        print("\n\n\nGRAND RESULTS:\n")
        
            
        for (tag_req, passed_req, tried_req, passed_ec, tried_ec) in results:
            name = os.path.basename(tag_req).strip()
            earned   = passed_req*weight_required + passed_ec*weight_extra_credit
            possible = tried_req *weight_required # + tried_ec *weight_extra_credit
            print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
                                                            name,
                                                            earned,
                                                            possible, 
                                                            (earned/possible)*100,
                                                            passed_req,tried_req,weight_required,
                                                            passed_ec,tried_ec,weight_extra_credit
                                                          ))
# only used for batch mode.
def run_all_orig():
        filenames = files_list(sys.argv[1])
        #print(filenames)
        
        wants = REQUIRED_DEFNS + SUB_DEFNS
        extra_credits = EXTRA_CREDIT_DEFNS
        
        results = []
        for filename in filenames:
            # wipe out all definitions between users.
            for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS :
                globals()[fn] = decoy(fn)
                fn = decoy(fn)
            try:
                name = os.path.basename(filename)
                print("\n\n\nRUNNING: "+name)
                (tag_req, passed_req, tried_req) = run_file(filename,wants,False)
                (tag_ec,  passed_ec,  tried_ec ) = run_file(filename,extra_credits,True)
                results.append((tag_req,passed_req,tried_req,tag_ec,passed_ec,tried_ec))
                print(" ###### ", results)
            except SyntaxError as e:
                tag = filename+"_SYNTAX_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except NameError as e:
                tag =filename+"_Name_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except ValueError as e:
                tag = filename+"_VALUE_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except TypeError as e:
                tag = filename+"_TYPE_ERROR"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except ImportError as e:
                tag = filename+"_IMPORT_ERROR_TRY_AGAIN"
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
            except Exception as e:
                tag = filename+str(e.__reduce__()[0])
                results.append((tag,0,len(wants),tag,0,len(extra_credits)))
        
#           try:
#               print("\n |||||||||| scrupe: "+str(scruples))
#           except Exception as e:
#               print("NO SCRUPE.",e)
#           scruples = None
        
        print("\n\n\nGRAND RESULTS:\n")
        for (tag_req, passed_req, tried_req, tag_ec, passed_ec, tried_ec) in results:
            name = os.path.basename(tag_req)
            earned   = passed_req*weight_required + passed_ec*weight_extra_credit
            possible = tried_req *weight_required # + tried_ec *weight_extra_credit
            print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
                                                            name,
                                                            earned,
                                                            possible, 
                                                            (earned/possible)*100,
                                                            passed_req,tried_req,weight_required,
                                                            passed_ec,tried_ec,weight_extra_credit
                                                          ))

def try_copy(filename1, filename2, numTries):
    have_copy = False
    i = 0
    while (not have_copy) and (i < numTries):
        try:
            # move the student's code to a valid file.
            shutil.copy(filename1,filename2)
            
            # wait for file I/O to catch up...
            if(not wait_for_access(filename2, numTries)):
                return False
                
            have_copy = True
        except PermissionError:
            print("Trying to copy "+filename1+", may be locked...")
            i += 1
            time.sleep(1)
        except BaseException as e:
            print("\n\n\n\n\n\ntry-copy saw: "+e)
    
    if(i == numTries):
        return False
    return True

def try_remove(filename, numTries):
    removed = False
    i = 0
    while os.path.exists(filename) and (not removed) and (i < numTries):
        try:
            os.remove(filename)
            removed = True
        except OSError:
            print("Trying to remove "+filename+", may be locked...")
            i += 1
            time.sleep(1)
    if(i == numTries):
        return False
    return True

def wait_for_access(filename, numTries):
    i = 0
    while (not os.path.exists(filename) or not os.access(filename, os.R_OK)) and i < numTries:
        print("Waiting for access to "+filename+", may be locked...")
        time.sleep(1)
        i += 1
    if(i == numTries):
        return False
    return True

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename,wants=None,checking_ec = False):
    if wants==None:
        wants = []
    
    # move the student's code to a valid file.
    if(not try_copy(filename,"student.py", 5)):
        print("Failed to copy " + filename + " to student.py.")
        quit()
        
    # import student's code, and *only* copy over the expected functions
    # for later use.
    import importlib
    count = 0
    while True:
        try:
#           print("\n\n\nbegin attempt:")
            while True:
                try:
                    f = open("student.py","a")
                    f.close()
                    break
                except:
                    pass
#           print ("\n\nSUCCESS!")
                
            import student
            importlib.reload(student)
            break
        except ImportError as e:
            print("import error getting student... trying again. "+os.getcwd(), os.path.exists("student.py"),e)
            time.sleep(0.5)
            while not os.path.exists("student.py"):
                time.sleep(0.5)
            count+=1
            if count>3:
                raise ImportError("too many attempts at importing!")
        except SyntaxError as e:
            print("SyntaxError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+"_SYNTAX_ERROR",None, None, None)
        except NameError as e:
            print("NameError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return((filename+"_Name_ERROR",0,1))    
        except ValueError as e:
            print("ValueError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+"_VALUE_ERROR",0,1)
        except TypeError as e:
            print("TypeError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+"_TYPE_ERROR",0,1)
        except ImportError as e:            
            print("ImportError in "+filename+":\n"+str(e))
            print("Run your file without the tester to see the details or try again")
            return((filename+"_IMPORT_ERROR_TRY_AGAIN   ",0,1)) 
        except Exception as e:
            print("Exception in loading"+filename+":\n"+str(e))
            print("Run your file without the tester to see the details")
            return(filename+str(e.__reduce__()[0]),0,1)
    
    # make a global for each expected definition.
    for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS :
        globals()[fn] = decoy(fn)
        try:
            globals()[fn] = getattr(student,fn)
        except:
            if fn in wants:
                print("\nNO DEFINITION FOR '%s'." % fn) 
    
    if not checking_ec:
        # create an object that can run tests.
        runner = unittest.TextTestRunner()
    
        # define the suite of tests that should be run.
        suite = TheTestSuite(wants)
    
    
        # let the runner run the suite of tests.
        ans = runner.run(suite)
        num_errors   = len(ans.__dict__['errors'])
        num_failures = len(ans.__dict__['failures'])
        num_tests    = ans.__dict__['testsRun']
        num_passed   = num_tests - num_errors - num_failures
        # print(ans)
    
    else:
        # do the same for the extra credit.
        runner = unittest.TextTestRunner()
        suite = TheExtraCreditTestSuite(wants)
        ans = runner.run(suite)
        num_errors   = len(ans.__dict__['errors'])
        num_failures = len(ans.__dict__['failures'])
        num_tests    = ans.__dict__['testsRun']
        num_passed   = num_tests - num_errors - num_failures
        #print(ans)
    
    # remove our temporary file.
    os.remove("student.py")
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
    if(not try_remove("student.py", 5)):
        print("Failed to remove " + filename + " to student.py.")
    
    tag = ".".join(filename.split(".")[:-1])
    
    
    return (tag, num_passed, num_tests)


# make a global for each expected definition.
def decoy(name):
        # this can accept any kind/amount of args, and will print a helpful message.
        def failyfail(*args, **kwargs):
            return ("<no '%s' definition was found - missing, or typo perhaps?>" % name)
        return failyfail

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
    main()
