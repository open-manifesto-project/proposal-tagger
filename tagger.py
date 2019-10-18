import requests

from settings import \
        TAGGER_API_URL


class Tagger:

    __text = ''
    __topics = None
    __tags = None

    def load_content(self, text):
        self.__text = text

    def tag(self):
        response = requests.post(
                TAGGER_API_URL,
                data={'text': self.__text}
                ).json()
        self.__topics = response['topics']
        self.__tags = response['tags']

    def get_topics(self):
        return self.__topics

    def get_tags(self):
        return self.__tags
