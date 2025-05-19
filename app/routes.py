from flask import Blueprint, render_template, request, jsonify
from app.utils import format_response
from app.chat import ChatManager

# Create a blueprint for the main application
main = Blueprint('main',__name__)

# Initialize the chatmanager
chat_manager = ChatManager()

@main.route('/')
def index():
    """ Render the chat interface"""
    return render_template("chat.html") # Renders the chat.html template

@main.route('/test')
def test():
    return render_template('base.html') # Assuming base.html exists

@main.route('/api/chat', methods = ["POST"])
def chat():
    """ Handle chat messages from users."""
    """
    request = {
        'message' : 'user promt'
    }
    """
    user_message = request.jsonn.get("message")
    
    if not user_message:
        return jsonify({'error': "no message provided"}), 400
    
    # Get AI's response using the chatmanager
    ai_response = chat_manager.get_response(user_message)
    
    # Format the response if necessart
    formatted_response = format_response(ai_response)
    
    return jsonify({'response': formatted_response}) # Return the formatted AI's response