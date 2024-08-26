from django.db import models

class Player(models.Model):
    student_name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=15, unique=True)
    dob = models.DateField()
    sex = models.CharField(max_length=10)
    A_Level_School = models.CharField(max_length=200)
    course_of_study = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    Hall_of_Residence = models.CharField(max_length=50)
    main_sport = models.CharField(max_length=50)
    alternative_sport = models.CharField(max_length=50, blank=True, null=True)
    playing_experience = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    current_club = models.CharField(max_length=100, blank=True, null=True)
    contact_information = models.CharField(max_length=100)
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_contacts = models.CharField(max_length=100)
    food_allergy = models.TextField(blank=True, null=True)
    injury_history = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student_name
