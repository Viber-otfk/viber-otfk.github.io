from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='PythonSampleBot',
	avatar='https://viber.com/avatar.jpg',
	auth_token='YOUR_AUTH_TOKEN_HERE'
)
viber = Api(bot_configuration)

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/incoming', methods=['POST'])
def incoming():
	logger.debug("received request. post data: {0}".format(request.get_data()))
	# handle the request here
	return Response(status=200)

context = ('server.crt', 'server.key')
app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)

viber.set_webhook('https://mybotwebserver.com:443/')