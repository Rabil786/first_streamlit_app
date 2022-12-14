import pandas
import requests
import streamlit
import snowflake.connector
from urllib.error import URLError

streamlit.title('Hello World')
streamlit.header('Breakfast Menu')
streamlit.text(' π₯£Omega 3 & Blueberry Oatmeal')
streamlit.text(' π₯Kale, Spinach & Rocket Smoothie')
streamlit.text(' π Hard-Boiled Free-Range Egg')
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('ππ₯­ Fruityvice Fruit Advice π₯π')
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice) 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json() 
    return fruityvice_normalized
                                                
streamlit.header('Fruityvice Fruit Advice!') 
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?') 
  if not fruit_choice:
     streamlit.error("Please select a fruit to get information.") 
  else:
     back_from_function = get_fruityvice_data(fruit_choice) 
     streamlit.dataframe(back_from_function)
  
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding ', fruit_choice)
my_cur.execute("insert into fruit_load_list values('from streamlit')")

