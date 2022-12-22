from django.db import models
from django.forms import CharField


gender=(
       ('male','male'),
       ('female','female'),
  )

level=(
      ('First level','First level'),
      ('Second level','Second level'),
      ('Third level','Third level'),
      ('Fourth level','Fourth level'),
)
  

depart=(
         ('IT','IT'),
         ('CS','CS'),
         ('DS','DS'),
         ('AI','AI'),
         ('IS','IS')
  )


status=(
         ('Active','Active'),
         ('Inactive','Inactive'),
  )


class students(models.Model):
  
  name = models.CharField(max_length=255)

  id1=models.PositiveIntegerField(
     primary_key=True
  )

  birthday=models.DateField()

  gpa=models.FloatField()

  gender=models.CharField(choices=gender,
        max_length = 20,
       
  )
  
  level=models.CharField(choices=level,
        max_length = 20,
       
  )

  depart=models.CharField(choices=depart,
        max_length = 20,
       
  )

  status=models.CharField(choices=status,
        max_length = 20,
       
  )
  
  email=models.EmailField()
  mobile=models.IntegerField()


class modretur(models.Model):
    userName=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    gender=models.CharField(choices=gender,
    max_length=20)

    Email=models.EmailField(
    )



