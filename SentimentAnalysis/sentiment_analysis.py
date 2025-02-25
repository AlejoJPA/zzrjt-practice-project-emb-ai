'''This module performs NLP - Sentiment Analysis using BERT
'''
import json
import requests  # Import the requests library to handle HTTP requests

def sentiment_analyzer(text_to_analyse):
    '''analyzer
    '''
    # URL of the sentiment analysis service
    url = (
    "https://sn-watson-sentiment-bert.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Default values for label and score (to prevent 'possibly-used-before-assignment' error)
    label = "Unknown"
    score = 0.0

    try:
        # Send a POST request to the API with the text and headers
        response = requests.post(url, json=myobj, headers=header, timeout=10)

        # Parse the JSON response
        formatted_response = json.loads(response.text)

        if response.status_code == 200:
            label = formatted_response.get('documentSentiment', {}).get('label', "Unknown")
            score = formatted_response.get('documentSentiment', {}).get('score', 0.0)

        elif response.status_code == 500:
            label = None
            score = None

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")  # Log error for debugging

    return {'label': label, 'score': score}
