from flask import Flask
from config import config
app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object(config)



from app import routes

