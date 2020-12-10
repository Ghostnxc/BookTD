from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith heard about a cool online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do' , self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #She is inviteded to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'

        )

        #She types "Buy peacock fethers" into a text box (Edith's hobby
        # is trying fly-fishing lures)
        inputbox.send_keys("Buy peacock fethers")

        # When she hits enter, the page updates, and now the page lists
        #"1: Buy peacock fethers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not apper in table"
        )
        #There is still a text box inviting her to add another item. She
        # enters "Use peacock fethers to make a fly" (Edith is very 
        # methodical)
        self.fail('finsih the test')

        #The page updates again, and now shows both items on her list

        #Edith wonders whether he site will remember her list. Then she sees
        # that the site has a generated a unique URL for her -- there is some
        # explantory rexr that effect.

        #She cisits that URL - her to-do list is still there.

        #Satisfied, she foes back to sleep
if __name__=='__main__':
        unittest.main(warnings='ignore')