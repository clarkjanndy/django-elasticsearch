# myapp/management/commands/load_csv_data.py

import csv
from django.core.management.base import BaseCommand
from api.models import Employer

from tqdm import tqdm

class Command(BaseCommand):
    help = 'Load data from a CSV file as a fixture'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        # Read the CSV file and create model instances
        with open(csv_file, 'r') as file:
            csv_data = csv.DictReader(file)

            # Initialize tqdm with total_iterations and configure its appearance
            progress_bar = tqdm(total=0, desc="Saving...", unit=" iteration")

            for row in csv_data:
                instance = Employer(**row)
                instance.save()
                progress_bar.update(1)

            # Close the progress bar
            progress_bar.close()

            self.stdout.write(self.style.SUCCESS('Command executed successfully!'))

            
