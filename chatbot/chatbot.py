from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/get_movie_detail', methods=['POST'])
def get_movie_detail():
       data = request.get_json(silent=True)
       movie = data['queryResult']['parameters']['movie']
       movie = movie.replace(" ", "_") 
       movie_detail = requests.get('http://www.omdbapi.com/?t={0}&apikey=YOUR_API_KEY'.format(movie)).content
       movie_detail = json.loads(movie_detail)
       response =  """
           Title : {0}
           Released: {1}
           Actors: {2}
           Plot: {3}
       """.format(movie_detail['Title'], movie_detail['Released'], movie_detail['Actors'], movie_detail['Plot'])

       reply = {
           "fulfillmentText": response,
       }
       return jsonify(reply)

# run Flask app
if __name__ == "__main__":
    app.run(debug=False, port = 5001)