# I would like to store all my co-workers 6 favorite numbers to use as a
# composite company powerball ticket number. First I capture the name of the
# co-worker entering the number. The first 5 favorite numbers will need to be
# in the range of 1 to 69 and unique. The 6th favorite number will need to be
# in the range of 1 to 26 and flagged as the 6th Powerball number. The system
# should keep count of each individual favorite number provided to determine
# which numbers to use in the final number. The system should retrieve the max
# count of each unique duplicate number and use them as the powerball numbers.
# If there is a tie based on the max counts randomly select the tied number.
# The system should display all co-workers with their corresponding number
# entries.  The system should display the final powerball number based on the
# requirements above.

import unittest

from selenium import webdriver


class HiveMindPowerballTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_registration_page_loads_correctly(self):
        # My co-drone Wade Wilson wants in!
        # First he navigates to the start page.
        self.browser.get('http://127.0.0.1:8000')

        # The page title mentions powerball
        self.assertIn('POWERBALL', self.browser.title.upper())
        self.fail('Finish the test!')


# He enters his first name: Wade

# He enters his last name: Wilson

# He selects his first number: 15

# He selects his second number (1 to 69, excluding 15): 26

# He selects his third number (1 to 69, excluding 15, 26): 33

# He selects his fourth number (1 to 69, excluding 15, 26, 33): 60

# He selects his fifth number (1 to 69, excluding 15, 26, 33, 60): 34

# He selects his POWERBALL number: 16

# My co-worker Frank Castle signs up!  First he navigates to the start page.

# He enters his first name: Frank

# He enters his last name: Castle

# He selects his first number: 15

# He selects his second number (excluding 15): 26

# He selects his third number (excluding 15, 26): 34

# He selects his fourth number (excluding 15, 26, 34): 56

# He selects his fifth number (excluding 15, 26, 34, 56): 61

# He selects his POWERBALL number: 16

# The number tally is:
# | ## | Count |
# +----+-------+
# | 15 | 2     |
# | 26 | 2     |
# | 34 | 2     |
# | 33 | 1     |
# | 60 | 1     |
# | 56 | 1     |
# | 61 | 1     |
#
# The Powerball Tally is:
# | ## | Count |
# +----|-------+
# | 16 | 2     |
#
# The composite powerball number is: 15, 26, 34, *, *, POWERBALL: 16

if __name__ == '__main__':
    unittest.main()
