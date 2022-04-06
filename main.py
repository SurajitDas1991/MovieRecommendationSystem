from utils import *
from src import logger
import template
import pandas as pd
import pathlib
import pickle
import streamlit as st

movies_dict=pickle.load(open("models/movies_dict.pkl","rb"))
movies_df=pd.DataFrame(movies_dict)

movie_similarity=pickle.load(open("models/similarity.pkl","rb"))

app_logger=logger.get_logger(__name__,"Training.txt")


def recommend_movie(movie):
    movie_index=movies_df[movies_df['title']==movie].index[0]
    distances=movie_similarity[movie_index]
    movies_list=sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for j in movies_list:
        recommended_movies.append(movies_df.iloc[j[0]].title)
    return recommended_movies


if __name__=="__main__":
    #app_logger.info("Creating project folders if they do not exist")
    #template.SetupTemplate()
    #print(get_folder_path())
    st.title("Movie Recommender System by Content Based")
    selected_movie_name =st.selectbox("Select a movie from the dropdown",movies_df['title'].values)
    if st.button("Recommend"):
        recommendations= recommend_movie(selected_movie_name)
        for i in recommendations:
            st.write(i)
