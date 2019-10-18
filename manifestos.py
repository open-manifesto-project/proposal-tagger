import requests

from settings import \
        FILTER_MANIFESTOS_BY, \
        OMP_API_URL, \
        OMP_API_MANIFESTOS_METHOD



class ManifestosManager:

    def __init__(self):
        self.__manifestos = self.__load_manifestos()

    def get_manifestos(self):
        return self.__manifestos

    def __load_manifestos(self):
        response = requests.get(
                '{}/{}'.format(OMP_API_URL, OMP_API_MANIFESTOS_METHOD),
                params=FILTER_MANIFESTOS_BY
                )
        return response.json()
