# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
#from rasa_sdk import Action, Tracker
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
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet

class ActionSuggest478breathing(Action):
    def name(self):
        return "action_suggest_478breathwork"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Try the 4-7-8 breathing technique: Inhale for 4s, hold for 7s, exhale for 8s.")
        return []

class ActionSuggestboxbreathing(Action):
    def name(self):
        return "action_suggest_boxbreathing"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Try this box breathing technique: Inhale for 4s, hold for 4s, exhale for 4s and hold for 4s.")
        return []
    
class ActionSuggestAbdombinalbreathing(Action):
    def name(self):
        return "action_suggest_boxbreathing"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Pay close attention to the movement of your abdomen and breath as you breathe deeply, filling your body with air.")
        return []

