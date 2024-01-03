import json
import logging
import requests


from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='otfc',
	avatar='https://viber.com/avatar.jpg',
	auth_token='522858ca55a7e176-d905e96302649e2b-3434e58445298988'
)
viber = Api(bot_configuration)

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/incoming', methods=['POST'])
def incoming():
	#logger.debug("received request. post data: {0}".format(request.get_data()))
	# handle the request here
	return Response(status=200)

context = ('server.crt', 'server.key')
app.run(host='https://github.com/Viber-otfk/viber-otfk.github.io.git/from viberbot import Api.py', port=443, debug=True, ssl_context=context)

viber.set_webhook('https://mybotwebserver.com:443/')