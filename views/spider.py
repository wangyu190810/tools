from base import BaseHandler
from model.spider import get_chouti_index
import json

base_url = r"/spider/"

class ChoutiSpiderIndex(BaseHandler):
    
    def get(self):
        data = get_chouti_index()
        self.write(json.dumps(data))

        # self.write(json.dumps(data))


spider_handler = [
    (base_url +  r"chouti/index",ChoutiSpiderIndex),
]

