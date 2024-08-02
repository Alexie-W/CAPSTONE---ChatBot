# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionCustomResponse (Action):
    def name(self) -> str:
        return "custom_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'greeting':
            dispatcher.utter_message(template="utter_greeting")
        elif intent == 'farewell':
            dispatcher.utter_message(template="utter_farewell")
        elif intent == 'question':
            dispatcher.utter_message(template="utter_question")
        else:
            dispatcher.utter_message(text="I'm here to help. Please let me know how I can assist you.")
        return []

