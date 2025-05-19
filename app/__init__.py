from flask import Flask
import os
import yaml
from dotenv import load_dotenv
from config import AppConfig
from logger import Customlogger

# load environment variables from .env file
load_dotenv()

def create_app():
    """ Create and configure the Flask application"""
    app = Flask(__name__, template_folder= "templates") # Initializing the app
    
    # Load configation
    app_config = AppConfig()
    app.config.update(app_config.config)
    
    # Setup logginf
    logger = Customlogger().get_logger()
    logger.info("Flask application starting....")
    
    # Import and register routes