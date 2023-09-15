import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Load and preprocess data
ratings = pd.read_csv(
    "https://s3-us-west-2.amazonaws.com/recommender-tutorial/ratings.csv")
movies = pd.read_csv(
    "https://s3-us-west-2.amazonaws.com/recommender-tutorial/movies.csv")


def create_matrix(df):
    N = len(df['userId'].unique())
    M = len(df['movieId'].unique())
    user_mapper = dict(zip(np.unique(df["userId"]), list(range(N))))
    movie_mapper = dict(zip(np.unique(df["movieId"]), list(range(M))))
    user_index = [user_mapper[i] for i in df['userId']]
    movie_index = [movie_mapper[i] for i in df['movieId']]
    X = csr_matrix((df["rating"], (movie_index, user_index)), shape=(M, N))
    return X, user_mapper, movie_mapper


X, user_mapper, movie_mapper = create_matrix(ratings)


def find_similar_movies(movie_id, X, k, metric='cosine', show_distance=False):
    neighbour_ids = []
    if movie_id not in movie_mapper:
        return neighbour_ids  # Return an empty list if the movie_id is not found
    movie_ind = movie_mapper[movie_id]
    movie_vec = X[movie_ind]
    k += 1
    kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
    kNN.fit(X)
    movie_vec = movie_vec.reshape(1, -1)
    neighbour = kNN.kneighbors(movie_vec, return_distance=show_distance)
    for i in range(0, k):
        n = neighbour.item(i)
        neighbour_ids.append(movie_mapper[n])
    neighbour_ids.pop(0)
    return neighbour_ids


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}


@app.get("/recommend/{movie_id}")
async def recommend_movies(movie_id: int):
    similar_ids = find_similar_movies(movie_id, X, k=10)
    if not similar_ids:
        return {"error": "Movie ID not found or not enough data to make recommendations."}

    movie_title = movies[movies['movieId'] == movie_id]['title'].values[0]

    recommended_movies = []
    for i in similar_ids:
        title = movies[movies['movieId'] == i]['title'].values[0]
        recommended_movies.append(title)

    return {"movie_title": movie_title, "recommended_movies": recommended_movies}
