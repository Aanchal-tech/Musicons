import requests

class Music():

    def recommendations(self, label):
        self.auth_token = 'BQB6DiUqjCbwveUswKZuYFH6Wi0shum_NJ13VZbLcoQcQ3R8bGnYez9Lf4PWI9h7eXWZoXehRVZm6c4nisua7CXvfjis32fqDrxuohVeutM7w7isl8M-bZbpqZwdRoW2q0csLP9wGy66lYsmHGQWng3w3XZMeHVD0SgtMsSsXe502BZt-GBjIHn_KtfnxgynQpJXgiW3rhhuuy3j'
        hed = {'Authorization': 'Bearer ' + self.auth_token}
        data = {'app': 'MRBE'}

        url = 'https://api.spotify.com/v1/playlists/'
        if label == "sad":
            id = "2XlzLiYK5TGoC4ihmJYQWV"
        elif label == "happy":
            id = "0ySRSWggz1WzI9rPkQTQn9"
        elif label == "angry":
            id = "4cllWzORlvlwrhZf17mpYN"
        elif label == "neutral":
            id = "1HYAXEiPSAweKDbx8T2pGC"
        elif label == "surprised":
            id = "6zxAPdCbKbMHxULOD25qFE"
        elif label == "fear":
            id = "1cjat0l75mQgSdKzwtjKhW"
        elif label == "disgust":
            id == "2dH0S4ytsw35IL5lJSVePU"
        response = requests.get(url + id, headers=hed)
        #print(response)
        resp = response.json()
        print(resp['external_urls']['spotify'])

#temp = Music()
#temp.recommendations()
