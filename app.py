from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <p>Filipe Dourado Pereira RA 2202115</p>
    <p>Henrique Almeida Silva RA 2202055</p>
    <p>Matheus Marques Matos de Oliveira RA 2201538 </p>
    <p>Rodrigo Antony Oliveira Maia RA 2201647</p>
    <p>Vitor Gabriel Pereira Becker RA 2202237</p>
'''