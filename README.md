# Movie Recommendation System

A content-based movie recommender system built with Python, using machine learning techniques to suggest similar movies based on genres, keywords, cast, crew, and plot overview.

## Features

- **Content-Based Filtering**: Recommends movies based on similarity in content features rather than user preferences
- **Interactive Web Interface**: Built with Streamlit for easy movie selection and recommendation display
- **Movie Posters**: Fetches and displays movie posters from TMDB API
- **Top 5 Recommendations**: Shows the 5 most similar movies for any selected movie

## Dataset

The system uses the TMDB 5000 Movie Dataset, which includes:
- `tmdb_5000_movies.csv`: Movie metadata including genres, keywords, overview, etc.
- `tmdb_5000_credits.csv`: Cast and crew information for movies

## How It Works

1. **Data Preprocessing**:
   - Merges movie and credits datasets
   - Extracts relevant features: genres, keywords, cast (top 3 actors), director, and overview
   - Creates "tags" by combining all text features
   - Applies stemming to normalize words

2. **Feature Extraction**:
   - Uses CountVectorizer to convert text tags into numerical vectors
   - Limits to 5000 most frequent words

3. **Similarity Calculation**:
   - Computes cosine similarity between all movie vectors
   - Creates a similarity matrix

4. **Recommendation Engine**:
   - For a selected movie, finds the most similar movies based on cosine similarity scores
   - Returns top 5 recommendations (excluding the selected movie itself)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd movie-recommendation-system
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

## Usage

### Training the Model

Run the Jupyter notebook to preprocess data and train the model:
```bash
jupyter notebook main.ipynb
```

This will generate `movies.pkl` and `similarity.pkl` files.

### Running the Web App

Start the Streamlit application:
```bash
streamlit run main.py
```

Open your browser to `http://localhost:8501` to use the recommender.

## Project Structure

```
movie-recommendation-system/
├── main.ipynb              # Data preprocessing and model training
├── main.py                 # Streamlit web application
├── pyproject.toml          # Project configuration and dependencies
├── README.md               # This file
├── tmdb_5000_movies.csv    # Movie dataset
├── tmdb_5000_credits.csv   # Credits dataset
├── movies.pkl              # Processed movie data (generated)
└── similarity.pkl          # Similarity matrix (generated)
```

## Dependencies

- `numpy` - Numerical computing
- `pandas` - Data manipulation
- `scikit-learn` - Machine learning algorithms
- `nltk` - Natural language processing (stemming)
- `streamlit` - Web application framework
- `requests` - HTTP requests for TMDB API
- `ipykernel` - Jupyter notebook support

## API Key

The application uses TMDB API to fetch movie posters. The API key is hardcoded in `main.py`. For production use, consider using environment variables.

## Future Improvements

- Add user-based collaborative filtering
- Implement hybrid recommendation system
- Add movie ratings and reviews
- Improve UI/UX with better styling
- Add search functionality
- Deploy to cloud platform

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.