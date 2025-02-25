from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest
class test_sentiment_analyzer(unittest.TestCase):
    def test1(self):
        self.assertEqual(sentiment_analyzer('I love working with Python')['label'], 'SENT_POSITIVE' )
        self.assertEqual(sentiment_analyzer('I hate working with Python')['label'], 'SENT_NEGATIVE' )
        self.assertEqual(sentiment_analyzer('I am neutral on Python')['label'], 'SENT_NEUTRAL' )

unittest.main()