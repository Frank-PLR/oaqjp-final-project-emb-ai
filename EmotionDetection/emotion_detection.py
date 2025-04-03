import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    try:
        #represent the raw data received in dictionary form
        text_to_analyze_dict = {"raw_document": {"text": text_to_analyze}}

        #send the request, accept all variations of success
        response = requests.post(URL, json=text_to_analyze_dict, headers=HEADERS)

        #if the return value is 200-299, let's call it good
        if response.status_code < 300:
            # Return the response from the API in text form
            resulting_emotions = response.json()

            # Extract emotions from the first prediction
            all_emotions = resulting_emotions['emotionPredictions'][0]['emotion']

            # Extract only the required emotions
            selected_emotions = {
                'anger': all_emotions.get('anger', 0),
                'disgust': all_emotions.get('disgust', 0),
                'fear': all_emotions.get('fear', 0),
                'joy': all_emotions.get('joy', 0),
                'sadness': all_emotions.get('sadness', 0)
            }

            # determine the dominant emotion
            dominant_emotion = max(selected_emotions, key=selected_emotions.get)

            json_list = {
                'anger': selected_emotions.get('anger', 0),
                'disgust': selected_emotions.get('disgust', 0),
                'fear': selected_emotions.get('fear', 0),
                'joy': selected_emotions.get('joy', 0),
                'sadness': selected_emotions.get('sadness', 0),
                'dominant_emotion': dominant_emotion
            }

            return json.dumps(json_list)

        else:
            # Return a message indicating the API did not respond as expected
            return json.dumps({"error": "requests.post error: {}".format(response.status_code)})

    except requests.exceptions.RequestException as postEx:
        # Handle any errors that occur during the request
        return json.dumps({"error": "Post failed: {}".format(postEx)})
