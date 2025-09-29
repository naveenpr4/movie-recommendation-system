import pandas as pd
import streamlit as st
import pickle as pkl

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
similarity=pkl.load(open('similarity.pkl','rb'))
movies_dict=pkl.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title("Movie Recommendation System")

selected_movie_name= st.selectbox(
"Select the MOVIE you LIKED",
    movies['title'].values)

if st.button("Recommend"):
    recommendations=recommend(selected_movie_name)
    st.write(selected_movie_name)
    for i in recommendations:
        st.write(i)