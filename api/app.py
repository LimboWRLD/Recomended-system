import json
from flask import Flask, jsonify
from config import TMDB_API_KEY, TMDB_BASE_URL
import requests
import pickle

app = Flask(__name__)

with open('../notebooks/movie_id_mapping.json', 'r') as f:
    movie_id_mapping = json.load(f)


with open('../notebooks/knn_model.pkl', 'rb') as f:
    knn_model = pickle.load(f)





def get_movie_details(movie_id):
    url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        movie_data = response.json()
        return {
            'id': movie_data.get('id'),
            'title': movie_data.get('title'),
            'overview': movie_data.get('overview'),
            'poster_path': movie_data.get('poster_path'),
            'backdrop_path': movie_data.get('backdrop_path'),
            'release_date': movie_data.get('release_date'),
            'vote_average': movie_data.get('vote_average'),
            'vote_count': movie_data.get('vote_count'),
            'genre_ids': [genre['id'] for genre in movie_data.get('genres', [])],
            'production_companies': [company['name'] for company in movie_data.get('production_companies', [])],
        }
    else:
        return None



@app.route('/recommendations/<int:tmdb_id>', methods=['GET'])
def get_recommendations(tmdb_id):
    movie_id = next((k for k, v in movie_id_mapping.items() if v == tmdb_id), None)
    if not movie_id:
        return jsonify({'error': 'Movie not found in dataset'}), 404
    
    predictions = knn_model.get_neighbors(int(movie_id), k=10)
    movie_details = get_movie_details(tmdb_id);
    
    recommended_movies = []
    for pred in predictions:
        
        tmdb_id_new = movie_id_mapping.get(str(pred))
        if tmdb_id_new:

            pred_movie_details = get_movie_details(tmdb_id_new)
            if pred_movie_details:
                pred_movie_genre_ids = pred_movie_details['genre_ids']
                movie_details_genre_ids = movie_details['genre_ids']
                if set(movie_details_genre_ids).intersection(pred_movie_genre_ids):
                    recommended_movies.append(pred_movie_details)
                print(pred_movie_details)
        

    return jsonify(recommended_movies)

if __name__ == "__main__":
    app.run(debug=True)
