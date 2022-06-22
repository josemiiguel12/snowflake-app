import streamlit
import pandas 

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

#tabla filtrada con información nutricionak
streamlit.dataframe(my_fruit_list)
