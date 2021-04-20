import pytest
from django.test import TestCase
from django.utils import timezone

from tasks.models import Task

today = timezone.now()
# https://devcenter.heroku.com/articles/heroku-redis#upgrading-a-heroku-redis-version
# Create your tests here.
def test_versioning():
    first_check = r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
    second_check = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
    assert True == True


class TestTasks(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Task.objects.create(
            title="ITM304",
            content="Quiz 6 SQL, Database Redesign",
            date_due=timezone.now() - timezone.timedelta(days=1),
            completed=True,
        )
        Task.objects.create(
            title="ITM304",
            content="Week 9 Problem Set",
            date_due=today + timezone.timedelta(days=1),
            completed=True,
        )
        Task.objects.create(
            title="ITM304",
            content="Week 9 Problem Set",
            date_due=today + timezone.timedelta(days=0),
            completed=True,
        )
        cls.tasks = Task.objects.all()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_first_task_title(self):
        assert self.tasks[0].title == "ITM304"

    def test_is_overdue_true(self):
        assert self.tasks[0].is_overdue == True

    def test_is_overdue_false(self):
        assert self.tasks[1].is_overdue == False

    def test_is_due_true(self):
        assert self.tasks[2].is_due == True

    def test_is_due_false(self):
        assert self.tasks[0].is_due == False


# title="Make dinner",group="Scuba Divers",task="Web project",created_by="shacker",date_created="",date_due="2019-06-14",completed=False,note="Please check with mgmt first",priority=3
# title="Bake bread",group="Scuba Divers",task="Example List",created_by="mr_random",date_created="2012-03-14",date_due="",completed=True
# title="Bring dessert",group="Scuba Divers",task="Web project",created_by="user1",date_created="2015-06-248",date_due="",assigned_to="user1",note="Every generation throws a hero up the pop charts",priority=77
# [
# {"task":"HTML I","done":true},
# {"task":"CSS","done":true},
# {"task":"Responsive design","done":true},
# {"task":"Git","done":true},
# {"task":"JavaScript I","done":true},
# {"task":"JavaScript II","done":false}
# ]
