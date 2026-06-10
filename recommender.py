import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("data/movies.csv")
movies["genres"] = movies["genres"].fillna("")

vectorizer = CountVectorizer(tokenizer=lambda x: x.split("|"))
genre_matrix = vectorizer.fit_transform(movies["genres"])

similarity_matrix = cosine_similarity(genre_matrix)

def recommend(movie_title):

    try:
        idx = movies[movies["title"].str.contains(movie_title, case=False)].index[0]
    except:
        return []

    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    results = []

    for i in scores[1:6]:
        results.append({
            "title": movies.iloc[i[0]]["title"],
            #"genre": movies.iloc[i[0]]["genres"],
            "genre": movies.iloc[i[0]]["genres"].replace("|", ", "),
            "reason": "Similar genre match"
        })

    return results