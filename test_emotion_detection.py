import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I love this!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I am really angry at this!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = emotion_detector("I am really scared about this")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
