import streamlit as st
import pandas as pd
import authenticate as a
from numpy import random
import json
from numpy import random
import template as t
from PIL import Image
import os

# gets current working directory
directory_path = os.getcwd()  + os.sep + 'data' + os.sep

df = pd.read_csv(directory_path + 'data/RECOMMENDED_mix_austalia.csv')
df_users = pd.read_json(directory_path + 'users.json')

RECOMMEDED_top_movies = pd.read_csv(directory_path + 'RECOMMEDED_top_movies.csv')
RECOMMEDED_top_shows = pd.read_csv(directory_path + 'RECOMMEDED_top_shows.csv')

random_image_number =random.randint(0, len(df))

#####################################################################
####################### THE APP #####################################
#####################################################################

st.set_page_config(layout="wide")

logo = Image.open(directory_path + 'abc_logo.png')
logo_width = 200
logo_height = 200
logo_loc = st.empty()
logo_loc.image(logo, width=logo_width, use_column_width=False)
# maybe add some content to the right of the logo:

st.header("Welcome to Australia! ")
with open(directory_path + 'activities.json') as json_file:
  users_activities = json.load(json_file)

if 'user' not in st.session_state:
  st.session_state['user'] = 0

if 'activities' not in st.session_state:
  st.session_state['activities'] = users_activities

if 'id' not in st.session_state:   # to start with a content item as a "home screen"
  st.session_state['id'] = 741.0

#authenticate
a.authenticate()
name_of_user = df_users.name.iloc[st.session_state['user']-1]

if st.session_state['authentication_status']:

  # create a cover and info column to display the selected book
  cover, info = st.columns([2, 3])

  with cover:
    # display the image
    st.image(df['image'].iloc[random_image_number], width = 700,  use_column_width=False)

  with info:
    col1, col2 = st.columns([2, 3])
    # display the movie information
    with col2:
      st.title(df['title'].iloc[random_image_number])
      # st.caption(df['publication_date'].iloc[0])
      st.markdown(df['description'].iloc[random_image_number])
      # st.caption('Season ' + str(df_episode['season']) + ' | episode ' + str(df_episode['episode']) + ' | Rating ' + str(df_episode['rating']) + ' | ' + str(df_episode['votes']) + ' votes')


  st.subheader('Dive into Australian content')
  t.tiles(df)

  # Top movies based on plays:
  st.subheader('Most viewed movies')
  t.tiles(RECOMMEDED_top_movies)

  # # Top shows based on plays:
  st.subheader('Most viewed shows')
  t.tiles(RECOMMEDED_top_shows)

  # part to create personalized user content:
  # based on user personas and collaborative filtering:
  # we are going to create two CB ribbons for movies and shows!

  ## Colaborative filtering:
  selected_movies = pd.read_csv(directory_path + f'RECOMMEDED_FOR_{name_of_user}_collaborative_movies.csv')
  st.subheader('Recommended movies for you')
  t.tiles(selected_movies)

  selected_shows = pd.read_csv(directory_path + f'RECOMMEDED_FOR_{name_of_user}_collaborative_shows.csv')
  st.subheader('Recommended shows for you')
  t.tiles(selected_shows)
