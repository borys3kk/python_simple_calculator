import requests

class ApiHandler:
    def __init__(self):
        
        with open("api-wolfram.txt") as f:
            self.APP_ID = f.read()
        self.APP_ENDPOINT = "http://api.wolframalpha.com/v2/query"
        self.params = {
            'input' : 'x',
            'appid' : self.APP_ID,
            'format': 'image',
            'output': 'json',
            'width' : 700
        }

    def get_new_image(self, function_to_get):
        self.params['input'] = function_to_get

        with requests.get(self.APP_ENDPOINT ,params=self.params, stream=True) as response:
            try: 
                data = response.json()
            except response.status_code != 200:
                return("somethings not quite right response")
            try:
                function_image_link = data['queryresult']['pods'][1]['subpods'][0]['img']['src']
                print(function_image_link) 
            except KeyError:
                return("somethings not quite right func image link")
        with requests.get(function_image_link) as response:
            with open('function_image.png', 'wb') as f:
                f.write(response.content)