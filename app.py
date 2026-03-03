import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np

movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')
name_movie = st.selectbox(
    'Select a movie from the list below',
    movies_list
)


def fecther_poster(movie_id):
    response = requests.get( f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=9770fef79370960a130344f45bbf23fa&language=en-US")
    data = response.json()
    poster_path = data['poster_path']
    full_path = 'https://image.tmdb.org/t/p/w500' + poster_path
    return full_path

def recommend(name_movie):
    index = movies_df[movies_df["title"] == name_movie].index[0]
    distances = similarity[index]
    movies_list_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:20]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list_sorted:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fecther_poster(movie_id))
    return recommended_movies, recommended_movies_poster


if st.button('Recommend'):
    name,posters = recommend(name_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    col = [col1, col2, col3, col4, col5]
    for i in range(len(name)):
        with col[i % 5]:
            st.image(posters[i])
            st.text(name[i])