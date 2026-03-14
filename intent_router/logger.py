import json

LOG_FILE = "route_log.jsonl"

def log_route(intent, confidence, message, response):

    entry = {
        "intent": intent,
        "confidence": confidence,
        "message": message,
        "response": response
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")