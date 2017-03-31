from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models import QuerySet
from rolepermissions.roles import assign_role, remove_role


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='test1', password='test', first_name = 'test', last_name = 'test')
        User.objects.create(username='test2', password='test2', first_name='test2', last_name='test2')
        
    def test_user_exists(self):
        user_counts = User.objects.filter(username='test1').count()
        self.assertEqual(user_counts, 1)
        
    def test_delete_user(self):
       user = User.objects.get(username='test2')
       user.delete()
       user_count = User.objects.all().count()
       self.assertEqual(user_count,1)
       
    def test_list_user(self):
        queryset =  User.objects.all()
        self.assertIsInstance(queryset, QuerySet)
        
    def test_assign_role(self):
        user = User.objects.get(username='test1')
        assign_role(user,'admin')
           
    def test_remove_role(self):
        user = User.objects.get(username='test1')
        remove_role(user,'admin')
