from flask import Flask, Response
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes


@app.route("/gcode/<int:design_id>")
def get_gcode(design_id):
    filepath = os.path.join("gcode", f"{design_id}.json")
    if not os.path.exists(filepath):
        return {"error": "Design not found"}, 404
    with open(filepath, "r") as f:
        gcode_data = f.read()  # read as plain text
    return Response(gcode_data, mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True)
