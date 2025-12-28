import streamlit as st
import pickle
import requests as req

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = req.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distance = similarity[index]
    movie_list = sorted(enumerate(distance), reverse=True, key=lambda x:x[1])[1:6]

    get_movies_titles = []
    get_movies_posters = []
    for x in movie_list:
        
        movie_index = movies.iloc[x[0]].id
        movie_title = movies.iloc[x[0]].title
        
        poster = fetch_poster(movie_index)
        
        get_movies_titles.append(movie_title)
        get_movies_posters.append(poster)

    return get_movies_titles, get_movies_posters

st.title("Movie Recommender System")

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button("Recommed") and selected_movie:
    get_movies_titles, get_movies_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(get_movies_posters[0])
        st.text(get_movies_titles[0])
    with col2:
        st.image(get_movies_posters[1])
        st.text(get_movies_titles[1])
    with col3:
        st.image(get_movies_posters[2])
        st.text(get_movies_titles[2])
    with col4:
        st.image(get_movies_posters[3])
        st.text(get_movies_titles[3])
    with col5:
        st.image(get_movies_posters[4])
        st.text(get_movies_titles[4])
