from .models import User, Student, HighSchoolList
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class StudentSerializer(serializers.ModelSerializer):
    race = serializers.ModelField(model_field=Student()._meta.get_field('race'))

    class Meta:
        model = Student
        fields = (
            'id',
            'url',
            'user',
            'lastname',
            'firstname',
            'phone',
            'school',
            'gradescale',
            'grade',
            'race',
            'parentsgraduated',
            'householdsize',
            'familyincome',
            'actsat',
            'sat_critical_reading',
            'sat_math',
            'sat_writing',
            'act_composite',
            'act_english',
            'act_math',
            'act_reading',
            'act_science',)


class HighSchoolSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = HighSchoolList
        fields = (
            'url',
            'name',
            'mail_city',
            'state')
