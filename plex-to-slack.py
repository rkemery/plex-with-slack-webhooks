from flask import Flask, request, jsonify
import requests
import argparse
import logging
import json

app = Flask(__name__)

SLACK_WEBHOOK_URL = ''  # Replace with your Slack Webhook URL

EVENT_MESSAGES = {
    "library.on.deck": "added a new item to their On Deck.",
    "library.new": "added a new item to a library they have access to.",
    "media.pause": "paused",
    "media.play": "started playing",
    "media.rate": "rated",
    "media.resume": "resumed playback of",
    "media.scrobble": "viewed (played past the 90% mark)",
    "media.stop": "stopped playing",
    "admin.database.backup": "completed a database backup via Scheduled Tasks.",
    "admin.database.corrupted": "detected corruption in the server database.",
    "device.new": "accessed the owner's server.",
    "playback.started": "started playback as a shared user for the server."
}

@app.route('/plex-webhook', methods=['POST'])
def plex_webhook():
    # Check if the payload is JSON or form-data
    if request.content_type == 'application/json':
        payload = request.json
    else:
        # Parse the JSON part of the multipart/form-data
        payload = json.loads(request.form['payload'])

    event_type = payload.get('event')
    user_title = payload['Account'].get('title')
    media_title = payload['Metadata'].get('title', 'an item')  # Default to 'an item' if title is not present
    player_title = payload['Player'].get('title')

    # Construct the message based on the event type
    message = f"User {user_title} {EVENT_MESSAGES.get(event_type, 'performed an action')} {media_title} on {player_title}."

    # Send message to Slack
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json={"text": message})
        response.raise_for_status()
        return jsonify({"message": "Notification sent to Slack."}), 200
    except requests.RequestException as e:
        logging.error(f"Error sending to Slack: {e}")
        return jsonify({"message": "Error sending to Slack."}), 500

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Plex to Slack notification server.")
    parser.add_argument('-verbose', action='store_true', help="Enable detailed logging.")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    app.run(host='0.0.0.0', port=3000)
