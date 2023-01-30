import streamlit
import pandas



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit') 
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')

streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')

streamlit.text('🐔 Half-boiled egg, Free-Range Egg')

streamlit.text('🥑🍞 Avocado-Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# ## Let's put a pick list here so they can pick the fruit they want to include
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# ## Display the selected fruits on the page.
streamlit.dataframe(fruits_to_show)

### new section to display fruitvie api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
# fruit name is static in the line below
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# to make it variale let's add plus sign
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) # write data to the screen

# take json version of the response and normalize it to panda dataframe
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output shown as as table
streamlit.dataframe(fruityvice_normalized)

## Display the table on the page.
#streamlit.dataframe(my_fruit_list)


