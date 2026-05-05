import pandas as pd
import numpy as np
import pickle

print("📥 Loading dataset...")


books = pd.read_csv('Books.csv', sep=',', encoding='latin-1', on_bad_lines='skip')
ratings = pd.read_csv('Ratings.csv', sep=',', encoding='latin-1', on_bad_lines='skip')


books.columns = books.columns.str.strip()
ratings.columns = ratings.columns.str.strip()

print("Books columns:", books.columns)


books = books[['ISBN', 'Book-Title', 'Book-Author']]


books.rename(columns={
    'Book-Title': 'title',
    'Book-Author': 'author'
}, inplace=True)

ratings.rename(columns={
    'User-ID': 'user_id',
    'Book-Rating': 'rating'
}, inplace=True)

print("🔗 Merging datasets...")


data = ratings.merge(books, on='ISBN')

print("👥 Filtering active users...")


active_users = data.groupby('user_id').count()['rating'] > 200
active_users = active_users[active_users].index
data = data[data['user_id'].isin(active_users)]

print("📚 Filtering popular books...")


popular_books = data.groupby('title').count()['rating'] >= 50
popular_books = popular_books[popular_books].index
data = data[data['title'].isin(popular_books)]

print("📊 Creating pivot table...")

pivot = data.pivot_table(index='title', columns='user_id', values='rating')
pivot.fillna(0, inplace=True)

print("🤖 Computing similarity matrix...")

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(pivot)

print("💾 Saving model files...")

pickle.dump(pivot, open('pivot.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ Training Completed Successfully!")