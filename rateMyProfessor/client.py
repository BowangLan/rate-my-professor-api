import requests
import re
from rich import print
from .constants import *
from .parsers import ProfessorDetailPageParser


headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.ratemyprofessors.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43',
    'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


class RateMyProfessorClient():
    def __init__(self, cookies: str = ""):
        self.cookies = cookies
        self.token = ""
        self.get_token()
    
    def get_token(self):
        res = requests.get(DOMAIN, headers=headers)
        token = re.findall(r'REACT_APP_GRAPHQL_AUTH\":\"(\w*)\"', res.text)[0]
        self.token = token


    @property
    def headers_with_auth(self):
        return {
            **headers,
            "Authorization": "Basic " + self.token,
            "Cookie": self.cookies,
        }

    def graphql(self, query: str, variables: dict):
        res = requests.post(
            'https://www.ratemyprofessors.com/graphql',
            headers=self.headers_with_auth,
            json={
                'query': query,
                'variables': variables
            })
        if res.text.strip() == "Unauthorized":
            return None
        return res.json()

    def search_professor(self, text: str, school_id: str = ""):
        return self.graphql(
            SEARCH_PROFESSOR,
            {
                'query': {
                    'text': text,
                    'schoolID': school_id,
                    'fallback': True,
                    'departmentID': None,
                },
                'schoolID': school_id
            })

    def get_professor_detail(self, professor_id: str):
        url = f"{DOMAIN}/professor/" + professor_id
        res = requests.get(url, headers=self.headers_with_auth)
        parser = ProfessorDetailPageParser()
        data = parser.parseHtml(res.text)
        return data
    
    def get_school_detail(self, school_id: str):
        return self.graphql(
            GET_SCHOOL_DETAIL,
            {
                'id': school_id
            })
