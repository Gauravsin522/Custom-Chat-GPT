import os
from app import create_app

print("Current working directory:", os.getcwd())

# create an instance of the Flask app

app = create_app()

if __name__ == '__main__':
    # run the application on the default port 5000
    print("Flask app is running on http://127.0.0.1.5000")
    
    app.run(host = "127.0.0.1:5000", port = 5000, debug = True)