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
            response = "Hello! How can I assist you today?"
        elif intent == 'farewell':
            response = "Goodbye! Take care."
        elif intent == 'question':
            response = "I'm sorry, I don't have the information you're looking for."
        else:
            response = "I'm here to help. Please let me know how I can assist you."

        dispatcher.utter_message(text=response)
        return []
