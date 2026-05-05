import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Book Recommender", layout="centered")


st.title("📚 Book Recommendation System")
st.write("Select a book and get top 5 similar recommendations")


pivot = pickle.load(open('pivot.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(book_name):
    index = np.where(pivot.index == book_name)[0][0]
    distances = similarity[index]
    books = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_books = []
    for i in books:
        recommended_books.append(pivot.index[i[0]])

    return recommended_books

book_list = pivot.index.values
selected_book = st.selectbox("📖 Choose a Book", book_list)

if st.button("🔍 Recommend"):
    results = recommend(selected_book)

    st.subheader("📌 Recommended Books:")
    for book in results:
        st.write("👉", book)