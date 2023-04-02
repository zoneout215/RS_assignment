import pandas as pd
from numpy import random
import json
from numpy import random
import os

directory_path = os.getcwd()  + os.sep + 'data' + os.sep

df_users = pd.read_json(directory_path + 'users.json')

collaborative_movies = pd.read_csv(directory_path + 'movie_recommendations.csv')  #the output data from the collaborative filtering aglorithm
collaborative_shows = pd.read_csv(directory_path + 'show_recommendations.csv')

movies = pd.read_pickle(directory_path + 'full_movies.pkl')
Top_movies = pd.read_csv(directory_path + 'most_viewed_movies.csv')
shows = pd.read_pickle(directory_path + 'full_shows.pkl')
Top_shows = pd.read_csv(directory_path + 'most_viewed_shows.csv')

## Top viewed movies and shows:
top_movies_ids = Top_movies['content_id'].values.tolist()
df2 = movies[movies['id'].isin(top_movies_ids)]
df2.to_csv(directory_path + 'RECOMMEDED_top_movies.csv', encoding='utf-8', index=False)

top_shows_ids = Top_shows['content_id'].values.tolist()
df3 = shows[shows['id'].isin(top_shows_ids)]
df3.to_csv(directory_path + 'RECOMMEDED_top_shows.csv', encoding='utf-8', index=False)

## Colaborative filtering:
# first get current user id from session state and combine it with
for i in df_users.id[:4]:

    collaborative_movies_user_list_ids = collaborative_movies.iloc[i][:6]
    collaborative_shows_user_list_ids = collaborative_shows.iloc[i][:6]

    selected_movies = movies[movies['id'].isin(collaborative_movies_user_list_ids)]
    selected_movies.to_csv(directory_path + f'RECOMMEDED_FOR_{df_users.name.iloc[i-1]}_collaborative_movies.csv', encoding='utf-8', index=False)
    selected_shows = shows[shows['id'].isin(collaborative_shows_user_list_ids)]
    selected_shows.to_csv(directory_path + f'RECOMMEDED_FOR_{df_users.name.iloc[i-1]}_collaborative_shows.csv', encoding='utf-8', index=False)
