# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from rasa_sdk.forms import FormAction
from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted


class ActionGreetUser(Action):
    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_greet', tracker)
        return [UserUtteranceReverted()]


class SalesForm(FormAction):
    def name(self):
        return "sales_form"

    @staticmethod
    def required_slots(tracker):
        return ['job_function', 'use_case', 'budget', 'person_name', 'company', 'business_email']

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Thanks for getting in touch, we’ll contact you soon')
        return []
