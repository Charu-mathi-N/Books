from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from main.models import Books
from pytz import UTC

DATETIME_FORMAT = '%m/%d/%Y'

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the books data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):

    help = "Loads data from books_data.csv into our Books mode"

    def handle(self, *args, **options):
        print("Loading the CSV file")

        if book.objects.exists():
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(open("./Book.csv")):
                book = Books()
                book.Title = row['title']
                book.Authors = row['authors']
                book.Rating = row['average_rating']
                book.ISBN = row['isbn']
                book.ISBN13 = row['isbn13']
                book.Language = row['language_code']
                book.Pages = row['  num_pages']
                book.Rating_Count = row['ratings_count']
                book.Reviews_Count = row['text_reviews_count']
                book.Published_Date = row['publication_date']
                book.Publisher = row['publisher']
                book.save()

        print("Loaded the data into the database")
