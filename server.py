from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route("/produtos")
    def produtos():
        produtos = { 1: "Smartwatch Iwo 8", 2: "Xiaomi Amazfit Bip", 3: "Apple Watch Series 3"}
        imagens = {1: "iwo8.jpg", 2: "amazfit.jpg", 3: "smartwartch.jpg"}

        return render_template('products.html', produtos=produtos, imagens=imagens)

    @app.route("/detalhes")
    def detalhes():

        return render_template('model.html')

    return app


app = create_app()

app.run(debug=True, port=2001, host="localhost")