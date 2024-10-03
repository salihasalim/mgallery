from django.db import models

class GenreChoice(models.TextChoices):

    ACTION='Action','Action'

    THRILLER='Thriller','Thriller'

    ROMANCE='Romance','Romance'

    COMEDY='Comedy','Comedy'

class Movies(models.Model):

    title=models.CharField(max_length=200)

    genre=models.CharField(max_length=200,choices=GenreChoice.choices)

    language=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    director=models.CharField(max_length=200)





    # WE CAN PUT CHOICE OPTION IN ANOTHER WAY


  
    # Genre_choice=[('Action','Action'),
    
    #               ('Thriller','Thriller'),
    #               ('Romance','Romance')
    #             ]

    #   genre=models.CharField(max_length=200,choices=GenreChoice)




# class Student(models.Model):

#     name=models.CharField(max_length=200)

#     classs=models.CharField(max_length=200,choices=ClassChoice.choices)

#     division=models.CharField(max_length=200,choices=DivisionChoice.choices)

#     contact=models.IntegerField()

    #    photo=models.ImageField()
 
    # url=models.URLField()



   #   about_me=models.TextField()


# class  ClassChoice(models.IntegerChoices):

#     'ONE'=1,1

#     'Two'=2,2

#     'THREE'=3,3

#     'FOUR'=4,4

#     'FIVE'=5,5

#     'SIX'=6,6

#     'SEVEN'=7,7

#     'EIGHT'=8,8

#     'NINE'=9,9

#     'TEN'=10,10


# class DivisionChoice(models.TextChoices):

#     'A'='A','A'

#     'B'= 'B', 'B'

#     'C'= 'C', 'C'

#     'D'= 'D', 'D'







# car 
# milage
# fuel type
# web link\

# Name 
# model
# reg.num
# stiock
# seat capacity
# releasedate




# class Car(models.model):

#     name=models.CharField(max_length=200)

#     model=models.CharField(max_length=200)

#     milage=models.IntegerField()

#     reg.num=models.IntegerField()

#     stock=models.CharField(max_length=200,choices=)

#     seat_capacity=models.IntegerField()


#     releasedate=models.DateTimeField()

#     fuel_type=models.CharField(max_length=200,choices=)


#     class FuelChoice(models.TextChoices):

#         'DIESEL'='Diesel','Diesel'
#         'PETROL'='Petrol','Petrol'\
#         'EV'='Ev','Ev'
    
#     class StockChoice(models.TextChoices):

#       'IN_STOCK'='In_stock','In_stock'
#       'OUT_STOCK'='Out_stock','Out_stock'









# class Registration(models.Model):

#     firstname=models.CharField(max_length=200,null=False)

#     lastname=models.CharField(max_length=200,null=False)
    
#     Address=models.CharField(max_length=200,null=False)
    
#     street=models.CharField(max_length=200)
    
#     streetline=models.CharField(max_length=200,null=True)
    
#     city=models.CharField(max_length=200)
    
#     state=models.CharField(max_length=200)
    
#     post=models.CharField(max_length=200)
    
#     phone=models.IntegerField(null=False)
    
#     email=models.EmailField()
    
#     about_us=models.CharField(max_length=200,null=False,choices=AboutChoice.choices)
    
#     feedback=models.TextField()
    
#     suggestions=models.TextField()
#     willing=models.CharField(max_length=200,choices=WillingChoice.choices)
    






class AboutChoice(models.TextChoices):
    NEWSPAPER='Newspaper','Newspaper'
    INTERNET='Internet','Internet'
    MAGAZINE='Magazine','Magazine'
    OTHER='Other','Other'





class WillingChoice(models.TextChoices):

    YES='Yes','Yes'
    NO='No','No'
    MAYBE='Maybe','Maybe'

















