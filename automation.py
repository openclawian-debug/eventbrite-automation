#!/usr/bin/env python3
"""Eventbrite Automation - Auto-reserve tickets"""

import requests
from datetime import datetime

class EventbriteAutomation:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://www.eventbriteapi.com/v3"
    
    def search_events(self, query, location="Manila"):
        endpoint = f"{self.base_url}/events/search/"
        params = {"q": query, "location.address": location}
        response = requests.get(endpoint, headers={"Authorization": f"Bearer {self.api_token}"}, params=params)
        return response.json()
    
    def reserve_ticket(self, event_id, ticket_type_id, quantity=1):
        endpoint = f"{self.base_url}/orders/"
        data = {"event_id": event_id, "tickets": [{"ticket_class_id": ticket_type_id, "quantity": quantity}]}
        response = requests.post(endpoint, headers={"Authorization": f"Bearer {self.api_token}"}, json=data)
        return response.json()

if __name__ == "__main__":
    print(f"Eventbrite Automation Ready - {datetime.now()}")
