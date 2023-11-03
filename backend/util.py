from cosinesim import most_similar_reviews
# data description:

#       restuarants is a list of dictionaries

# keys of restuarants are:
    # restuarant = {
    #     "business_id": "string",
    #     "name": "string",
    #     "address": "string",
    #     "city": "string",
    #     "state": "string",
    #     "postal_code": "string",
    #     "latitude": "string",
    #     "longitude": "string",
    #     "stars": "string",
    #     "review_count": "string",
    #     "is_open": "string",
    #     "attributes": dictionary,
    #     "categories": list,
    #     "hours": "string"
# }
# This function takes in a list of restaurant names and the complete set of restaurants and returns a list of recommended restaurants.
# Note that the input restaurant names are not necessarily in the list of all restaurants, so check for that.
# The input restuarants are a list of dictionaries, the definition inside is commented out above.

def generate_recommendations(input_restaurant, city, restaurants):

    r1 = input_restaurant[0]
    r2 = input_restaurant[1]
    r3 = input_restaurant[2]

    my_dict = {d["name"]: d for d in restaurants}
    restaurant1 = my_dict[r1]
    restaurant2 = my_dict[r2]
    restaurant3 = my_dict[r3]
    filtered_list = [c for c in restaurants if c["city"] == city]
    list_of_restaurants = []
    for r in filtered_list:
        score_1 = get_similarity_score(restaurant1, r)
        score_2 = get_similarity_score(restaurant2, r)
        score_3 = get_similarity_score(restaurant3, r)
        avg_score = (score_1+score_2+score_3)/3
        list_of_restaurants.append((r,avg_score))
    sorted_list = sorted(list_of_restaurants, key=lambda x: x[1], reverse=True)
    return sorted_list[0:3]


def get_similarity_score(r1, r2):
    #takes in two restaurants and returns their similarity score
    return get_price_similarity(r1,r2)+get_category_similarity(r1,r2) + float(r2['stars'])

def get_price_similarity(r1,r2):
    #takes in two restaurants and returns how similar their prices are based on the price range in the yelp dataset
    if('attributes' not in r1 or 'attributes' not in r2):
        return 2.5
    # print(r1['attributes'])
    # try:
    #     if ('RestaurantsPriceRange2' in r1['attributes'] and 'RestaurantsPriceRange2' in r2['attributes']):
    #         diff = int(r1['attributes']['RestaurantsPriceRange2']) - int(r2['attributes']['RestaurantsPriceRange2'])
    #         diff = abs(diff)
    #         return 5 - diff
    else:
        return 2.5
def get_category_similarity(r1,r2):
    #takes in two restaurants and returns the jaccard similarity of the set of their categories
    r1_categories = set(r1['categories'])
    r2_categories = set(r2['categories'])
    intersection = r1_categories.intersection(r2_categories)
    union = r2_categories.union(r1_categories)
    sim = len(intersection)/len(union)
    return sim

def cosine_similarity_reviews(r1, r2):
    r1_row = list(business_id_to_text.keys()).index(r1['business_id'])
    r2_row = list(business_id_to_text.keys()).index(r2['business_id'])
    r1_vec = restaurant_topic_matrix[r1_row]
    r2_vec = restaurant_topic_matrix[r2_row]
    return cosine_similarity(r1_vec, r2_vec)

def SVD(tfidf):
    svd = TruncatedSVD(n_components=10)
    svd.fit(tfidf)
    topic_term_matrix = svd.components_
    restaurant_topic_matrix = svd.transform(tfidf)
    return restaurant_topic_matrix
