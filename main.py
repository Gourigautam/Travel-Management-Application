from flask import Flask, request, jsonify
from flask_cors import CORS 
import subprocess
import requests
from mysql.connector import errorcode
from  model import model_input


def get_url():
    response = requests.get('http://localhost:4040/api/tunnels')
    data = response.json()
    ng_url = data['tunnels'][0]['public_url']
    f =  open('token.txt','w')
    f.writelines(ng_url)
    f.close()

try:
    get_url()
    print("1")
except :
    ngrok_process = subprocess.Popen(['ngrok', 'http', '5000'])
    print("2")
finally:
     get_url()
     print("3")


app = Flask(__name__)
CORS(app)


@app.route('/gen_response', methods=['POST'])
def screen_seeho():
    data =  request.args.get('q')
    q = str(data)
    response = model_input(q)
    response_data = {'message': f'{response}'}
    return jsonify(response_data)



if __name__ == '__main__':
    app.run(port=5000)
