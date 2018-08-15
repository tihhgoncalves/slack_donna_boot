import os 
import requests 
from flask import Flask 
from flask import request

app = Flask(__name__)

slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')

@app.route("/", methods=['POST', ]) 
def webhook():

action = request.json['action'] 
release = request.json['release'] 
repository = request.json['repository']

slack_data = { 
 "text": "A new release from *{repo_name}* was {action}!\n" 
 "Click <{release_url}|Release {tag_name}> for more details".format(action=action, repo_name=repository['name'], release_url=release['url'], tag_name=release['tag_name']) 
}

response = requests.post(slack_webhook_url, json=slack_data)

if response.status_code != 200:
 raise ValueError('Request to slack returned an error {}, the response is:\n{}'.format(response.status_code, response.text))

return ""
