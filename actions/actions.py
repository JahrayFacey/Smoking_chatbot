from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from datetime import datetime
import time
import openai
import random


class ActionCompleteIntroForm(Action):
    def name(self):
        return "action_complete_intro_form"
    def run(self, dispatcher, tracker: Tracker, domain):
        name = tracker.get_slot("name")

        dispatcher.utter_message(
            text=f"Thank you {name}! It's great to meet you. As said earlier, my name is paul and just like you struggled with smoking for a long time.")
        dispatcher.utter_message(
            text="It took me a while to finally conquer my addiction, but now I want to help people like you. Believe me this step you're taking will be worth it in the end."
        )
        return [SlotSet("completed_form", True)]

class ActionSetCommitment(Action):
    def name(self):
        return "action_set_commitment"
    def run(self, dispatcher, tracker: Tracker, domain):
        dispatcher.utter_message(text = "Perfect. Just type it in. An example of a commitment could be to not smoke for 1 week.")
        commitment_text = tracker.latest_message.get("text")
        dispatcher.utter_message(text="Perfect. I will be sure to remind you.")
        return(SlotSet("commitment", commitment_text))
    
class ActionDispatchBreathingActivity(Action):
    def name(self):
        return "action_dispatch_breathing_activity"
    
    def run(self, dispatcher, tracker, domain):
        activity_type = tracker.get_slot("activity_type")
        if activity_type == "abdominal breathing":
            return [FollowupAction("action_abdominal_breathing")]
        elif activity_type == "4-7-8 breathing" or "478 breathing":
            return [FollowupAction("action_four_seven_eight_breathing")]
        elif activity_type == "Box breathing":
            return [FollowupAction("action_box_breathing")]
        else:
            dispatcher.utter_message("Sorry, I don't know that activity.")
            return []

class ActionAbdominalBreathing(Action):
    def name(self) -> Text:
        return "action_abdominal_breathing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's try abdominal breathing. Place one hand on your chest and the other on your belly.")
        dispatcher.utter_message(text="Inhale slowly and deeply through your nose, feeling your belly rise more than your chest.")
        dispatcher.utter_message(text="Exhale slowly through your mouth, feeling your belly fall.")
        dispatcher.utter_message(text="Continue this for a few minutes, focusing on your breath.")
        dispatcher.utter_message(text="How do you feel now?")
        return []

class ActionFourSevenEightBreathing(Action):
    def name(self) -> Text:
        return "action_four_seven_eight_breathing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's try the 4-7-8 breathing technique.")
        dispatcher.utter_message(text="First, exhale completely through your mouth, making a whooshing sound.")
        dispatcher.utter_message(text="Close your mouth and inhale quietly through your nose to a count of four.")
        dispatcher.utter_message(text="Hold your breath for a count of seven.")
        dispatcher.utter_message(text="Exhale completely through your mouth, making a whooshing sound to a count of eight.")
        dispatcher.utter_message(text="This is one breath. Now repeat the cycle three more times for a total of four breaths.")
        dispatcher.utter_message(text="Notice any changes in how you feel.")
        return []

class ActionBoxBreathing(Action):
    def name(self) -> Text:
        return "action_box_breathing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's try box breathing, also known as square breathing.")
        dispatcher.utter_message(text="Exhale completely, pushing all the air out of your lungs.")
        dispatcher.utter_message(text="Inhale slowly and deeply through your nose to a count of four.")
        dispatcher.utter_message(text="Hold your breath for a count of four.")
        dispatcher.utter_message(text="Exhale slowly through your mouth to a count of four.")
        dispatcher.utter_message(text="Hold your breath again for a count of four.")
        dispatcher.utter_message(text="Repeat this cycle for a few minutes.")
        dispatcher.utter_message(text="Take a moment to observe how you feel.")
        return []

