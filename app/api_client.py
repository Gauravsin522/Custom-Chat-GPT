import os
import openai  # type: ignore
from logger import Customlogger

class OpenAIClient:
    """Class to interact with OpenAI Client"""
    
    def __init__(self):
         self.api_key = os.getenv("API_KEY") # Get the actual API key from environment
         self.clent = openai.OpenAI(api_key = self.api_key)
         self.logger = Customlogger().get_logger() # Initialize your Custom logger

    def get_response(self,messages):
        """
        Send messages to thr OpenAI API and return the response.
        
        :param messages: List of messages for the conversation.
        :return AI response as a string.
        """
        
        try:
            self.logger.info("Sending message to the OpenAI API...")
            
            # Invoking the openai api and soring the response.
            chat_completion = self.client.chat.completions.create(
                messages = messages,
                model = "gpt-3.5-turbo"
            )
            response = chat_completion.choices[0].message.content
            
            self.logger.info("Received response from Open AI")
            
            return response
        except Exception as e:
            self.logger.error(f"Error communication with openai API : {e}")
            return "Sorry, I couldn't get a response at this time."