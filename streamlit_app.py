import streamlit
streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')

streamlit.text('Omega 3 & Blueberry Oatmeal')

streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


#let's put a pick list
streamlit.multiselect("pick some fruits:", list(my_fruit_list.index))
                      
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

my_fruit_list = my_fruit_list.set_index('Fruit')

