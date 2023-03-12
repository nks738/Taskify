from django.db import models


class UserInfo(models.Model):
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class SchedulerInfo(models.Model):
    Scheduler_owner = models.CharField(max_length=32)
    Scheduler_name = models.CharField(max_length=32)


class TaskInfo(models.Model):
    Task_owner_user = models.IntegerField(null=True, blank=True)
    Task_owner_scheduler = models.IntegerField(null=True, blank=True)
    Task_name = models.CharField(default="", max_length=32, null=True, blank=True)
    Task_description = models.CharField(default="", max_length=64, null=True, blank=True)
    Task_start_time = models.DateTimeField(null=True, blank=True)
    Task_end_time = models.DateTimeField(null=True, blank=True)


# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30, blank=True, null=True)

