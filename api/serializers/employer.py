from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from core.serializers import CustomModelSerializer

from api.documents import EmployerDocument
from api.models import Employer

__all__ = ['EmployerSerializer', 'EmployerDocumentSerializer']

class EmployerSerializer(CustomModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'

class EmployerDocumentSerializer(DocumentSerializer):

    class Meta:
        document = EmployerDocument
        fields = '__all__'

    