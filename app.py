from flask import Flask, request, jsonify
from flask_cors import CORS
import dialogflow_v2 as dialogflow
import os


app = Flask(__MentalFriend__)
CORS(app)


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_dialogflow_service_account.json"
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "your-dialogflow-project-id"