from django.db import models

class Candidate(models.Model):
    instruction_ID = models.IntegerField()
    case_ref_no = models.CharField(max_length=20)
    client_name = models.CharField(max_length=50)
    candidate_name = models.CharField(max_length=50)
    complete_address = models.TextField()
    period_od_stay = models.DateField()

    def __str__(self):
        return self.candidate_name 

