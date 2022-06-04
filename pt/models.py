# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Collection(models.Model):
    donor = models.OneToOneField('Donor', models.DO_NOTHING, primary_key=True)
    volunteer = models.ForeignKey('Volunteer', models.DO_NOTHING)
    payment_month = models.IntegerField(blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection'
        unique_together = (('donor', 'volunteer'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('PtAuthPtaccount', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Donor(models.Model):
    donor_id = models.TextField(primary_key=True)
    name = models.TextField()
    phone_no = models.IntegerField()
    d_email = models.TextField()
    team_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donor'


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
    sub_head = models.ForeignKey('SubHead', models.DO_NOTHING, blank=True, null=True)

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


class PtAuthPtaccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_no = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True, blank=True, null=True)
    username = models.TextField(unique=True, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    team = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'pt_auth_ptaccount'


class PtAuthPtaccountGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    ptaccount = models.ForeignKey(PtAuthPtaccount, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pt_auth_ptaccount_groups'
        unique_together = (('ptaccount', 'group'),)


class PtAuthPtaccountUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    ptaccount = models.ForeignKey(PtAuthPtaccount, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pt_auth_ptaccount_user_permissions'
        unique_together = (('ptaccount', 'permission'),)


class SubHead(models.Model):
    sub_head = models.OneToOneField(Member, models.DO_NOTHING, primary_key=True)
    head = models.ForeignKey(Head, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_head'


class Volunteer(models.Model):
    volunteer = models.OneToOneField(Member, models.DO_NOTHING, primary_key=True)
    sub_head = models.ForeignKey(SubHead, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volunteer'


class VolunteerAssignment(models.Model):
    sub_head = models.OneToOneField(SubHead, models.DO_NOTHING, primary_key=True)
    volunteer = models.ForeignKey(Volunteer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'volunteer_assignment'
        unique_together = (('sub_head', 'volunteer'),)
