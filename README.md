# Movie Recommendation System

## Overview

This project is an AI-powered Movie Recommendation System developed using Flask, Python, Pandas, and Scikit-learn. The system uses content-based filtering techniques to recommend movies with similar genres based on a movie title entered by the user.

The application provides a simple and user-friendly web interface where users can search for a movie and receive recommendations with explanations.

## Features

* Content-based movie recommendation system
* Genre similarity matching using cosine similarity
* Flask web application
* User-friendly interface
* Invalid movie title validation
* Recommendation explanations

## Technologies Used

* Python 3.11
* Flask
* Pandas
* Scikit-learn
* HTML
* CSS
* MovieLens Dataset

## Dataset

This project uses the MovieLens Latest Small Dataset provided by the GroupLens Research Group.

## How to Run

1. Activate the Conda environment:

conda activate movie_rec

2. Navigate to the project directory.

3. Run the Flask application:

python app.py

4. Open the application in a browser:

http://127.0.0.1:5000

## Example

Input:

Toy Story

Output:

* Toy Story 2
* Antz
* Monsters, Inc.
* The Emperor's New Groove
* Adventures of Rocky and Bullwinkle

## Future Improvements

* Collaborative filtering recommendations
* User rating support
* Movie poster integration
* Personalized recommendations
* Chatbot-based recommendation interface

## Author

Prachi Chaudhari

## License

This project was created for educational purposes as part of the Artificial Intelligence for Human-Computer Interaction course.
