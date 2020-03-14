from django.test import TestCase

from mysite.models import Blog

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['blog_data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        firefox_options = Options()
        firefox_options.headless = True
        binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        firefox_options.binary = binary
        cls.selenium = webdriver.Firefox(firefox_options=firefox_options,
                                         executable_path="geckodriver.exe")

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_find_element(self):
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        test = self.selenium.find_element_by_id('title')


class BlogTestCase(TestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     cls.data = Blog.objects.create(title="Lorem ipsum")

    fixtures = ['blog_data.json']

    def test_home(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'Hello')
        self.assertEqual(response.context['blog'].title, 'Lorem ipsum')