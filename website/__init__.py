from flask import Flask, render_template, request, redirect, url_for
import json
import os 
import website.contact_form


def create_app():
	app = Flask(__name__)

	@app.route("/")
	def inicio():
		return render_template("/inicio.html")

	@app.route("/ahorro")
	def ahorro():
		return render_template("/pages/ahorro.html")
	@app.route("/nuestrosProductos")
	def nuestrosProductos():
		return render_template("/pages/nuestrosProductos.html")
	@app.route("/contacto", methods=['GET', 'POST'])
	def contacto():
		website.contact_form.data_form_save()
		return render_template("/pages/contacto.html", email = "caca", ciudad=request.form.get("ciudad"))
#__________________-Blog____________________________________
	@app.route("/blog")
	def blog():
		return render_template("/pages/blog/entradas/blog.html")	
	@app.route("/blog/hyperledger")
	def hyperledger():
		return render_template("/pages/blog/entradas/hyperledger.html")
	@app.route("/blog/wiki")
	def wiki():
		return render_template("/pages/blog/entradas/wiki.html")
	@app.route("/blog/top_10")
	def top_10():
		return render_template("/pages/blog/entradas/top_blockchains_usadas_empresas.html")	
		#______________________Estrategias____________________	
	@app.route("/blog/estrategias/volumen")
	def volumen():
		return render_template("/pages/blog/entradas/estrategias_inversion/volumen.html")
	@app.route("/blog/estrategias/pares_sinteticos")
	def pares_sinteticos():
		return render_template("/pages/blog/entradas/estrategias_inversion/pares_sintetios.html")
		#_______________Criptomonedas___________________
	@app.route("/blog/criptomonedas/ada")
	def ada():
		return render_template("/pages/blog/entradas/criptomonedas/ada.html")	
		#______________________Beneficios Inverccript____________________	
	@app.route("/blog/beneficios/fiscalidad")
	def fiscalidad():
		return render_template("/pages/blog/entradas/BeneficiosDeInvercript/ahorroFiscal.html")	
	@app.route("/blog/beneficios/seguridad")
	def seguridad():
		return render_template("/pages/blog/entradas/BeneficiosDeInvercript/seguridad.html")
	@app.route("/blog/beneficios/diversificacion")
	def diversificacion():
		return render_template("/pages/blog/entradas/BeneficiosDeInvercript/diversificacion.html")

	return app