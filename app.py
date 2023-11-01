import streamlit as st 
import requests
import pickle




movies=pickle.load(open('movies_list.pkl' , 'rb'))
similarity=pickle.load(open('similarity.pkl' , 'rb'))

movies_list=movies['title'].values
st.header("Movie Recommendation System")


selectedvalue=st.selectbox("Select a movie from dropdown", movies_list)


def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=33e9596e85e72a8bf0e14fdc2bc6279b&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


def recommend_movies(movie):
    index=movies[movies['title']==movie].index[0]
    # print ("Index is:",index)
    distance=sorted(list(enumerate(similarity[index])) , reverse=True , key=lambda vector:vector[1])
    recommend_posters=[]
    recommended_movies_list=[]
    for i in distance[1:8]:
        movie_id=movies.iloc[i[0]].id
        recommended_movies_list.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_poster(movie_id))
    return recommended_movies_list , recommend_posters




if st.button("Show Recommendation"):
    movie_name , movie_poster=recommend_movies(selectedvalue)
    col1,col2,col3,col4,col5,col6=st.columns(6)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
    with col6:
        st.text(movie_name[5])
        st.image(movie_poster[5])
 
  