class ActionSuggestBreathwork(Action):
    def name(self) -> Text:
        return "action_suggest_breathwork"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        techniques = ["abdominal breathing", "4-7-8 breathing", "box breathing"]
        chosen_technique = random.choice(techniques)
        dispatcher.utter_message(text=f"Let's try some breathwork. How about we do some {chosen_technique}?")
        return []
    
class ActionMindfulnessMeditation(Action):
    def name(self) -> Text:
        return "action_mindfulness_meditation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's begin mindfulness meditation.")
        dispatcher.utter_message(text="Find a comfortable position, either sitting or lying down.")
        dispatcher.utter_message(text="Close your eyes or keep them softly focused on a point in front of you.")
        dispatcher.utter_message(text="Bring your attention to your breath, noticing the sensation of each inhale and exhale.")
        dispatcher.utter_message(text="When your mind wanders, gently bring it back to your breath.")
        dispatcher.utter_message(text="Continue for a few minutes, allowing yourself to simply observe your thoughts and feelings without judgment.")
        dispatcher.utter_message(text="When you're ready, slowly open your eyes.")
        return []

class ActionProgressiveRelaxation(Action):
    def name(self) -> Text:
        return "action_progressive_relaxation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's begin progressive relaxation.")
        dispatcher.utter_message(text="Find a comfortable position.")
        dispatcher.utter_message(text="Start by tensing the muscles in your toes for 5 seconds, then release them.")
        dispatcher.utter_message(text="Move up your body, tensing and releasing each muscle group: feet, calves, thighs, buttocks, abdomen, chest, hands, arms, shoulders, neck, and face.")
        dispatcher.utter_message(text="Focus on the feeling of relaxation as you release each muscle group.")
        dispatcher.utter_message(text="Continue for a few minutes, allowing your body to fully relax.")
        return []

class ActionFocusedMeditation(Action):
    def name(self) -> Text:
        return "action_focused_meditation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's begin focused meditation.")
        dispatcher.utter_message(text="Choose a focal point, such as your breath, a candle flame, or a sound.")
        dispatcher.utter_message(text="Bring your attention to the focal point, noticing its sensations.")
        dispatcher.utter_message(text="When your mind wanders, gently bring it back to the focal point.")
        dispatcher.utter_message(text="Continue for a few minutes, maintaining your focus.")
        return []

class ActionDispatchMeditation(Action):
    def name(self):
        return "action_dispatch_meditation"
    
    def run(self, dispatcher, tracker, domain):
        meditation_type = tracker.get_slot("meditation_type")
        guided = tracker.get_slot("guided")
        if meditation_type == "mindfulness" and guided == "yes":
            return [FollowupAction("action_guided_mindfulness_meditation")]
        elif meditation_type == "focused" and guided == "yes":
            return [FollowupAction("action_guided_focused_meditation")]
        elif meditation_type == "progressive relaxation" and guided == "yes":
            return [FollowupAction("action_guided_progressive_relaxation")]
        elif meditation_type == "mindfulness" and guided == "no":
            return [FollowupAction("action_mindfulness_meditation")]
        elif meditation_type == "focused" and guided == "no":
            return [FollowupAction("action_focused_mediation")]
        elif meditation_type == "progressive relaxation" and guided == "no":
            return [FollowupAction("action_progressive_relaxation")]
        else:
            dispatcher.utter_message("Not familiar with that mediation, sorry.")
            return []


