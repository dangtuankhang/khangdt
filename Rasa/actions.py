# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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

# Ham lay ket qua so xo va tra ve. Ten ham la action_get_lottery
import feedparser 
from datetime import datetime
import requests


class action_get_lottery(Action):
   def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
          return 'action_get_lottery'
   def run(self, dispatcher, tracker, domain):
            # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
            url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
            # Tien hanh lay thong tin tu URL
            feed_cnt = feedparser.parse(url)
            # Lay ket qua so xo moi nhat
            first_node = feed_cnt['entries']
            # Lay thong tin ve ngay va chi tiet cac giai
            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
            # Tra ve cho nguoi dung
            dispatcher.utter_message(return_msg)
            return []


class action_get_time(Action):
   def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
          return 'action_get_time'
   def run(self, dispatcher, tracker, domain):
       now = datetime.now()
       abc = now.strftime("%d/%m/%Y %H:%M:%S")
       dispatcher.utter_message(abc)
       return []

class action_get_(Action):

   def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
          return 'action_get_google'
   def run(self, dispatcher, tracker, domain):
            # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
            url = 'https://www.google.com/search?q='            # Tien hanh lay thong tin tu URL
            link = url + 'chatbot'


            f = requests.get(link)
            return_msg = f.text[0:1000]

            # Tra ve cho nguoi dung
            dispatcher.utter_message(return_msg)
            return []