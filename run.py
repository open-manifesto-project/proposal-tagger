from manifestos import ManifestosManager
from proposals import ProposalsManager
from settings import TAGGER_BY


if __name__ == '__main__':
    manifestos = ManifestosManager().get_manifestos()
    proposals_manager = ProposalsManager(manifestos)
    proposals_manager.tag()
    for topic in TAGGER_BY:
        proposals_manager.export(filter_by=topic)
