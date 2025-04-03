from flask import Flask, request
from EmotionDetection import emotion_detector
import json

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    # Get the "text" query parameter
    text = request.args.get("text")
    
    if not text:
        return "Please provide a 'text' query parameter.", 400

    # Call your emotion detector
    result_json = emotion_detector(text)
    result = json.loads(result_json)

    # Handle errors from the emotion detector
    if "error" in result:
        return f"Error: {result['error']}", 500

    # Format the response string as per customer requirements
    response = (
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}, "
        f"'The dominant emotion is': {result['dominant_emotion']}."
    )

    return response

if __name__ == "__main__":
    #app.run(debug=True, port=5000)
    app.run(debug=True, host='0.0.0.0', port=5000)