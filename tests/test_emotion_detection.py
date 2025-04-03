from EmotionDetection import emotion_detector
import json

# test format == (input, expected_emotion)
test_cases = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear")
]

def test_emotion_detector_expected_outputs():
    for input_statement, expected in test_cases:
        result = emotion_detector(input_statement)
        data = json.loads(result)

        print(f"\nInput: {input_statement}")
        print(f"Expected: {expected}")
        print(f"Returned: {data.get('dominant_emotion', 'N/A')}")

        assert data.get("dominant_emotion") == expected