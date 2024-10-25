import os
import django

# Set the settings module for your Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Initialize Django
django.setup()

from route_planner.models import TruckStop
import csv
count = 0
# CSV Loading Logic
with open('fuel-prices-for-be-assessment.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        TruckStop.objects.create(
            name=row['Truckstop Name'],
            address=row['Address'],
            city=row['City'],
            state=row['State'],
            price=float(row['Retail Price'])
        )
        count += 1

        print(f"{count} rows inserted.")

print("CSV data successfully loaded!")
