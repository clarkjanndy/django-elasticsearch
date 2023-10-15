from django.db import models

__all__ = ['Employer']

class Employer(models.Model):
    rank = models.IntegerField() 
    company = models.CharField(max_length=255)
    industries = models.CharField(max_length=255)  
    country_territory = models.CharField(max_length=255)  
    employees = models.IntegerField()  
    publish_year = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.company}"

    class Meta:
        db_table = 'employers'