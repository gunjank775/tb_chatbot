from typing import Text, List, Any, Dict, Union

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk import Action
from rasa_sdk.events import SlotSet




class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_hiv_detection"

    def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        symptoms = tracker.get_slot('symptoms')
        # weight = tracker.get_slot('weight')
        # fever = tracker.get_slot('fever')
        # sweating = tracker.get_slot('sweating')
        message=""
        
        if(symptoms=="yes"):
            message="utter_ask_hiv"
        else:
            message="utter_no_tb"
        dispatcher.utter_message(response = message)

        return [SlotSet("symptoms", None)]


# class ActionSaveConversation(Action):
#     def name(self) -> Text:
#         return "action_save_conversation"

#     def run(self,
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print(tracker.events)
#         print("Conversation")
#         dispatcher.utter_message(text="Chat collected")

#         return []



