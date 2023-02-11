from flask import Flask, redirect, request
from msal import PublicClientApplication
import json, logging, requests, os, sys

CONFIG_FILE = 'parameters.json'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/loggedin')
def logged_in():
    return 'We have logged in'

@app.route('/authdone')
def auth_done():
    print(request.headers)
    return 'your are authenticated'

# get settings from config file
config = json.load(open(CONFIG_FILE))

@app.route('/token')
def token():
    logging.info('starting the process \n')
    app.logger.info("starting the process \n")
    authapp = PublicClientApplication(
    config["client_id"], authority=config["authority"])

    # The pattern to acquire a token looks like this.
    result = None

    # app.getaccounts()
    accounts = authapp.get_accounts()
    if accounts:
        # If so, you could then somehow display these accounts and let end user choose
        print("Pick the account you want to use to proceed:", file=sys.stderr)
        app.logger.info("Pick the account you want to use to proceed:")
        for a in accounts:
            print(a["username"])
        # Assuming the end user chose this one
        chosen = accounts[0]
        result = authapp.acquire_token_silent(["https://graph.microsoft.com/.default"], account=chosen)

    if not result:
        result = authapp.acquire_token_interactive(["https://graph.microsoft.com/.default"])
    if "access_token" in result:
        # print(result["access_token"])
        app.logger.info(result["access_token"])
    else:
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))  # You may need this when reporting a bug

    # return result["access_token"]
    return redirect('http://localhost:5000/authdone')

#run server
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)