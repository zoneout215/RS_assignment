import streamlit as st
import pandas as pd
# import template as t
import authenticate as a
import numpy as np
import json
from itertools import cycle
from random import random
import base64
import template as t
import pygame
from PIL import Image

st.set_page_config(layout="wide")
#replaced csvjson.json file name with test_data.json
# the simpsons episodes

logo = Image.open('data/abc_logo.png')
logo_width = 150
logo_height = 150
logo_loc = st.empty()
logo_loc.image(logo, width=logo_width, use_column_width=False)
# maybe add some content to the right of the logo:
st.write("Some content to the right of the logo...")


df = pd.read_json('data/test_data.json')

df_users = pd.read_json('data/users.json')

with open('data/activities.json') as json_file:
  users_activities = json.load(json_file)
#
# # create a session state
# # if 'season' not in st.session_state:
# #   st.session_state['season'] = 1
# #
# # if 'episode' not in st.session_state:
# #   st.session_state['episode'] = 'tt0348034'
#
if 'user' not in st.session_state:
  st.session_state['user'] = 0

if 'activities' not in st.session_state:
  st.session_state['activities'] = users_activities

if 'id' not in st.session_state:   # to start with a content item as a "home screen"
  st.session_state['id'] = 741.0

#df= df[df['id'] == st.session_state['id']]

#authenticate
a.authenticate()

if st.session_state['authentication_status']:

  # def add_bg_from_local(image_file):
  #     with open(image_file, "rb") as image_file:
  #         encoded_string = base64.b64encode(image_file.read())
  #     st.markdown(
  #     f"""
  #     <style>
  #     .stApp {{
  #         background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
  #         background-size: cover
  #     }}
  #     </style>
  #     """,
  #     unsafe_allow_html=True
  #     )

  # add_bg_from_local('data/backg.jpg')


  # based on the users ID that logs in we need to get recommendations
  # first try with content based data from Kate:
  # using template.py as in the labs

  # create a cover and info column to display the selected book
  cover, info = st.columns([2, 3])

  with cover:
    # display the image
    st.image(df['image'].iloc[0], width = 600,  use_column_width=False)

  with info:
    col1, col2 = st.columns([2, 3])
    # display the movie information
    with col2:
      st.title(df['title'].iloc[0])
      # st.caption(df['publication_date'].iloc[0])
      st.markdown(df['description'].iloc[0])
      # st.caption('Season ' + str(df_episode['season']) + ' | episode ' + str(df_episode['episode']) + ' | Rating ' + str(df_episode['rating']) + ' | ' + str(df_episode['votes']) + ' votes')


  st.subheader('Dive into Australian content')
  #df = pd.read_json('test_data.json')
  #df.to_csv('test_data.csv', encoding='utf-8', index=False)
  df = pd.read_json('data/test_data.json')
  #df = df.merge(df_books, on='ISBN')
  t.tiles(df)


  # part to create personalized user content:
  # based on user personas and collaborative filtering:
  # we are going to create two CB ribbons for movies and shows!

  cb = pd.read_csv('data/jonas_sofo_data.csv')  #the output data from the collaborative filtering aglorithm
  # first get current user id from session state and combine it with
  # collaborative filtering data:
  #df_cb_user = df_cb[df_cb['user_id'] == st.session_state['user']]
  cb_user_list_ids = cb.iloc[st.session_state['user']][:6]
  # test with movies dataframe:
  movies = pd.read_pickle('data/full_movies.pkl')
  selected_df = movies[movies['id'].isin(cb_user_list_ids)]
  st.subheader('Recommended movies for you')
  t.tiles(selected_df)
