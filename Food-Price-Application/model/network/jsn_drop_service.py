import requests  # HTTP library for requests
import json  # Encoding library


class jsnDrop(object):
    """
    Json drop class
    """

    def __init__(self, tok=None, url=None) -> None:
        # Set initial variables
        self.tok = tok
        self.url = url
        self.jsnStatus = ""
        self.jsnResult = {}

        # Data structures for storing JsnDrop Commands
        self.decode = json.JSONDecoder().decode
        self.encode = json.JSONEncoder().encode

        # Instantiate attributes of jsnDrop
        self.jsnDropRecord = self.decode('{"tok":"","cmd":{}}')
        self.jsnDropCreate = self.decode('{"CREATE":"aTableName","EXAMPLE":{}}')
        self.jsnDropStore = self.decode('{"STORE":"aTableName","VALUE":[]}')
        self.jsnDropAll = self.decode('{"ALL":"aTableName"}')
        self.jsnDropSelect = self.decode('{"SELECT":"aTableName","WHERE":"aField = b"}')
        self.jsnDropDelete = self.decode('{"DELETE":"aTableName","WHERE":"aField = b"}')
        self.jsnDropDrop = self.decode('{"DROP":"aTableName"}')

    # Functions for calling the functionality of jsnDrop
    def jsnDropApi(self, command):
        api_call = self.jsnDropRecord
        api_call["tok"] = self.tok
        api_call["cmd"] = command
        payload = {'tok': self.encode(api_call)}

        # Request to the API (Synchronous)
        r = requests.get(self.url, payload)

        # Update
        jsnResponse = r.json()
        self.jsnStatus = jsnResponse["JsnMsg"]
        self.jsnResult = jsnResponse["Msg"]

        # Feedback
        print(f"Status = {self.jsnStatus} , Result = {self.jsnResult}")
        return self.jsnResult

    def create(self, table_name, example):
        command = self.jsnDropCreate
        command["CREATE"] = table_name
        command["EXAMPLE"] = example
        return self.jsnDropApi(command)

    def store(self, table_name, value_list):
        command = self.jsnDropStore
        command["STORE"] = table_name
        command["VALUE"] = value_list
        return self.jsnDropApi(command)

    def all(self, table_name):
        command = self.jsnDropAll
        command["ALL"] = table_name
        return self.jsnDropApi(command)

    def select(self, table_name, where):
        command = self.jsnDropSelect
        command["SELECT"] = table_name
        command["WHERE"] = where
        return self.jsnDropApi(command)

    def delete(self, table_name, where):
        command = self.jsnDropDelete
        command["DELETE"] = table_name
        command["WHERE"] = where
        return self.jsnDropApi(command)

    def drop(self, table_name):
        command = self.jsnDropDrop
        command["DROP"] = table_name
        return self.jsnDropApi(command)
