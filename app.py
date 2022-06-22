#-----------------------------------
# LIBRERIAS
#-----------------------------------
import streamlit
import pandas 
import requests
import snowflake.connector
#-----------------------------------
#FUNCIONES
#------------------------------------


# Creacion de funcion
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    # streamlit.text(fruityvice_response.json())

    # Normalizamos el dato que nos entrega la api rest
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
#------------------------------------

streamlit.title('Esto es un titulo')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

#Agregar una sección para crear tu batido
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#cargar un listado a un dataframe desde s3
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#crear un filtrado con multiples selecciones 
my_fruit_list = my_fruit_list.set_index('Fruit')

# Seleccion multiple de frutas
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

#filtro a nivel de tabla
fruits_to_show = my_fruit_list.loc[fruits_selected]

#tabla filtrada con información nutricional
streamlit.dataframe(fruits_to_show )

#consumir una API
streamlit.header("Fruityvice Fruit Advice!")

# text input para consultar sobre una fruta
fruit_choice = streamlit.text_input('What fruit would you like information about?')

#invocamos la funcion get para consultar una fruta
back_from_function = get_fruityvice_data(fruit_choice)

# mostramos el dato en formato tabla filtrado desde un text inut
streamlit.dataframe(back_from_function)

# Creacion de funcion
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    # streamlit.text(fruityvice_response.json())

    # Normalizamos el dato que nos entrega la api rest
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
 
