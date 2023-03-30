import streamlit as st
import pandas as pd
import authenticate as a
from numpy import random
import json
from numpy import random
import template as t
import pygame
from PIL import Image
import os

# gets current working directory
directory_path = os.getcwd()  + os.sep + 'data' + os.sep

df = pd.read_json(directory_path + 'test_data.json')
df_users = pd.read_json(directory_path + 'users.json')

random_image_number =random.randint(0, len(df))

#####################################################################
####################### THE APP #####################################
#####################################################################

st.set_page_config(layout="wide")

logo = Image.open(directory_path + 'abc_logo.png')
logo_width = 150
logo_height = 150
logo_loc = st.empty()
logo_loc.image(logo, width=logo_width, use_column_width=False)
# maybe add some content to the right of the logo:
st.write("Some content to the right of the logo...")


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
if st.session_state['authentication_status']:

  # create a cover and info column to display the selected book
  cover, info = st.columns([2, 3])

  with cover:
    # display the image
    st.image(df['image'].iloc[random_image_number], width = 600,  use_column_width=False)

  with info:
    col1, col2 = st.columns([2, 3])
    # display the movie information
    with col2:
      st.title(df['title'].iloc[random_image_number])
      # st.caption(df['publication_date'].iloc[0])
      st.markdown(df['description'].iloc[random_image_number])
      # st.caption('Season ' + str(df_episode['season']) + ' | episode ' + str(df_episode['episode']) + ' | Rating ' + str(df_episode['rating']) + ' | ' + str(df_episode['votes']) + ' votes')


  st.subheader('Dive into Australian content')
  df = pd.read_json(directory_path + 'test_data.json')
  t.tiles(df)


  # part to create personalized user content:
  # based on user personas and collaborative filtering:
  # we are going to create two CB ribbons for movies and shows!

  cb = pd.read_csv(directory_path + 'jonas_sofo_data.csv')  #the output data from the collaborative filtering aglorithm

  # first get current user id from session state and combine it with
  # collaborative filtering data:
  #df_cb_user = df_cb[df_cb['user_id'] == st.session_state['user']]
  cb_user_list_ids = cb.iloc[st.session_state['user']][:6]
  # test with movies dataframe:
  movies = pd.read_pickle(directory_path + 'full_movies.pkl')
  selected_df = movies[movies['id'].isin(cb_user_list_ids)]
  st.subheader('Recommended movies for you')
  t.tiles(selected_df)
