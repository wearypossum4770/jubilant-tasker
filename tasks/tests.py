from django.test import TestCase
import pytest
from django.utils import timezone
from tasks.models import Task
# https://devcenter.heroku.com/articles/heroku-redis#upgrading-a-heroku-redis-version
# Create your tests here.
class TestTasks(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Task.objects.create(title ="ITM304",content = "Quiz 6 SQL, Database Redesign",date_due=timezone.now() - timezone.timedelta(days=1), completed = True)
        Task.objects.create(title ="ITM304",content = "Week 9 Problem Set # 4: Convert VARCHAR() string date to data type DATE",date_due=timezone.now() + timezone.timedelta(days=1), completed = True)
        Task.objects.create(title ="ITM304",content = "Week 9 Problem Set # 4: Convert VARCHAR() string date to data type DATE",date_due=timezone.now() + timezone.timedelta(days=0), completed = True)
        cls.tasks = Task.objects.all()
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
    def test_first_task_title (self):
        assert self.tasks[0].title == "ITM304"
    def test_is_overdue_true(self):
        assert self.tasks[0].is_overdue == True
    def test_is_overdue_false(self):
        assert self.tasks[1].is_overdue == False
    def test_is_due_true(self):
        assert self.tasks[2].is_due == True
    def test_is_due_false(self):
        assert self.tasks[0].is_due == False


# [
# {"task":"HTML I","done":true},
# {"task":"CSS","done":true},
# {"task":"Responsive design","done":true},
# {"task":"Git","done":true},
# {"task":"JavaScript I","done":true},
# {"task":"JavaScript II","done":false}
# ]