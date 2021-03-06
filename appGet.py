
import urllib
import json
import os
import re

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)



@app.route('/garryMan', methods=["GET"])
def webhook():
	req = request.get_json(silent=True, force=True)

	print("Request:")
	print(json.dumps(req, indent=4))

	res = makeWebhookResult(req)

	res = json.dumps(res, indent=4)
	print(res)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r

def makeWebhookResult(req):

	print(req.get("result").get("action"))
	if req.get("result").get("action") == "something":
		'''result = req.get("result")
		parameters = result.get("parameters")
		book = parameters.get("title")
		'''
		return {"speech": "speech","displayText": "speech","source": "python_stubot"}
		#"data": {},
		# "contextOut": [],
		



if __name__ == '__main__':

	port = int(os.getenv('PORT', 5000))
	print("Starting")
	app.run(debug=True, port=port, host='0.0.0.0')
