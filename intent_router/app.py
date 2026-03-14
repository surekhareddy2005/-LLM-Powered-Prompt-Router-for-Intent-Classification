from classifier import classify_intent 
from router import route_and_respond
from logger import log_route


def main():

    print("LLM Prompt Router")
    print("Type 'exit' to quit\n")

    while True:

        message = input("Enter message: ")

        if message.lower() == "exit":
            break

        # Manual override
        if message.startswith("@code"):
            intent_data = {"intent": "code", "confidence": 1.0}
            message = message.replace("@code", "").strip()

        elif message.startswith("@data"):
            intent_data = {"intent": "data", "confidence": 1.0}
            message = message.replace("@data", "").strip()

        elif message.startswith("@writing"):
            intent_data = {"intent": "writing", "confidence": 1.0}
            message = message.replace("@writing", "").strip()

        elif message.startswith("@career"):
            intent_data = {"intent": "career", "confidence": 1.0}
            message = message.replace("@career", "").strip()

        else:
            intent_data = classify_intent(message)

        intent = intent_data["intent"]
        confidence = intent_data["confidence"]

        print("\nDetected Intent:", intent)
        print("Confidence:", confidence)

        response , final_intent= route_and_respond(message, intent_data)

        print("\nResponse:\n", response)

        log_route(final_intent, confidence, message, response)

        print("\nRequest logged.\n")


if __name__ == "__main__":
    main()