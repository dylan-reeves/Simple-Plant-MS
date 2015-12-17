import unittest

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse, resolve
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from autofixture import AutoFixture

from .models import department
from sites.models import site
from .views import *
# Create your tests here.


class TestDepartment(TestCase):

    def setUp(self):
        department.objects.all().delete()
        AutoFixture(site, generate_fk=True).create(5)
        AutoFixture(department, generate_fk=True).create(20)

    # Just a general test to check the department model is accessable and has the
    # records added by the setUp
    def test_site_model(self):
        numberOfRecords = department.objects.all().count()
        # Assert that the setup methid successfully created 20 departments
        self.assertEqual(numberOfRecords, 20)

    # Test to check update on model works fine
    def test_site_model_update(self):
        testRecord = department.objects.get(pk=3)
        testRecord.name = 'TestSite'
        testRecord.save()
        self.assertEqual(department.objects.get(pk=3).name, 'TestSite')

    # Test to check that delete on model works fine
    def test_site_model_delete(self):
        testRecord = department.objects.get(pk=5)
        testRecord.delete()
        recordExists = True
        try:
            department.objects.get(pk=5)
        except ObjectDoesNotExist:
            recordExists = False
        self.assertFalse(recordExists)

    # Test Inserts on site model
    def test_site_model_insert(self):
        newDept = department(name='NewDepartment',
                             manager=User.objects.get(pk=6))
        newDept.save()
        newDept.sites.add(site.objects.get(pk=1))
        recordExists = True
        try:
            department.objects.get(name='NewDepartment')
        except ObjectDoesNotExist:
            recordExists = False
        self.assertTrue(recordExists)

    # Test the index view for the departments app
    def test_index_view(self):
        request = HttpRequest()
        response = self.client.get('/departments/')
        self.assertTemplateUsed(response, 'departments/index.html')
        # self.assertEqual(len(response.context['department_details']),20)
