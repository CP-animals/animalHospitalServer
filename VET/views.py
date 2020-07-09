from rest_framework.response import Response
from rest_framework.decorators import api_view
from VET.models import Data
from VET.serializers import DataSerializer
# Create your views here.

@api_view(['GET'])
def dataVet(request):
    queryset = Data.objects.all()
    serializer = DataSerializer(queryset, many=True)
    return Response(serializer.data)