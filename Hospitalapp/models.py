from django.db import models

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.name


class doctors(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    department =models.CharField(max_length=50)
    status =models.CharField(max_length=50)
    phone =models.CharField(max_length=15)


    def __str__(self):
        return self.name+ " "+self.status




class staff(models.Model):
    firstname = models.CharField(max_length=20)
    lastname =models.CharField(max_length=20)
    position =models.CharField(max_length=20)
    phone =models.CharField(max_length=20)
    email =models.EmailField()
    hiredate =models.DateField()


    def __str__(self):
        return self.firstname+ " "+self.lastname



class ward(models.Model):
    name = models.CharField(max_length=20)
    totalbeds = models.IntegerField()
    availablebeds =models.IntegerField()


    def __str__(self):
        return self.name




class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    phone = models.CharField(max_length=25)
    date = models.DateTimeField()
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.TextField()


    def __str__(self):
        return self.name





    class Appointment(models.Model):
        name = models.CharField(max_length=50)
        email = models.EmailField()
        subject = models.CharField(max_length=25)
        message = models.TextField()

        def __str__(self):
            return self.name




