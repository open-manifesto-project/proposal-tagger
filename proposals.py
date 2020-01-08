import requests
import json
from slugify import slugify

from tagger import Tagger
from settings import \
        OMP_API_URL, \
        OMP_API_MANIFESTOS_METHOD, \
        OMP_API_PROPOSALS_METHOD, \
        TAGGER_BY


class ProposalsManager:

    def __init__(self, manifestos):
        self.__proposals = self.__load_proposals(manifestos)

    def get_proposals(self):
        return self.__proposals

    def __load_proposals(self, manifestos):
        proposals = list()
        i = 1
        total = len(manifestos)
        for manifesto in manifestos:
            print("Recuperando manifesto {} de {}".format(i, total))
            manifesto_ext = requests.get(
                    '{}/{}/{}'.format(OMP_API_URL, OMP_API_MANIFESTOS_METHOD, manifesto['id'])
                    ).json()
            for proposal in manifesto_ext['proposals']:
                proposals.append({
                    'political_party': manifesto_ext['political_party'],
                    'election_type': manifesto_ext['election_type'],
                    'geographical_area': manifesto_ext['geographical_area'],
                    'proposal': proposal['body'],
                    'topics': [],
                    'tags': []
                    })
            i = i + 1
        return proposals

    def export(self, filter_by=''):
        proposals = [p for p in self.__proposals if filter_by in p['topics']]
        proposals_exported = list()
        for proposal in proposals:
            proposal_copy = proposal.copy()
            proposal_copy['topics'] = filter_by
            proposal_copy['tags'] = [
                    t['tag']
                    for t in proposal['tags']
                    if t['topic'] == filter_by
                    ]
            proposals_exported.append(proposal_copy)
        file_output = open(slugify(filter_by)+'.json', 'w')
        file_output.write(
                json.dumps(
                    proposals_exported,
                    ensure_ascii=False,
                    indent=4)
                )
        file_output.close()


    def tag(self):
        tagger = Tagger()
        i = 1
        total = len(self.__proposals)
        for proposal in self.__proposals:
            print("Etiquetando propuesta {} de {}".format(i, total))
            tagger.load_content(proposal['proposal'])
            tagger.tag()
            proposal['topics'] = tagger.get_topics()
            proposal['tags'] = tagger.get_tags()
            i = i + 1
