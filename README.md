
# Movie Recommendation System

This project implements a movie recommendation system using a dataset of movie ratings and genres. The system uses a K-Nearest Neighbors (KNN) model to provide movie recommendations based on a given movie's ID. 

## Requirements

Before you start, ensure that you have the following installed:
- Python 3.12 or higher
- Pip (Python package manager)
- Git
- Jupyter Notebook

You will also need to create an account on [TMDb](https://www.themoviedb.org/) and get your own API key to interact with the TMDb API.

## Setup

### 1. Unzip the Dataset

The first step is to unzip the dataset. Navigate to the `datasets/` folder and unzip the dataset file.

```bash
unzip datasets/dataset.zip -d datasets/
```

This will extract the necessary files into the `datasets/` folder.

### 2. Install Dependencies

You will need to install the necessary Python libraries to run the project. Use the following command to install the required packages:

```bash
pip install -r requirements.txt
```

This will install all the dependencies specified in the `requirements.txt` file.

### 3. Run the Model Building Jupyter Notebook

Next, open the `model_building.ipynb` notebook and run all the code blocks in order. This will train the recommendation model and generate the necessary files, such as the KNN model and movie ID mapping.

To run the Jupyter notebook, you can use the following command:

```bash
jupyter notebook notebooks/model_building.ipynb
```

After running the notebook, it will save the trained model (`knn_model.pkl`) and the movie ID mapping (`movie_id_mapping.json`) to the `notebooks/` folder.

### 4. Add Your TMDb API Key

Before running the Flask app, you will need to add your own TMDb API key and the TMDb base URL. 

1. Open the `api/app.py` file.
2. Find the following lines:

```python
TMDB_API_KEY = 'YOUR_TMDB_API_KEY'
TMDB_BASE_URL = 'https://api.themoviedb.org/3'
```

3. Replace `'YOUR_TMDB_API_KEY'` with your actual TMDb API key.

### 5. Run the Flask App

Now that everything is set up, you can run the Flask application to start the server. Run the following command:

```bash
python api/app.py
```

This will start the Flask server on `http://127.0.0.1:5000`. You can now make GET requests to the `/recommendations/<tmdb_id>` endpoint to get movie recommendations based on a movie's TMDb ID.

Example:

```bash
http://127.0.0.1:5000/recommendations/383498
```

This will return the recommended movies based on the movie with TMDb ID `383498`.

## Project Structure

```
.
├── api/                    # Flask API server
│   └── app.py              # Main application code
├── datasets/               # Unzipped dataset files
├── notebooks/              # Jupyter notebooks for model building
│   ├── data_exploration.ipynb
│   └── model_building.ipynb
├── requirements.txt        # List of dependencies
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Notes

- Ensure that the dataset is correctly unzipped before running the notebook.
- You may need to adjust the Flask app configuration based on your machine's setup.
- If you encounter any issues with the KNN model or Flask server, check the logs for debugging information.

---
