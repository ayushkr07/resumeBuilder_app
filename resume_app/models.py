from django.db import models

MONTHS_CHOICES = (
    ('jan','JAN'),
    ('feb', 'FEB'),
    ('march','MARCH'),
    ('april','APRIL'),
    ('may','MAY'),
    ('june','JUNE'),
    ('july', 'JULY'),
    ('aug','AUG'),
    ('sep','SEP'),
    ('oct','OCT'),
    ('nov','NOV'),
    ('dec','DEC'),
)
YEAR_CHOICES = (
    ('2009','2009'),
    ('2009', '2009'),
    ('2010','2010'),
    ('2011','2011'),
    ('2012','2012'),
    ('2013','2013'),
    ('2014', '2014'),
    ('2015','2015'),
    ('2016','2016'),
    ('2018','2017'),
    ('2019','2019'),
    ('2020','2020'),
)

STAR_CHOICES = (
    ('5','5,EXPERT'),
    ('4', '4,EXPERIENCED'),
    ('3','3,SKILLFUL'),
    ('2','2,BEGINNER'),
    ('1','1,NOVICE'),
)

class Personal(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE,related_name='personals')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    intro = models.TextField()

    def __str__(self):
        return self.name

class Education(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='educations')
    institution_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    degree = models.CharField(max_length=30)
    stream = models.CharField(max_length=70,blank=True,null=True)
    percentage_or_cg = models.CharField(max_length=10,blank=True,null=True)
    graduation_year=models.CharField(max_length=8)

class Employment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='employments')
    employer = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    description = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    start_month = models.CharField(max_length=6, choices=MONTHS_CHOICES, default='may')
    start_year = models.CharField(max_length=6, choices=YEAR_CHOICES, default='2019')
    presently_working = models.BooleanField()
    end_month = models.CharField(max_length=6, choices=MONTHS_CHOICES, blank=True,null=True)
    end_year = models.CharField(max_length=6, choices=YEAR_CHOICES, blank=True,null=True)

class Project(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='projects')
    project_title = models.CharField(max_length=100)
    description = models.TextField()

class Skill(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=50)
    skill_rating = models.CharField(max_length=20, choices=STAR_CHOICES, default='3')

class Certificate(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='certificates')
    certificate_title = models.CharField(max_length=100,null=True,blank=True)
    organization = models.CharField(max_length=100)
    month = models.CharField(max_length=6, choices=MONTHS_CHOICES, default='may')
    year = models.CharField(max_length=6, choices=YEAR_CHOICES, default='2019')
    description = models.TextField()
