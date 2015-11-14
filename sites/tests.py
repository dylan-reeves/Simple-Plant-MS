from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import site

# Create your tests here.
#Test the site model works correctly
class siteTest(TestCase):
    def setUp(self):
        #Create Test Data inside site model
        site.objects.create(name='site1', manager='dylan.reeves', reportGroup='RBT report')
        site.objects.create(name='site2', manager='dylan.reeves', reportGroup='RBT report')
        site.objects.create(name='site3', manager='dylan.reeves', reportGroup='RBT report')

    def test_site_manager(self):
        site1 = site.objects.get(name='site1')
        site2 = site.objects.get(name = 'site2')
        site3 = site.objects.get(name='site3')
        #Assert that the site manager is correct
        self.assertEqual(site1.manager = 'dylan.reeves')
        self.assertEqual(site2.manager = 'dylan.reeves')
        self.assertEqual(site3.manager = 'dylan.reeves')
        #assert that the site manager is incorrect
        self.assertNotEqual(site.manager = 'jim.bob')
        self.assertNotEqual(site.manager = 'smart.fella')
        self.assertNotEqual(site.manager = 'me.clever')

    def test_site_reportGroup(self):
        site1 = site.objects.get(name='site1')
        site2 = site.objects.get(name ='site2')
        site3 = site.objects.get(name='site3')
        #Check the report Group
        self.assertEqual(site1.reportGroup = 'RBT report')
        self.assertEqual(site2.reportGroup = 'RBT report')
        self.assertEqual(site3.ReportGroup = 'RBT report')
        #assert incorrect options
        self.assertNotEqual(site1.reportGroup = 'Hellla')
        self.assertNotEqual(site2.reportGroup = 'kiiiieeellla')
        self.assertNotEqual(site3.reportGroup = 'deeznuts')

    
