from src import logger
import pandas as pd
import pathlib
import pickle
import streamlit as st
import requests

movies_dict=pickle.load(open("models/movies_dict.pkl","rb"))
movies_df=pd.DataFrame(movies_dict)

movie_similarity=pickle.load(open("models/similarity.pkl","rb"))

app_logger=logger.get_logger(__name__,"Training.txt")

def fetch_poster(movie_id):
    response=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a6bd2cc04687c3598361a82a51b422c7&language=en-US")
    data=response.json()
    image="http://image.tmdb.org/t/p/w500/"+data['poster_path']
    return image


def recommend_movie(movie):
    movie_index=movies_df[movies_df['title']==movie].index[0]
    distances=movie_similarity[movie_index]
    movies_list=sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters = []
    for j in movies_list:
        movie_id=movies_df.iloc[j[0]].id
        recommended_movies.append(movies_df.iloc[j[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


if __name__=="__main__":
    st.title("Movie Recommender System by Content Based")
    selected_movie_name =st.selectbox("Select a movie from the dropdown",movies_df['title'].values)
    if st.button("Recommend"):
        names,posters= recommend_movie(selected_movie_name)
        col1,col2,col3,col4,col5=st.columns(5)
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
