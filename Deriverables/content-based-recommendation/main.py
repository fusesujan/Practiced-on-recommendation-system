import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI, HTTPException

# Create an instance of FastAPI
app = FastAPI()

# Capture similarity
data = pd.read_csv("./data/new_data.csv")

# Content Similarity function (you can include this)
# Content Similarity
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(data["combined"])
cosine_similarities = linear_kernel(matrix, matrix)
movie_title = data['title']
indices = pd.Series(data.index, index=data['title'])


def content_recommender(title):
    '''
    function that takes title as
    input and then returns series of movies.
    '''
    idx = indices[title]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return movie_title.iloc[movie_indices]


@app.post("/recommend")
async def recommend_books(request: dict):
    input_title = request.get("title")

    if input_title is None:
        raise HTTPException(
            status_code=400, detail="Title is missing in the request")

    recommended_books = content_recommender(input_title)
    return {"recommended_books": recommended_books.tolist()}


# If you want a root endpoint for testing
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Book Recommendation API!"}
