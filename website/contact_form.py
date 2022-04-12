from flask import Flask, render_template, request, redirect, url_for
import json
import os 
#Se saca del formulario en función del nombre en el html

def data_form_save():
	email = request.form.get("e-mail")
	direccion = request.form.get("direccion")
	ciudad = request.form.get("ciudad")
	comunidad = request.form.get("comunidad")
	codPostal = request.form.get("codPostal")
	check = request.form.get("check")
	#Creo una carpeta si no existee, la creo.
	create_folder = "data"
	if not os.path.exists(create_folder):
		os.makedirs(create_folder)
	#inserto el archivo en una función, si no existe, lo crea.
	file_data = f'data/data.json'
	#declaro el archivo que debo buscar si existe.
	file_exist = os.path.isfile(f'data/data.json')
	#Si el archivo no existe, hace esto: lo cre y guarda
	if file_exist == False:
		data = [
		[email, direccion, ciudad, comunidad, codPostal, check]
		]
		with open(file_data, 'a+') as fd:
			json.dump(data, fd, indent=4)
	else:
		with open(file_data, 'r') as fd:
			json_load = json.load(fd)
		data = [
		[email, direccion, ciudad, comunidad, codPostal, check]
		]
		total_data = json_load + data 
		fd.close()
		with open(file_data, 'w') as fd:
			json.dump(total_data, fd, indent=4)