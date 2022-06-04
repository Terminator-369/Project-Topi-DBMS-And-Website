from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


# Create your models here.

class PtAccount(AbstractBaseUser, PermissionsMixin):
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_no = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True, unique=True)
    username = models.TextField(blank=True, null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    team = models.CharField(max_length=2, default=00)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'phone_no', 'address', 'team']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Collection(models.Model):
    donor = models.OneToOneField('Donor', models.DO_NOTHING, primary_key=True)
    volunteer = models.ForeignKey('Volunteer', models.DO_NOTHING)
    payment_month = models.IntegerField(blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection'
        unique_together = (('donor', 'volunteer'),)


class Donor(models.Model):
    donor_id = models.TextField(primary_key=True)
    name = models.TextField()
    phone_no = models.IntegerField()
    d_email = models.TextField()
    team_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donor'

    def __str__(self):
        return self.donor_id


class DonorAssignment(models.Model):
    volunteer = models.OneToOneField('Volunteer', models.DO_NOTHING, primary_key=True)
    donor = models.ForeignKey(Donor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'donor_assignment'
        unique_together = (('volunteer', 'donor'),)


class Ec(models.Model):
    ec_id = models.TextField(primary_key=True)
    name = models.TextField()
    ec_email = models.TextField()
    address = models.TextField()
    session = models.DateField()
    linkdin_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'ec'


class Head(models.Model):
    head = models.OneToOneField('Member', models.DO_NOTHING, primary_key=True)
    sub_head = models.ForeignKey('SubHead', models.DO_NOTHING, blank=True, null=True, related_name='head_sub_head')

    class Meta:
        managed = False
        db_table = 'head'


class Member(models.Model):
    m_id = models.TextField(primary_key=True)
    name = models.TextField()
    team = models.ForeignKey('Modules', models.DO_NOTHING)
    address = models.TextField()
    phone_no = models.TextField()
    m_email = models.TextField()
    username = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'member'


class Modules(models.Model):
    module_id = models.IntegerField(primary_key=True)
    manager = models.ForeignKey(Ec, models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'modules'


class Payments(models.Model):
    donor_id = models.TextField(primary_key=True)
    payment_month = models.IntegerField(blank=True, null=True)
    payment_year = models.IntegerField(blank=True, null=True)
    payments = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class SubHead(models.Model):
    sub_head = models.OneToOneField(Member, models.DO_NOTHING, primary_key=True)
    head = models.ForeignKey(Head, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_head'


class Volunteer(models.Model):
    volunteer = models.OneToOneField(Member, models.DO_NOTHING, primary_key=True)
    sub_head = models.ForeignKey(SubHead, models.DO_NOTHING, blank=True, null=True, related_name='vol_subhead')

    class Meta:
        managed = False
        db_table = 'volunteer'
    def __str__(self):
        return self.volunteer.name

class VolunteerAssignment(models.Model):
    sub_head = models.OneToOneField(SubHead, models.DO_NOTHING, primary_key=True)
    volunteer = models.ForeignKey(Volunteer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'volunteer_assignment'
        unique_together = (('sub_head', 'volunteer'),)


