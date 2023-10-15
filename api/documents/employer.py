from django_elasticsearch_dsl import Document, fields

from django_elasticsearch_dsl.registries import registry
from api.models import Employer

__all__ = ['EmployerDocument']


@registry.register_document
class EmployerDocument(Document):

    class Index:
        # Name of the Elasticsearch index
        name = 'employers'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Employer # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id',
            'rank',
            'company',
            'industries',
            'country_territory',
            'employees',
            'publish_year'
        ]