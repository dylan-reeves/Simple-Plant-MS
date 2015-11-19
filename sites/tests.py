import unittest

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse, resolve
from django.http import HttpRequest
from .models import site
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from autofixture import AutoFixture
from django.core.exceptions import ObjectDoesNotExist
from .views import *

# Create your tests here.
#Check create form is loaded /sites/create/ -- create template
# Test the site model
class TestSite(TestCase):
        def setUp(self):
            site.objects.all().delete()
            AutoFixture(site, generate_fk=True).create(20)

        #Just a general test to check the site model is accessable and has the
        #records added by the setUp
        def test_site_model(self):
            numberOfRecords = site.objects.all().count()
            #Assert that the setup methid successfully created 20 sites
            self.assertEqual(numberOfRecords,20)

        #Test to check update on model works fine
        def test_site_model_update(self):
            testRecord = site.objects.get(pk=3)
            testRecord.name = 'TestSite'
            testRecord.save()
            self.assertEqual(site.objects.get(pk=3).name, 'TestSite')

        #Test to check that delete on model works fine
        def test_site_model_delete(self):
            testRecord = site.objects.get(pk=5)
            testRecord.delete()
            recordExists = True
            try:
                site.objects.get(pk=5)
            except ObjectDoesNotExist:
                recordExists = False
            self.assertFalse(recordExists)

        #Test Inserts on site model
        def test_site_model_insert(self):
            site.objects.create(name='NewSite', manager=User.objects.get(pk=6),
                                reportGroup=Group.objects.get(pk=3))
            recordExists = True
            try:
                site.objects.get(name='NewSite')
            except ObjectDoesNotExist:
                recordExists = False
            self.assertTrue(recordExists)

        #Test the index view for the sites app
        def test_index_view(self):
            request = HttpRequest()
            response = self.client.get('/sites/')
            self.assertTemplateUsed(response, 'sites/index.html')
            self.assertEqual(len(response.context['site_details']),20)
