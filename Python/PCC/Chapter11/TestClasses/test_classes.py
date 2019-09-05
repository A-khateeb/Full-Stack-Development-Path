"""
assertEqual(a,b) a == b
assertNotEqual(a,b) a != b
assertTrue(x) x is true
assertFalse(x) x is false
assertIn(item, list) item is in the list
assertNotIN(item, list) item is not in the list
"""

import unittest
from classes import AnonymousSurvey

class TestAnonSurvey(unittest.TestCase):

    def setUp(self):
        question = "What languages did you first learn to speak"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English","Spanish","Arabic"]

    def test_store_single_response(self):
        # question = "What langauge did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response("English")
        # self.assertIn('English', my_survey.responses)
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_three_responses(self):
        for i in self.responses:
            self.my_survey.store_response(i)
        for i in self.responses:
            self.assertIn(i, self.my_survey.responses)

unittest.main()
