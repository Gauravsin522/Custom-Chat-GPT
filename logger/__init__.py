import logging
from datetime import datetime
import os

# Create a directory for logs if it doesn't exist
class Customlogger:
    """
    custom logger class to hanldle the loggingwith with timestamp to file
    """
    
    def __init__(self):
        # Define the directory for logs files
        self.log_dir = "logs"
        
        # Create the directory if it doesn't exist
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Create a timestamped log file name 
        current_time_stamp = f"{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}"
        
        # define the log file name with timestamp
        self.log_file_name = f"log_{current_time_stamp}.log"
        
        # Define the full path for the log file
        self.log_file_path = os.path.join(self.log_dir,self.log_file_name)
        
        # Set up basic logging configration
        logging.basicConfig(
            filename = self.log_file_path,
            filemode = "a", # Use "a" for appending to existing logs instead overwriting
            format = '[%(asctime)s %(name)s - %(levelname)s - %(message)s]',
            level = logging.INFO
        )
        
        self.logger = logging.getLogger(__name__)
        
    def get_logger(self):
        """ Return the configured logger instance"""
        return self.logger
    