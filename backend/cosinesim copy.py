import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def most_similar_reviews(business_id, csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Group reviews by business_id
    grouped = df.groupby('business_id')['text'].apply(' '.join).reset_index()

    # Compute TF-IDF matrix
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform(grouped['text'])

    # Get the index of the business_id in the dataframe
    idx = grouped[grouped['business_id'] == business_id].index[0]

    # Compute cosine similarity with other businesses
    cosine_similarities = cosine_similarity(tfidf[idx:idx+1], tfidf).flatten()

    # Get the index of the most similar business (excluding itself)
    most_similar_idx = cosine_similarities.argsort()[-2]
    
    # Return the business_id of the most similar business
    return grouped.loc[most_similar_idx, 'business_id']

# Test the function
# print(most_similar_reviews('C3Nc7EUqo64jRPWPn6vY9w'))
# """
# XQfwVwDr-v0ZS3_CbbE5Xw -> oqP1oQEycpp4J6u5YebRoQ

# """