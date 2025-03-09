from flask import Flask, jsonify
from backend.server.llm.llm_handler import filter_event, prioritize_event

app = Flask(__name__)

@app.route("/")
def entry():
    response = {"message": "Server is up and running"}
    return jsonify(response), 200 

app.add_url_rule("/filter/<int:crowdsource_event_id>", view_func=filter_event, methods=['GET'])
app.add_url_rule("/prioritize/<int:filtered_event_id>", view_func=prioritize_event, methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True)