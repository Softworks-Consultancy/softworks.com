from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    user = models.OneToOneField(User, null=True, blank=True)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    gradescale = models.CharField(max_length=255, null=True, blank=True)
    grade = models.FloatField(null=True, blank=True)
    race = models.CharField(max_length=255, null=True, blank=True)
    parentsgraduated = models.BooleanField(default=True, blank=True)
    householdsize = models.IntegerField(null=True, blank=True)
    familyincome = models.CharField(max_length=255, null=True, blank=True)
    actsat = models.CharField(max_length=255, null=True, blank=True)
    sat_critical_reading = models.IntegerField(null=True, blank=True)
    sat_math = models.IntegerField(null=True, blank=True)
    sat_writing = models.IntegerField(null=True, blank=True)
    act_composite = models.IntegerField(null=True, blank=True)
    act_english = models.IntegerField(null=True, blank=True)
    act_math = models.IntegerField(null=True, blank=True)
    act_reading = models.IntegerField(null=True, blank=True)
    act_science = models.IntegerField(null=True, blank=True)

    @classmethod
    def create(cls, user):
        new_student = cls(user=user)
        new_student.save()
        return new_student

    @property
    def normalize_race(self):
        normal_race = None
        if self.race:
            if self.race=="Black":
                normal_race = "Black"
            elif self.race =="Latino" or self.race=="Hispanic":
                normal_race = "Hispanic"
            else:
                normal_race = "White"
        return normal_race


class HighSchoolList(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    borough = models.CharField(max_length=255, null=True, blank=True)
    sed_bed_code = models.BigIntegerField(null=True, blank=True)
    institution_type = models.CharField(max_length=255, null=True, blank=True)
    inst_sub_type = models.CharField(max_length=255, null=True, blank=True)
    needs_resource = models.CharField(max_length=255, null=True, blank=True)
    school_type = models.CharField(max_length=255, null=True, blank=True)
    community_type = models.CharField(max_length=255, null=True, blank=True)
    mailing_address = models.CharField(max_length=255, null=True, blank=True)
    mail_city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)


class Counsellor(models.Model):
    pass
