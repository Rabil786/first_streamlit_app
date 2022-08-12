import pandas
import streamlit

streamlit.title('Hello World')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list,200.100)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.fruit))
