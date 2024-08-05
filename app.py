from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request
from flask import Flask, make_response
app = Flask(__name__)
@app.route('/')
def index():
     return render_template('index.html')

@app.route('/cad/usuario')
def usuario():
      return render_template('usuario.html', titulo='Cadastro de Usuário')

#@app.route('/cad/caduser', methods=['POST'])
#def caduser():
#     return request.form

@app.route('/cad/anuncio')
def anuncio():
       return render_template('anuncio.html')

@app.route('/anuncio/pergunta')
def pergunta():
       return render_template('pergunta.html')

@app.route('/anuncios/compra')
def compra():
      print('Anúncio comprado')
      return ''

@app.route('/anuncio/favorito')
def favoritos():
       print('Favorito inserido')
       return '<h4>Comprado</h4>'


@app.route('/config/categoria')
def categoria():
       return render_template('categoria.html')

@app.route('/relatorio/vendas')
def relVendas():
       return render_template('relVenda.html')


@app.route('/relatorio/compra')
def relCompras():
      return render_template('relCompra.html')

       