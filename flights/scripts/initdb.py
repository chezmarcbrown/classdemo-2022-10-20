import csv
from flights.models import Airport

FNAME = "seeddata/airports.csv"

def run():
    print(f'Reading file: {FNAME}')
    with open(FNAME) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'Processsing: {row}')
            code = row["code"]
            city = row["city"]
            # if not Airport.objects.exists(code=code):
            #     a = Airport(code=code, city=city)
            #     a.save()
            Airport.objects.get_or_create(code=code, city=city)
