import streamlit as st
from random import random
import json
import datetime

def select_movie(id):
  st.session_state['id'] = id



def tile_item(column, item):
  with column:
    #st.button('📖', key=random(), on_click=select_movie, args=(item['id'],))
    st.button('▶', key=random(), on_click=select_movie, args=(item['id'], ))
    st.image(item['image'], use_column_width='always')
    st.markdown(item['title'])
    #st.caption(item['summary'][:50] + (item['summary'][50:] and '..'))
    #st.caption('Season ' + str(item['season']) + ' | episode ' + str(item['episode']) + ' | Rating ' + str(item['rating']) + ' | ' + str(item['votes']) + ' votes')



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