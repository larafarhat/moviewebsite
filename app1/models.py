from django.db import models

# Create your models here.



class Movies(models.Model):
    movie_id= models.IntegerField(primary_key=True)
    movie_name = models.CharField(max_length=30)
    movie_location = models.CharField(max_length=30)
    movie_price = models.IntegerField(default=0)


class Users(models.Model):
    user_id= models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=30)

 


class Reservations(models.Model):
    reservation_id= models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    movie_id=models.ForeignKey(Movies,on_delete=models.CASCADE)
    reservation_locations=models.CharField(max_length=30)
    number_of_seats=models.IntegerField()

   
