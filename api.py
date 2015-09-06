from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask import request, abort, send_file
from werkzeug import secure_filename


app = Flask(__name__)
api = Api(app)



''' API to upload content'''

# curl -X POST -H "Content-Type: multipart/form-data" -F "image0=@/home/abhay/Pictures/deep.png" -F "num_images=1" localhost:5000/upload/slideshow

class UploadAPI(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('userid', type=str)
	parser.add_argument('num_images', type=int, default=1)

	@staticmethod
	def checkimage(imagefile):
		return True

	@staticmethod
	def checkvideo(videofile):
		return True

	def post(self, filetype):
		args = UploadAPI.parser.parse_args()
		print args
		# print secure_filename(f.filename), args
		if filetype not in ['image','video', 'slideshow']:
			abort(400)
		if filetype == 'image':
			f = request.files['image']
			UploadAPI.checkimage(f)
		if filetype == 'video':
			f = request.files['video']
			UploadAPI.checkvideo(f)
		if filetype == 'slideshow':
			for i in xrange(args['num_images']):
				print i, request.files['image%s' %i]
				f = request.files['image%s' %i]
				UploadAPI.checkimage(f)



		#
		# Do stuff with the uploads here inside the loop
		#
		return {'status': 'done'}


class DownloadAPI(Resource):

	def get(self, contentID):
		# Fetch resource from database and return 
		file_location = 'deep.png'
		# If the object had been serialized, use the following code and replace file_location with strIO
		# strIO = StringIO.StringIO()
  #   	strIO.write('Hello from Dan Jacob and Stephane Wirtel !')
  #   	strIO.seek(0)

		return send_file(file_location)


class AdvertAPI(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('userid', type=str)
	parser.add_argument('type', type=str, default=1)
	parser.add_argument('contentid', type=str)

	def get(self):
		args = AdvertAPI.parser.parse_args()
		## Get form data and return a json object
		return {'property1': 'value1'}

	def post(self):
		args = AdvertAPI.parser.parse_args()
		# Write this stuff to db and return advertid
		return {'advertid' : 'xxxxx'}

	def put(self):
		args = AdvertAPI.parser.parse_args()
		# Update db where advertid is args['advertid']

	def delete(self):
		# Delete advertisement corresponding to advertid
		pass

class UserAPI(Resource):
	def get(self):
		return {'logged_in': 'false'}


class UserAdvertsAPI(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('userid',type=str,required=True)
	parser.add_argument('max_adverts', type=int)

	def get(self):
		args = UserAdvertsAPI.parser.parse_args()
		# Get advertids posted by user
		return {'userid': args['userid'], 'advertid_list' : '1,2,3,4,5'}


# Get user data like remaining budget, number of advertisements, location, etc
class UserInfoAPI(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('userid',type=str,required=True)

	def get(self):
		args = UserInfoAPI.parser.parse_args()
		# Get data here
		return {'remaining_budget': 500, 'num_adverts_active' : 10}


class AdvertApproximateCostAPI(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('location',type=str)
	parser.add_argument('radius',type=str)
	parser.add_argument('start_date',type=str)
	parser.add_argument('end_date',type=str)
	parser.add_argument('age_start',type=int)
	parser.add_argument('age_end',type=int)
	parser.add_argument('budget',type=int)

	def get(self):
		args = AdvertApproximateCostAPI.parser.parse_args()
		# Calculate approximate cost of advertisement 
		return {'num_hours' : 5}


if __name__ == '__main__':
	app.run(debug=True)