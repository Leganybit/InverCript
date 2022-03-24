from flask import Flask, render_template

def create_app():
	app = Flask(__name__)

	@app.route("/")
	def inicio():
		return render_template("/inicio.html")

	@app.route("/ahorro")
	def ahorro():
		return render_template("/pages/ahorro.html")
	@app.route("/inversion")
	def inversion():
		return render_template("/pages/Inversión.html")
	@app.route("/contacto")
	def contacto():
		return render_template("/pages/contacto.html")

	@app.route("/blog")
	def blog():
		return render_template("/pages/blog/entradas/blog.html")	
	@app.route("/blog/hyperledger")
	def hyperledger():
		return render_template("/pages/blog/entradas/hyperledger.html")
	@app.route("/blog/wiki")
	def wiki():
		return render_template("/pages/blog/entradas/wiki.html")		


	return app