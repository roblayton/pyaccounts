from flask import Flask
from flask import Response, request
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo
from bson.json_util import dumps
from bson.json_util import loads

#import uuid
#id = uuid.uuid4()

app = Flask(__name__)
cors = CORS(app)
app.config['MONGO_HOST'] = 'mongodb://database'
app.config['MONGO_DBNAME'] = 'main'

# connect to the mongo db
mongo = PyMongo(app)

@app.route('/accounts', methods=['GET'])
def accounts():
  result = mongo.db.accounts.find()
  data = dumps(result)
  response = Response(data, status=200, mimetype='application/json')
  return response

@app.route('/account', methods=['GET'])
def account():
  result = mongo.db.accounts.find({"accountId": request.args.get('id')})
  data = dumps(result)
  response = Response(data, status=200, mimetype='application/json')
  return response

if __name__ == "__main__":
  app.run(host='0.0.0.0')
