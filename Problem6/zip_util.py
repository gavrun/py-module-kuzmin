# zip_util module

import os
import csv

def read_zip_all():
    zip_data = []
    dir_path = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(dir_path, 'us-zips', 'uszips.csv')
                            
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            zip_entry = [
                row['zip'],
                float(row['lat']),
                float(row['lng']),
                row['city'],
                row['state_id'],
                row['county_name']
            ]
            zip_data.append(zip_entry)
    return zip_data


