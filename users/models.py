from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models import (
  CharField,
   OneToOneField, BooleanField, Model, PositiveSmallIntegerField,
   ManyToManyField,DateField,
   IntegerChoices,  
   SET_NULL, ImageField,DateTimeField,
)
from django.utils.translation import gettext_lazy as _
def user_directory_path(instance, filename):
    return f"user_{instance.user.id}/profile_pics/{filename}"
class Role(Model):
    class UserType(IntegerChoices):
        REGULAR  = 0, _("Regular User")
        STUDENT = 1 , _("Student")
        TEACHER = 2, _("Teacher")
        SECRETARY = 3, _("Secretary")
        SUPERVISOR = 4, _("Supervisor")
        ADMIN = 5, _("Administrator")
    user_type = PositiveSmallIntegerField(choices=UserType.choices,default=UserType.REGULAR, primary_key=True)

class User(AbstractUser):
    roles = ManyToManyField(Role)
    middle_name = CharField(max_length=30, blank=True)
    date_of_birth = DateField(null=True, blank=True)

class Profile(Model):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    user = OneToOneField(get_user_model(), on_delete=SET_NULL, null=True)
    date_created = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)
    is_public = BooleanField(default=False)
    is_active = BooleanField(default=True)
    image = ImageField(default="default.webp", upload_to=user_directory_path)
#  have rust task using celery or golang task to convert image files to webp.
