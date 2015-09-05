from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask import request, abort

app = Flask(__name__)
api = Api(app)

''' Api for screens '''

class ServerPollAPI(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('screenid',type=str,required=True)
	parser.add_argument('active_advertid',type=str,action='append')
	
	def get(self):
		args = ServerPollAPI.parser.parse_args()
		# Screen screenid is alive 
		# Current active ads on this screen are in list active_advertid
		# Save it in db and return



class ServerFetchAdvertsAPI(Resource):

	def get(self):
		



api.add_resource(ServerPollAPI, '/poll')


if __name__ == '__main__':
	app.run(debug=True,port=5001)