from app import app


@app.route('/')
def hello_world():
    return "<p>Hello, World! It's ya boi</p>"
