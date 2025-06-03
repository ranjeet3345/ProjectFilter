from django.test import TestCase
from .ai_classifier import classify_message

class ClassifierTest(TestCase):
    def test_classify(self):
        label = classify_message("Can I apply for a loan?")
        self.assertIn(label, ['loan query', 'repayment', 'irrelevant'])
