
import pandas as pd
import matplotlib.pyplot as plt


business = pd.read_json('yelp_academic_dataset_business.json', lines=True)

#  Filter out businesses that are not restaurants

is_resaurant = business['categories'].str.contains('Restaurants')

# make the is_restaurant column from NA to False

is_resaurant = is_resaurant.fillna(False)

business = business[is_resaurant]

# draw a matplotlib piegram based on the stars
business['stars'].value_counts().plot(kind='pie', autopct='%1.0f%%', figsize=(6, 6))