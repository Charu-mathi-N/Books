from django.db import models

# Create your models here.
'''class Books(object):
    """docstring for Books"""
    def __init__(self, arg):
        super(Books, self).__init__()
        self.arg = arg

    def book():
        with open('book.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_file:
                book = csv.file'''

class Books(models.Model):
    Title = models.CharField(max_length = 100)
    Authors = models.CharField(max_length = 100)
    Rating = models.FloatField(max_length = 3)
    ISBN = models.CharField(max_length = 10)
    ISBN13 = models.CharField(max_length = 10)
    Language = models.CharField(max_length = 5)
    Pages =  models.IntegerField(blank=True, null=True)
    Rating_Count = models.IntegerField()
    Reviews_Count = models.IntegerField()
    Published_Date = models.CharField(max_length = 20)
    Publisher = models.CharField(max_length = 100)

# class cart(model.Model):

# class cartItem(model.Model):
