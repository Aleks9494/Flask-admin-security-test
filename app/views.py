from app import app

@app.route('/')
def index():
    return 'Hi, Aleks'
