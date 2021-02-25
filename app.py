import streamlit as st
import pandas as pd 
import numpy as np

from PIL import Image
import SessionState


# Parámetros
activities = ["Seleccione", "Iniciar"]
triangulos=Image.open("triangulos2.png")
logo_largo=Image.open("logo_largo.png")

st.set_page_config(
	page_title="ECSAN",
	page_icon="random",
	layout="centered",
	initial_sidebar_state="expanded",
	)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


def main():
	st.title("¿Estás listo para comenzar?")
	st.subheader("El Oficial de Policía del Futuro deberá contar con muchas habilidades del siglo XXI, descifra a continuación, si tienes madera para convertirte en un Oficial en este siglo")
	st.subheader(" ")
	st.markdown("**NOTA:** Este es un ejercicio individual. Un Oficial de Policía no solamente debe ser innovador, también debe ser ético. Resuelve por tu cuenta los acertijos sin preguntar a los demás y sin buscar en Google. Si tienes dificultades resolviendo alguno de los acertijos, pide ayuda y te enviaremos una pista. Sólo tú sabrás si cumpliste con este reto.")
	session_state = SessionState.get(name="", button_sent=False)
	button_sent = st.button("Iniciar")

	if button_sent:
		session_state.button_sent = True

	if session_state.button_sent:
		st.subheader(" ")
		st.subheader("PRIMERA MISIÓN:")
		st.subheader("Para ser un oficial innovador tienes que afinar bien tu oído, aclarar la visión y poner alerta los demás sentidos para lograr hacer empatía con las problemáticas sociales. ¿Cuántos triángulos ves en la siguiente imagen?")
		st.image(triangulos, caption=' ', use_column_width=True)

		input_string1 = st.text_input("Tu respuesta a la misión 1")
		if input_string1=='18':
			st.subheader("Felicitaciones. Has superado la primera prueba. Ahora tendrás que estimular tu creatividad, el pensamiento lateral.")
			st.subheader("SEGUNDA MISIÓN:")
			st.subheader('Resuelve el siguiente acertijo y continúa a la siguiente fase: Una persona vive en una casa redonda, rodeada por completo por ventanas. Por cualquier lugar por donde mire siempre ve al sur. ¿De qué color es el oso?')
			input_string2 = st.text_input("Tu respuesta a la misión 2")
			if input_string2=='blanco':
				st.subheader('Fantástico. Estás cerca de obtener la información que necesitas para ser un oficial adaptado a las condiciones del S. XXI. Ahora viene la última prueba')
				st.subheader("TERCERA MISIÓN:")
				st.subheader('Hay un video en donde se encuentra la última respuesta. Es un video muy famoso. El más visto en una plataforma que tiene nombre de oso. Quien da la conferencia tiene apellido como el nombre de un famoso náufrago. Mira el video y completa la siguiente frase:')
				st.subheader("Gente que tenía que moverse para '_ _ _ _ _ _'")

				input_string3 = st.text_input("Tu respuesta a la misión 3")
				if input_string3=='pensar':
					st.subheader('Maravilloso, has completado las tres pruebas. Te has hecho acreedor/a a la llave final.')
					st.subheader(' ')
					st.markdown('Ingresa a <a href="https://www.youtube.com">https://www.youtube.com</a>  el viernes 5 de marzo a las 4:00 pm y te enterarás cómo convertir tu investigación de grado en un proyecto de innovación.', unsafe_allow_html=True)
					st.image(logo_largo, use_column_width=True)
					st.balloons()


				elif input_string3 != '':
					st.error("Estás cerca, abre tu mente e inténtalo nuevamente!")
			elif input_string2 != '':
				st.error("Estás cerca, abre tu mente e inténtalo nuevamente!")
		elif input_string1 != '':
			st.error("Estás cerca, abre tu mente e inténtalo nuevamente!")


if __name__ == "__main__":
	main()