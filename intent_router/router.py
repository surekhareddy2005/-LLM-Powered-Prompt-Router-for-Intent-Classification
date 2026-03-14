from groq import Groq
from prompts import PROMPTS

client = Groq()

CONFIDENCE_THRESHOLD = 0.7

def route_and_respond(message, intent_data):

    intent = intent_data["intent"]
    confidence = intent_data["confidence"]

    if confidence < CONFIDENCE_THRESHOLD:
        intent = "unclear"

    if intent == "unclear":
        return "Could you clarify whether you need help with coding, writing, data analysis, or career advice?"

    system_prompt = PROMPTS[intent]

    response = client.chat.completions.create(
       model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content,intent