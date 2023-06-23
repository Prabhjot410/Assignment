import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dish_search_app.settings')
django.setup()

from dish_search.models import Restaurant

def load_data():
    with open('restaurants_small.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            latitude, _ = row['lat_long'].split(',')
            Restaurant.objects.create(
                name=row['name'],
                location=row['location'],
                items=row['items'],
                latitude=float(latitude),
                details=row['full_details']
            )

if __name__ == '__main__':
    load_data()
