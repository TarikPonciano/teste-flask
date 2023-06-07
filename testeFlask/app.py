from flask import *
from Controle.classConexao import Conexao

import env


app = Flask(__name__)

conexaoBanco = Conexao(env.dbname,env.host,env.port,env.user,env.password)

@app.route("/")
def index():
    return "bem vindo"+os.getenv("DBNAME")

@app.route("/version")
def version():

    return conexaoBanco.consultarBanco("Select version()")

@app.route("/Pokemons")
def listaPokemon():

    pokedex = conexaoBanco.consultarBanco('''Select * From "Pokedex"''')

    listaPokemons = []

    for pokemon in pokedex:

        listaPokemons.append({'id':pokemon[0], 'especie':pokemon[1]})

    return jsonify(listaPokemons)

if __name__ == "__main__":
    app.run(debug=True)