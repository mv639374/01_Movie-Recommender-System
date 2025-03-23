import pandas as pd
import streamlit as st
import pickle
import requests


# API Key - dee73acbf0b9895c4ee16b2c51079f00

# Fetch the posters
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dee73acbf0b9895c4ee16b2c51079f00&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']

# Make a recommend function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # Gives Index Position
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Title of the Page
st.title("Movie Recommender System")
st.write('This is web deplyoed python app')

# Load the pickle files
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict) # Convert back it to dataframe
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Select Box for movie name
selected_movie_name = st.selectbox('Write a movie name you want recommend of?',
movies['title'].values)

# Recommend Button
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
