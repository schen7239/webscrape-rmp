import requests as rq
from dotenv import load_dotenv
import os
import json

load_dotenv()
RMP_AUTHORIZATION_TOKEN = os.getenv('RMP_AUTHORIZATION_TOKEN')

headers = {"Authorization": RMP_AUTHORIZATION_TOKEN}

def write_to_json_file(file_name, data):
    file = open(file_name, "w")
    file.write(json.dumps(data))
    file.close

class GraphQLQuery:
    def __init__(self, query_items, query_url, gql_query, gql_variables,):
        self.query_items = query_items
        self.query_url = query_url
        self.gql_query = gql_query
        self.gql_variables = gql_variables
    
    def retrieve_data(self):
        teacher_data = {
            "entries": 0,
            "data": []
        }
        i = 0
        for item in self.query_items:
            variables = self.gql_variables
            variables['id'] = item['node']['id']
            req = rq.post(self.query_url, json={ "query": self.gql_query, "variables": variables }, headers=headers)
            json_teacher_data = req.json()
            teacher_data['data'].append(json_teacher_data)
            i = i + 1
            print(i)
        teacher_data['entries'] = len(teacher_data['data'])
        write_to_json_file('teacher_reviews.json', teacher_data)
        
        
            
            
        