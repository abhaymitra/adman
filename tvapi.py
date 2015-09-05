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
		# Save it in db 
		# Return latest configuration
		# schedule is for weekday and weekend
		return {'max_active_adverts': 5, 'default_countdown' : 10, 'schedule': [(9,18), (10,21)]}



class ServerFetchAdvertsAPI(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('screenid',type=str,required=True)
	parser.add_argument('num_free_slots',type=int,required=True)

	def get(self):
		# Results from the scheduler should be maintained in a hash table indexed by screenid. 
		# When the server calls this function, we get the value corresponding to its id and return new advertids
		return {'advert_list' : [{'metadata': {'countdown': 15}, 'contentId': 4}, {'metadata': {'countdown': 15}, 'contentId': 9}, {'metadata': {'countdown': 15}, 'contentId': 11}]}



api.add_resource(ServerPollAPI, '/poll')
api.add_resource(ServerFetchAdvertsAPI, '/fetch')

if __name__ == '__main__':
	app.run(debug=True,port=5001)