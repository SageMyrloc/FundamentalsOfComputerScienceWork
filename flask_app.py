# import flask
from flask import Flask, render_template
# import package to read csv and iterator tools
import csv
import itertools
import os

app = Flask(__name__)
# route = localhost

def get_data():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # get the directory for the data
    csv_path = os.path.join(dir_path, "static", "data", "Kaggle_TwitterUSAirlineSentiment.csv")
    # open the data specifying the encoding used
    with open(csv_path, encoding="utf-8-sig") as csv_file:
        # set data using the csv file and naming the delimiter
        data = csv.reader(csv_file, delimiter=',')
        # set first line to true so that the first line is avoided
        first_line = True
        # create an array to store the results
        tweet_data = []
        # iterate through the data adding it to tweetData
        for row in data:
            # if we are not on the first line run this code
            if not first_line:
                tweet_data.append({
                    "id": row[0],
                    "airline_sentiment": row[1],
                    "airline_sentiment_confidence": row[2],
                    "negative_reason": row[3],
                    "airline": row[4],
                    "name": row[5],
                    "text": row[6],
                    "tweet_created": row[7],
                    "tweet_location": row[8]
                })
            # if we are on the first line set first line to False so that the next line will be read
            else:
                first_line = False
        return tweet_data


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n-i-1):
            if array[j]["airline_sentiment_confidence"] > array[j+1]["airline_sentiment_confidence"]:
                array[j], array[j+1] = array[j+1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array


@app.route('/')
def index():
    return render_template("index.html")


# route = localhost/basic
@app.route('/basic')
def basic():
    tweet_data = get_data()
    # sort the data using the bubble sort above
    bubble_sort(tweet_data)
    # limit the amount of data returned.
    return_data = itertools.islice(tweet_data, 40)
    # render the file using the template of basic.html.
    return render_template("basic.html", tweetData=return_data)

@app.route('/advanced')
def advanced():
    return render_template("advanced.html")

@app.route('/creative')
def creative():
    return render_template("creative.html")