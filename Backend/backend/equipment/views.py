import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dataset

@api_view(['POST'])
def upload_csv(request):
    file = request.FILES.get('file')
    df = pd.read_csv(file)

    summary = {
        "total_equipment": len(df),
        "avg_flowrate": df['Flowrate'].mean(),
        "avg_pressure": df['Pressure'].mean(),
        "avg_temperature": df['Temperature'].mean(),
        "type_distribution": df['Type'].value_counts().to_dict()
    }

    Dataset.objects.create(file=file, summary=summary)

    if Dataset.objects.count() > 5:
        Dataset.objects.first().delete()

    return Response(summary)
