import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


ratings = pd.DataFrame({
    'userId': [1, 1, 1, 2, 2, 3, 3, 4],
    'movieId': [10, 20, 30, 10, 40, 20, 30, 40],
    'rating': [4, 5, 3, 5, 4, 2, 5, 3]
})

movies = pd.DataFrame({
    'movieId': [10, 20, 30, 40],
    'title': ['Inception', 'Interstellar', 'The Dark Knight', 'Tenet']
})


user_item_matrix = ratings.pivot_table(
    index='userId', columns='movieId', values='rating'
).fillna(0)

print("User-Item Rating Matrix:")
print(user_item_matrix)


similarity_matrix = cosine_similarity(user_item_matrix)
similarity_df = pd.DataFrame(similarity_matrix, index=user_item_matrix.index, columns=user_item_matrix.index)

print("\nUser Similarity Matrix:")
print(similarity_df)

def recommend_movies(user_id, num_recommendations=2):

    similar_users = similarity_df[user_id].sort_values(ascending=False).index[1:]
    

    recommended_movies = []
    for sim_user in similar_users:
        movies_rated = ratings[ratings['userId'] == sim_user]
        recommended_movies.extend(movies_rated.sort_values(by='rating', ascending=False)['movieId'].tolist())
    

    user_movies = ratings[ratings['userId'] == user_id]['movieId'].tolist()
    final_recommendations = [m for m in recommended_movies if m not in user_movies]
    

    final_recommendations = movies[movies['movieId'].isin(final_recommendations)]['title'].head(num_recommendations)
    return final_recommendations.tolist()


print("\nRecommended Movies for User 1:")
print(recommend_movies(1, num_recommendations=2))
