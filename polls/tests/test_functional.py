import datetime
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from django.utils import timezone
from selenium import webdriver
from polls.models import Question, Choice


def create_question(question_text, days):
    
    time = timezone.now() + datetime.timedelta(days=days)
    question = Question.objects.create(
        question_text=question_text, pub_date=time)
    return question

class SeleniumTestCase(LiveServerTestCase):

    username = 'polladmin'
    password = '12345'

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='Users\Ing\Downloads\chromedriver')
        super(SeleniumTestCase, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(SeleniumTestCase, self).tearDown()

    def test_find_h1(self):
        self.browser.get(self.live_server_url + '/polls/')
        header = self.browser.find_element_by_tag_name('h1')
        self.assertEqual('Polls Topics', header.text)
    
    def test_find_poll(self):
        test_question = create_question('Test', days=0)
        self.browser.get(self.live_server_url + '/polls/')
        question = self.browser.find_element_by_id(f"q-{test_question.id}")
        self.assertEqual('Test', question.text)
    
    def test_poll_hyperlink(self):
        question = create_question('Test', days=0)
        self.browser.get(self.live_server_url + '/polls/')
        links = self.browser.find_elements_by_tag_name('a')
        links[1].click()
        self.assertEqual(self.browser.current_url,
                         self.live_server_url + '/polls/' + f"{question.id}/")
    
   