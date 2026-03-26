# Emotion Detector

A Flask web application that uses IBM Watson NLP to detect emotions in text.

## Features

- Detects 5 emotions: anger, disgust, fear, joy, sadness
- Returns the dominant emotion
- Error handling for blank/invalid input (HTTP 400)
- REST API endpoint + simple web UI

## Setup

```bash
pip install flask requests
```

## Run

```bash
python server.py
```

Then open [http://localhost:5000](http://localhost:5000)

## API

```
GET /emotionDetector?textToAnalyze=I+love+this
```

Response:
```
For the given statement, the system response is 'anger': 0.012, 'disgust': 0.008, 'fear': 0.009, 'joy': 0.923 and 'sadness': 0.049. The dominant emotion is joy.
```

## Tests

```bash
python -m unittest test_emotion_detection.py
```
