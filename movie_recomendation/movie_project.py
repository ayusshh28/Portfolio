import streamlit as st
import joblib
import numpy as np
import requests

# --- Load saved models and data ---
tv = joblib.load("tfidf_vectorizer.pkl")
model = joblib.load("knn_model.pkl")
movies = joblib.load("movies_dataframe.pkl")

# --- Page Configuration ---
st.set_page_config(page_title="Movie Recommender", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #8e9eab, #eef2f3);
        background-attachment: fixed;
        color: #1a1a1a;
    }
    .poster-container img {
        width: 220px !important;
        height: 320px !important;
        object-fit: cover;
        border-radius: 10px;
        border: 4px solid #ccc;
        box-shadow: 0 6px 14px rgba(0, 0, 0, 0.3);
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🎬 Movie Recommendation System")
st.markdown("Get similar movies based on your favorite one!")

# --- Input from user ---
movie_list = ['-- Select your movie --'] + sorted(movies['name'].unique())

st.markdown("""
    <style>
    /* Change cursor to pointer when hovering over the selectbox */
    div[data-baseweb="select"] > div {
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

selected_movie = st.selectbox(
    "Choose a movie",
    options=sorted(movies['name'].unique()),
    index=None,
    placeholder="Select your movie"
)

# --- Recommendation Function ---

API_KEY = "85a6b972"  

def fetch_poster(movie_id):
    url = f"http://www.omdbapi.com/?i={movie_id}&apikey={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        poster = data.get("Poster", "")

        # Enhanced validation check
        if not poster or poster.strip() == "" or poster == "N/A" or poster.startswith("http") is False:
            return "https://via.placeholder.com/300x450?text=No+Image+Available"
        return poster

    except:
        return "https://via.placeholder.com/300x450?text=Error"


num_recommendations = st.slider("How many movie recommendations do you want?", min_value=2, max_value=10, value=5)

def recommend(movie_name, n_recommendations):
    movies_reset = movies.reset_index(drop=True)
    vectors = tv.transform(movies_reset['tag'])

    try:
        index = movies_reset[movies_reset['name'] == movie_name].index[0]
    except IndexError:
        return [], []

    distances, indices = model.kneighbors(vectors[index], n_neighbors=n_recommendations + 1)  # +1 to skip itself

    recommended_movies = movies_reset.iloc[indices[0][1:]]  # skip self
    names = recommended_movies['name'].values
    movie_ids = recommended_movies['movie_id'].values

    posters = [fetch_poster(movie_id) for movie_id in movie_ids]

    return names, posters

# --- Show Recommendations ---
if st.button("Recommend 🎥"):
    if selected_movie != '-- Select your movie --':
        recommended_movies, recommended_posters = recommend(selected_movie, num_recommendations)

        st.subheader("📽️ Recommended Movies:")
        cols = st.columns(min(5, num_recommendations))
        for i in range(len(recommended_movies)):
            with cols[i % len(cols)]:
                st.markdown('<div class="poster-container">', unsafe_allow_html=True)
                st.image(recommended_posters[i])
                if "No+Image" in recommended_posters[i] or "Error" in recommended_posters[i]:
                    st.markdown('<p style="color: red; font-weight: bold;">Image not available</p>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown(f"**{recommended_movies[i]}**")

    else:
        st.warning("⚠️ Please select a movie from the dropdown.")
