from uuid import uuid4
from datetime import date
from django.db.models import (
    BooleanField,
    CharField, 
    DateField, 
    DateTimeField, 
    Model, 
    SET_NULL,
    UUIDField,
)

class Task(Model):
    external_id =UUIDField(default=uuid4, primary_key=False)
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
