from django.db import models

from concepts.models import Concept

# Create your models here.
# 환자에 대한 정보
class Person(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    gender_concept_id = models.IntegerField(blank=True, null=True)
    year_of_birth = models.IntegerField(blank=True, null=True)
    month_of_birth = models.IntegerField(blank=True, null=True)
    day_of_birth = models.IntegerField(blank=True, null=True)
    birth_datetime = models.DateTimeField(blank=True, null=True)
    race_concept_id = models.IntegerField(blank=True, null=True)
    ethnicity_concept_id = models.IntegerField(blank=True, null=True)
    location_id = models.BigIntegerField(blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    care_site_id = models.BigIntegerField(blank=True, null=True)
    person_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_concept_id = models.IntegerField(blank=True, null=True)
    race_source_value = models.CharField(max_length=50, blank=True, null=True)
    race_source_concept_id = models.IntegerField(blank=True, null=True)
    ethnicity_source_value = models.CharField(max_length=50, blank=True, null=True)
    ethnicity_source_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


# 환자의 사망 정보
class Death(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    death_date = models.DateField(blank=True, null=True)
    death_datetime = models.DateTimeField(blank=True, null=True)
    death_type_concept_id = models.IntegerField(blank=True, null=True)
    cause_concept_id = models.BigIntegerField(blank=True, null=True)
    cause_source_value = models.IntegerField(blank=True, null=True)
    cause_source_concept_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'death'