class ActionGuidedMindfulnessMeditation(Action):
    def name(self) -> Text:
        return "action_guided_mindfulness_meditation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's begin a guided mindfulness meditation.")
        dispatcher.utter_message(text="Find a comfortable position, either sitting or lying down.")
        dispatcher.utter_message(text="Close your eyes or keep them softly focused on a point in front of you. Now, inhale deeply feeling the air filling up your lungs, and exhale slowly, noticing the changes to your body")
        time.sleep(5) 
        dispatcher.utter_message(text="Now, turn your attention outwards and see if you can pick up on any sounds around you. It could be the sound of birds chirping or cars as they drive by. Don't think about it, just pick a sound and focus on it.")
        time.sleep(15)
        dispatcher.utter_message(text = "Now bring your awareness to the smells around you, perhaps you can smell food in the distance. Try not to get hungry if you do and concentrate for 15 secs.")
        time.sleep(15)
        dispatcher.utter_message(text="Now, pay attention to what you can feel. It could be the surface under you or wind breezing past your face. Or it could be something internal like your abdomen movements.")
        time.sleep(5)
        dispatcher.utter_message(text="Finally, return your attention to your breath and, without doing anything to change it, observe. Thoughts may enter, but don't judge. Just allow them to pass without engagement and carry on breathing.")
        dispatcher.utter_message(text="Sit for a couple more moments and when you're ready, gently open your eyes.")
        return []

class ActionGuidedProgressiveRelaxation(Action):
    def name(self) -> Text:
        return "action_guided_progressive_relaxation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's begin a Progresive relaxation meditation.")
        dispatcher.utter_message(text="Find a comfortable position. Close your eyes.")
        dispatcher.utter_message(text="Now. Tense your toes for five seconds. Then release. Feel the relaxation.")
        time.sleep(5)
        dispatcher.utter_message(text="Now tense your calf muscles. And hold for five seconds. And release. Feel the tension leaving your body.")
        dispatcher.utter_message(text="Continue to your stomach. And on your next inhale. Gently tense your stomach. For five seconds. And on your next exhale. Release.")
        dispatcher.utter_message(text="If your mind wanders, gently bring it back to your breath.")
        time.sleep(5)
        dispatcher.utter_message("Place your attention on your shoulders. On your next inhale. Raise your shoulders as high as you can. Almost to your ears if possible. And on your next exhale. Release.")
        dispatcher.utter_message("Next. Direct your focus to your arms and hands. On your next inhale, clench your fists. Feeling the tensions. Through up your arms. On your next exhale. Release.")
        dispatcher.utter_message("Finally, your face. Scrunch your face up and try not to look in any mirrors. For five seconds. On your next exhale. Release. Allow your whole body to feel relaxed and at peace.")       
        dispatcher.utter_message(text="Allow yourself to be fully present in this moment.")
        dispatcher.utter_message(text="When you are ready, open your eyes.")
        return []

class ActionGuidedFocusedMeditation(Action):
    def name(self) -> Text:
        return "action_guided_focused_meditation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's begin a guided focused meditation.")
        dispatcher.utter_message(text="Find a comfortable position. And see if you can find any object around you to focus on.")
        dispatcher.utter_message(text="It can be big or small, don't think about it too much.")
        time.sleep(5)
        dispatcher.utter_message(text="Once you found your object, take a few deep breaths to gently ready yourself for a few momemnts of concentration.")
        dispatcher.utter_message(text="Relax your shoulders and make your back straight.")
        dispatcher.utter_message(text="Now keep a gentle gaze on your focal point. Hone in on the details of this object. It could be the colours or the patterns. The important thing isn't to think about it, but simply to experience it. ")
        dispatcher.utter_message(text="If your mind wanders, gently bring your attention back to the focal point. The goal is to keep a quiet mind.")
        time.sleep(5)
        dispatcher.utter_message(text="You're doing great. Just maintain your focus for a couple of more seconds")     
        dispatcher.utter_message(text="Allow yourself to be fully present in this moment.")
        time.sleep(10)
        dispatcher.utter_message(text="You may now release your focus. Take a few moments to do some light stretches.")
        dispatcher.utter_message(text="Have a great day")
        return []

class ActionAskGuided(Action):
    def name(self) -> Text:
        return "action_ask_guided"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_guided")
        return []
    
