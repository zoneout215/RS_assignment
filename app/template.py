import streamlit as st
from random import random
import json
import datetime
import os

directory_path = os.getcwd()  + os.sep + 'data' + os.sep

def select_movie(id):
  st.session_state['id'] = id

# save the activities as a file
def save_activities():
  with open(directory_path + 'activities.json', 'w') as outfile:
    json.dump(st.session_state['activities'], outfile, indent=4)

# function that processes an activity
def activity(id, activity):
  data = {'content_id': id, 'activity': activity, 'user_id': st.session_state['user'], 'datetime': str(datetime.datetime.now())}
  # add to the session state
  st.session_state['activities'].append(data)
  # directly save the activities
  save_activities()

def tile_item(column, item):
  
  with column:
    col1, col2, col3  = st.columns(3)
    
    with col1:
      st.button('▶', key=random(), on_click=activity, args=(item['id'], 'Play'))
    with col2:
      st.button('👍', key=random(), on_click=activity, args=(item['id'], 'Like'))
    with col3:
      st.button('👎', key=random(), on_click=activity, args=(item['id'], 'Dislike'))  
    
    st.image(item['image'], use_column_width='always')
    st.markdown(item['title'])
    

def tiles(df):
  # check the number of items
  nbr_items = df.shape[0]
  cols = 6

  if nbr_items != 0:
    # create columns with the corresponding number of items
    columns = st.columns(cols)

    # convert df rows to dict lists
    items = df.to_dict(orient='records')

    # apply tile_item to each column-item tuple (created with python 'zip')
    any(tile_item(x[0], x[1]) for x in zip(columns, items))
