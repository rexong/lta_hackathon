from flask import request, jsonify
from backend.schema.event_storage import EventStorage

verified_event_storage = EventStorage()

def create_event():
    """Create a new event."""
    data = request.get_json()
    timestamp = data.get('timestamp')
    town = data.get('town')
    street = data.get('street')
    congestion_level = data.get("congestion_level")
    speed = data.get("speed")
    end_node = data.get("end_node")

    if not (timestamp and town and street and congestion_level and speed and end_node):
        return jsonify({'message': 'Missing required fields'}), 400

    event_id = verified_event_storage.create(timestamp, town, street)
    return jsonify({'message': 'Event created', 'event_id': event_id}), 201


def get_event(event_id):
    """Get an event by ID."""
    event = verified_event_storage.read(event_id)
    if event:
        return jsonify(event.to_dict()), 200
    return jsonify({'message': 'Event not found'}), 404


def update_event(event_id):
    """Update an event by ID."""
    data = request.get_json()
    timestamp = data.get('timestamp')
    town = data.get('town')
    street = data.get('street')
    congestion_level = data.get("congestion_level")
    speed = data.get("speed")
    end_node = data.get("end_node")

    updated_event = verified_event_storage.update(
        event_id,
        timestamp,
        town,
        street,
        congestion_level,
        speed,
        end_node
    )
    if updated_event:
        return jsonify(updated_event.to_dict()), 200
    return jsonify({'message': 'Event not found'}), 404


def delete_event(event_id):
    """Delete an event by ID."""
    deleted_event = verified_event_storage.delete(event_id)
    if deleted_event:
        return jsonify({'message': 'Event deleted'}), 200
    return jsonify({'message': 'Event not found'}), 404


def list_events():
    """List all events."""
    events = verified_event_storage.list_events()
    return jsonify([event.to_dict() for event in events]), 200