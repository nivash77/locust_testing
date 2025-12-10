from locust import HttpUser, task, between
import  json
import time
import os
from dotenv import load_dotenv

load_dotenv()
APIKEY=os.get('Apikey')
URL=os.getenv('url')
class APILoadTest(HttpUser):
    wait_time = between(1, 2)

    def on_start(self) :
        with open("payload.json","r") as f:
            self.payload = json.load(f)

    @task
    def call_once(self):
        print(f"API request Time:{time.strftime('%H:%M:%S')}")
        response=self.client.post(URL,headers={"Apikey":APIKEY,"Content-Type":"application/json"},json=self.payload)
        print(response.status_code)
        print(f"API completed Time:{time.strftime('%H:%M:%S')}")
        self.environment.runnner.quit()




