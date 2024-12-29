from flask import Flask

app = Flask(__name__)

# Create
@app.route('/create', methods=['POST'])
def create():
    return "<h1>Create was successful</h1>"

# Read
@app.route('/read', methods=['GET'])
def read():
    return "<h1>Read was successful</h1>"

# Update
@app.route('/update', methods=['PUT'])
def update():
    return "<h1>Update was successful</h1>"

# Delete
@app.route('/delete', methods=['DELETE'])
def delete():
    return "<h1>Delete was successful</h1>"

if __name__ == '__main__':
    app.run(debug=True)
