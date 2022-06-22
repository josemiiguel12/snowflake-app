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

# funcion de insersion a Snowflake
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        query = "insert into fruit_load_list values ('from streamlit " + new_fruit + "')"
        my_cur.execute(query)
        return "Tranks fro adding " + new_fruit
    
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

#------------------------------------

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Mostramos el titulo
my_fruit_list = my_fruit_list.set_index('Fruit')

# Seleccion multiple de frutas
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error('Please select a fruit to get information')
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        # mostramos el dato en formato tabla
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()

# streamlit.stop()
streamlit.header("The fruit load list contains:")


if streamlit.button('Get Fruit Load List'):
    #Creamos la conexion de datos a Snowflake
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)


add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_function)
 
