import pickle

# import pandas as pd
import requests
import streamlit as st


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=22987175c6efbda61383e80cd48d2ef8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w185/SPECIFICMOVIEPOSTERPATH" + data['poster_path']

def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)) , reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []
    for i in movies_list:
        movie_id = movies_list.iloc[i[0]].movie_id

        recommend_movies.append(movies_list.iloc[i[0]].title)
        # fetch poster from API
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_posters
        # print(new_df.iloc[i[0]].title)

movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
# movies_list = movies_list['title'].values


similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")


option = st.selectbox(
    "How would you like to be contacted?",
    movies_lists['title'].values)

if st.button('Recommend'):
    names, posters = recommend(option)
    # for i in recommendations:
    #     st.write(i)
    st.write(option)

    col1, col2, col3, col4, col5 = st.beta_columns(5)
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
