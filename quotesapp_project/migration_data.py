import certifi
import django
from pymongo import MongoClient
from django.conf import settings
from django.conf import global_settings
from quotesapp.models import Author, Quote


settings.configure(
    default_settings=global_settings,
    DEBUG=True,
    INSTALLED_APPS=[
        'quotesapp',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': '567234',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
)

django.setup()


def migrate_data():
    client = MongoClient(
        "mongodb+srv://test_db:test@cluster0.1nimxos.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        tlsCAFile=certifi.where()
    )
    mongo_db = client['quotes']
    mongo_collection_quotes = mongo_db['quotes']
    mongo_collection_authors = mongo_db['authors']

    for document in mongo_collection_authors.find():
        fullname = document.get("fullname")
        born_date = document.get("born_date")
        born_location = document.get("born_location")
        description = document.get("description")

        Author.objects.create(
            fullname=fullname,
            born_date=born_date,
            born_location=born_location,
            description=description
        )

    for document in mongo_collection_quotes.find():
        tags = document.get("tags")
        author_name = document.get("author")
        quote_text = document.get("quote")

        author_instance = Author.objects.get(fullname=author_name)

        Quote.objects.create(
            quote=quote_text,
            author=author_instance,
            tags=tags
        )

    client.close()


if __name__ == "__main__":
    migrate_data()
