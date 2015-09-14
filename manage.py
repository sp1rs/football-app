from flask import Flask,render_template,request
import requests
import json
import ast
app = Flask(__name__)



def json_file_to_dict(_file):
        config = None
        config_file = open(_file)
        config = json.load(config_file)
        return config
config = json_file_to_dict('config.json')

header = {'X-Auth-Token': config["X-Auth-Token"]}

@app.route('/')
def hello():
    r = requests.get('http://api.football-data.org/alpha/soccerseasons' , headers= header)
    data = json.loads(dict(vars(r))['_content'])
    return render_template('season.html',data=data)

@app.route('/season',methods=['POST'])
def season():
    name = request.form['cars']
    name = ast.literal_eval(name)
    r = requests.get(name['href'], headers = header)
    r = json.loads(r.content)
    data = r['teams']
    return render_template('team.html',data=data)

@app.route('/team',methods=['POST','GET'])
def team():
    name = request.form['cars']
    r = requests.get(name , headers = header)
    r = json.loads(r.content)
    r = r['fixtures']
    data = r
    return render_template('fixture.html',data=data)


if __name__=='__main__':
    app.run(debug=True)