class ActionHandleGuidedChoice(Action):
    def name(self) -> Text:
        return "action_handle_guided_choice"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        guided_value = tracker.get_slot("guided")
        meditation_type = tracker.get_slot("meditation_type") #get the meditation type the user previously requested.

        if guided_value and guided_value.lower() in ["yes", "guided", "yeah", "sure"]:
            if meditation_type == "mindfulness":
                return [dispatcher.utter_message(text = "starting guided mindfulness"), ActionGuidedMindfulnessMeditation().run(dispatcher,tracker,domain)]
            elif meditation_type == "progressive relaxation":
                return [dispatcher.utter_message(text = "starting guided progressive relaxation"), ActionGuidedProgressiveRelaxation().run(dispatcher,tracker,domain)]
            elif meditation_type == "focused":
                return [dispatcher.utter_message(text = "starting guided focused meditation"), ActionGuidedFocusedMeditation().run(dispatcher,tracker,domain)]
        else:
            if meditation_type == "mindfulness":
                return [dispatcher.utter_message(text = "starting unguided mindfulness"), ActionMindfulnessMeditation().run(dispatcher,tracker,domain)]
            elif meditation_type == "progressive relaxation":
                return [dispatcher.utter_message(text = "starting unguided progressive relaxation"), ActionProgressiveRelaxation().run(dispatcher,tracker,domain)]
            elif meditation_type == "focused":
                return [dispatcher.utter_message(text = "starting unguided focused meditation"), ActionFocusedMeditation().run(dispatcher,tracker,domain)]
        return []
    
class ActionChatwithGPT(Action):
    def name(self):
         return "action_chat_with_gpt"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get('text')

        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a supportive coach helping someone quit smoking."},
                {"role": "user", "content": user_message}
            ]
        )

        gpt_reply = response['choices'][0]['message']['content']
        dispatcher.utter_message(text=gpt_reply)
        return []
    
class ActionActivityGenerateWithGPT(Action):
    def name(self):
        return "action_activity_generate_with_gpt"
    
    def run(self, dispatcher, tracker, domain):
        craving_intensity = tracker.get_slot("craving_intensity")
        location = tracker.get_slot("location")

        prompt = (f"A user reported that they smoked after trying to quit."
                  f"Their craving intensity was {craving_intensity}/10 whilst they were at {location}."
                  "Suggest a healthy activity that they can do for when they are in that situation again."
        )
        
        openai.api_key = "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"
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
    )
        suggestion = response.choices[0].message['content'].strip()
        dispatcher.utter_message(text = suggestion)
        return []


class MilestoneAchieved(Action):

    def name(self) -> Text:
        return "milestone_achieved"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):

        
        quit_date = tracker.get_slot("smoking_progress")
        smoking_progress = datetime.striptime(quit_date, "%m - %d").date()
        days = (datetime.now().date() - smoking_progress).days

        milestones = {
            1: "utter_milestone_day_1",
            2: "utter_milestone_day_2",
            3: "utter_milestone_day_3",
            4: "utter_milestone_day_4",
            5: "utter_milestone_day_5",
            6: "utter_milestone_day_6",
            7: "utter_milestone_day_7",
            8: "utter_milestone_day_8",
            9: "utter_milestone_day_9",
            10: "utter_milestones_day_10",
            11: "utter_milestones_day_11",
            12: "utter_milestone_day_12",
            13: "utter_milestone_day_13",
            14: "utter_milestone_day_14",
            15: "utter_milestone_day_15",
            16: "utter_milestone_day_16",
            17: "utter_milestone_day_17",
            18: "utter_milestone_day_18",
            19: "utter_milestone_day_19",
            20: "utter_milestone_day_20",
            21: "utter_milestone_day_21",
            22: "utter_milestone_day_22",
            23: "utter_milestone_day_23",
            24: "utter_milestone_day_24",
            25: "utter_milestone_day_25",
            26: "utter_milestone_day_26",
            27: "utter_milestone_day_27",
            28: "utter_milestone_day_28",
            30: "utter_milestone_day_30",
            90: "utter_milestone_day_90",
            180: "utter_milestone_day_180",
            365: "utter_milestone_day_365",
        }

        response = milestones.get(days)
        dispatcher.utter_message(response = response)
        return []
    
