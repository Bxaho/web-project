from django.db import models

class Student(models.Model):
    FACULTY_CHOICES = (
        ('Science and Technology','Science and Technology'),
        ('Management','Management'),
        ('Humanities','Humanities'),
        ('Education','Education'),
    )

    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    faculty = models.CharField(max_length=50, choices=FACULTY_CHOICES, default='Management')
    email = models.EmailField(blank=True)
    contact = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name
