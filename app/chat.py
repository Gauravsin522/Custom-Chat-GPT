from app.api_client import OpenAIClient


class ChatManager:
    """
    Class to manage chat interractions.
    """
    def __init__(self):
        self.client = OpenAIClient() # Initializtion the openai client
        self.conversation_history = [] # Stores conversation history
        
    def add_message(self, role, content):
        """Add a message to the converation history."""
        self.conversation_history.append({"role": role,"content": content})
        
    def get_response(self, user_message):
        """
        Gets a concise or detailed response based on user input.
        
        :params user_message: The message input from the user.
        :return: AI response as a string.
        """
        
        # Add user's message to the history
        self.add_message("user", user_message)
        
        # Prepare messages for the API call based on user intent
        
        if any(keyword in user_message.lower() for keyword in ["what is ","define"]):
            promt = f"Provide a concise definition of : {user_message}"
            
        elif "explain" in user_message.lower() or "code" in user_message.lower():
            promt = f"Explain clearly with examples: {user_message}"
            
        else:
            promt = f"Response concise to : {user_message}"
            
        messages = [{"role":"user","content":promt}]
        
        # Get AI's response
        ai_response = self.client.get_response(messages)
        
        # Add AI's response to the history
        self.add_message("assistant",ai_response)
        
        return ai_response
        