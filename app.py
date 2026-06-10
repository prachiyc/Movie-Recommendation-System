from flask import Flask, render_template, request
from recommender import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    message = ""

    if request.method == "POST":

        movie = request.form["movie"]
        recommendations = recommend(movie)

        if not recommendations:
            message = "Movie not found. Please try another title."

    return render_template(
        "index.html",
        recommendations=recommendations,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)