from django.db import models
import uuid

class Participant(models.Model):
    worker_id = models.CharField(max_length=50, unique=True)


class StudyRecord(models.Model):
    record_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE)
    experiment_version = models.CharField(max_length=50)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)
    condition_order = models.CharField(max_length=512, blank=True)
    article_order = models.CharField(max_length=512, blank=True)
    unique_code = models.CharField(max_length=512, blank=True)
    questionnaire_data = models.TextField(blank=True)
    demographic_data = models.TextField(blank=True)


class ReportRecord(models.Model):
    record_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    study_record = models.ForeignKey('StudyRecord', on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)
    article_id = models.IntegerField()
    condition_id = models.IntegerField()
    input_veracity = models.CharField(max_length=50, blank=True)
    input_q1 = models.CharField(max_length=50, blank=True)
    input_q2 = models.CharField(max_length=2018, blank=True)
    input_r1 = models.CharField(max_length=50, blank=True)
    input_r2 = models.CharField(max_length=50, blank=True)
    input_r3 = models.CharField(max_length=50, blank=True)
    user_logs = models.TextField(blank=True)
