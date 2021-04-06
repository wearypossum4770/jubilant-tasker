from datetime import date
from django.db.models import (
    Model, CharField, SET_NULL, BooleanField,DateTimeField, DateField
)

class Task(Model):
    title=CharField(max_length=80)
    content=CharField(max_length=100)
    date_modified = DateTimeField(auto_now=True)
    date_created=DateTimeField(auto_now_add=True)
    date_due=DateField(null=True, blank=True)
    completed =BooleanField(default=False)
    def __str__(self):
        return self.title
    @property
    def is_due(self):
        return date.today() == self.date_due
    @property
    def is_overdue(self):
        return date.today() > self.date_due
