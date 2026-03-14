import json
from groq import Groq

client = Groq()

CLASSIFIER_PROMPT = """
You are an intent classifier.

Classify the user message into one of these labels:

code
data
writing
career
unclear

Return ONLY a JSON object like this:

{
 "intent": "code",
 "confidence": 0.92
}
"""

def classify_intent(message):

    try:

        response = client.chat.completions.create(
           model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": CLASSIFIER_PROMPT},
                {"role": "user", "content": message}
            ]
        )

        text = response.choices[0].message.content.strip()

        print("MODEL OUTPUT:", text)   # debug line

        result = json.loads(text)

        return result

    except Exception as e:

        print("Error parsing response:", e)

        return {
            "intent": "unclear",
            "confidence": 0.0
        }