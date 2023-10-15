import csv

# Function to read names from CSV and write to TXT
def csv_to_txt(csv_filename, txt_filename):
    count = 0
    with open(csv_filename, mode ='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        with open(txt_filename, mode='w') as txt_file:
            for row in csv_reader:
                txt_file.write(row['name'] + '\n')
                count += 1
                
            txt_file.write(f'Total count of names: {count}')

# Specify the names of your CSV and TXT files
csv_filename = 'yelp_academic_dataset_restaurants.csv'
txt_filename = 'restaurant_names.txt'

# Call the function
csv_to_txt(csv_filename, txt_filename)