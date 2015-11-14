import unittest

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from .models import site
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your tests here.
#Check create form is loaded /sites/create/ -- create template
class urlTestCreate(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        #get the response for the create template
        
#Test the url patterns for the /sites/ index template
class urlTestIndex(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        #create the test data for the database
        UserName = User.objects.create_user('test.user', 'test.user@test.com', 'testpassword')
        GroupName = Group.objects.create(name = 'groupname')
        site.objects.create(name = 'Site1', manager = UserName, reportGroup = GroupName)

    def test_details(self):
        #get the response for the root of the
        response = self.client.get('/sites/')
        #check the response is 200 - success
        self.assertEqual(response.status_code, 200)
        #check the context has one item
        self.assertEqual(len(response.context['site_list']), 5)

#test the url patterns for /sites/35/ to get details
class urlTestDetails(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        #create the test data start with users and groups
        for number in range(0,4):
            UserName = User.objects.create_user('test.user' + str(number), 'test.user' + str(number) + '@test.com', 'testpassword' + str(number))
            GroupName = Group.objects.create(name = 'groupname' + str(number))
            site.objects.create(name = 'Site' + str(number), manager = UserName, reportGroup = GroupName)

    def test_details(self):
        #send get request that will call the page
        response = self.client.get('/sites/2/')
        #check that the request response is 200 i.e. a valid page
        self.assertEqual(response.status_code, 200)
        #check that the context has three items
        self.assertIsNotNone(response.context['site_details'])
