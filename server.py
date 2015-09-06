from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask import request, abort, send_file, render_template

from tvapi import ServerPollAPI, ServerFetchAdvertsAPI
from api import UserAPI, UserInfoAPI, UserAdvertsAPI, UploadAPI, DownloadAPI, AdvertAPI, AdvertApproximateCostAPI

app = Flask(__name__)
api = Api(app)

## API for clients
api.add_resource(UserAPI,'/user')
api.add_resource(UserInfoAPI, '/user/info')
api.add_resource(UserAdvertsAPI,'/user/adverts')
api.add_resource(UploadAPI, '/upload/<string:filetype>')
api.add_resource(DownloadAPI, '/download/<string:contentID>')
api.add_resource(AdvertAPI, '/adverts')
api.add_resource(AdvertApproximateCostAPI, '/advert/approx')


## API for screens
api.add_resource(ServerPollAPI, '/poll')
api.add_resource(ServerFetchAdvertsAPI, '/fetch')

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/new")
def new_advert():
	return render_template('new_advert.html')

if __name__ == '__main__':
	app.run(debug=True)