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


minority = pd.read_csv(directory_path + 'RECOMMENDED_mix_div.csv')
df_users = pd.read_json(directory_path + 'users.json')

RECOMMEDED_top_movies = pd.read_csv(directory_path + 'RECOMMEDED_top_movies.csv')
RECOMMEDED_top_shows = pd.read_csv(directory_path + 'RECOMMEDED_top_shows.csv')
diversity = pd.read_csv(directory_path + 'diversity_library.csv').sample(5)


#####################################################################
####################### THE APP #####################################
#####################################################################

st.set_page_config(layout="wide")
# maybe add some content to the right of the logo:


with open(directory_path + 'activities.json') as json_file:
  users_activities = json.load(json_file)

if 'user' not in st.session_state:
  st.session_state['user'] = 0

if 'activities' not in st.session_state:
  st.session_state['activities'] = users_activities

if 'id' not in st.session_state:   # to start with a content item as a "home screen"
  st.session_state['id'] = 741.0

col1, col2 = st.columns([1, 3])
with col1:
    logo = Image.open(directory_path + 'abc_logo.png')
    logo_width = 200
    logo_height = 200
    logo_loc = st.empty()
    logo_loc.image(logo, width=logo_width, use_column_width=False)
with col2:
  new_title = '<p style="font-family:sans-serif; color:White; font-size: 80px;">Welcome to Australia!</p>'
  st.markdown(new_title, unsafe_allow_html=True)
  

# authenticate
a.authenticate()

random_image_number = random.randint(0, 4)


if st.session_state['authentication_status']:
  # create a cover and info column to display the selected book
  name_of_user = df_users.name[df_users.id == st.session_state['user']].iloc[0]
  df = pd.read_csv(directory_path + f'RECOMMENDED_FOR_{name_of_user}_austalia.csv')
  cover, info = st.columns([3, 1])

  with cover:
    # display the image
    st.image(df['image'].iloc[random_image_number],  use_column_width=True)

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
  
  st.subheader('Spotlighting diversity')
  t.tiles(diversity)

  # Top movies based on plays:
  st.subheader('Most viewed movies')
  # st.subheader(name_of_user)
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

  