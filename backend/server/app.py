from flask import Flask, jsonify

from backend.server.event_handler import (
    create_event,
    get_event,
    update_event,
    delete_event,
    list_events
)

app = Flask(__name__)

@app.route("/")
def entry():
    response = {"message": "Server is up and running"}
    return jsonify(response), 200 

app.add_url_rule("/events", view_func=create_event, methods=["POST"])
app.add_url_rule("/events", view_func=list_events, methods=["GET"])
app.add_url_rule("/events/<int:event_id>", view_func=get_event, methods=["GET"])
app.add_url_rule("/events/<int:event_id>", view_func=delete_event, methods=["DELETE"])
app.add_url_rule("/events/<int:event_id>", view_func=update_event, methods=["PUT"])

if __name__ == "__main__":
    app.run(debug=True)
    