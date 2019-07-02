from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd


def transform_csv(file, email_column_name):
    pass


def transform_excel(file, email_column_name):
    excel = pd.ExcelFile(file.open('r'))
    print(excel.sheet_names)
    #print(file)



@api_view(['POST'])
def service(request):
    try:
        email_column_name = request.data.get('email_column_name')
        file = request.FILES.get['file']
        if (file.name.split('.')[1]).lower() == 'csv':
            response = delimiter = request.data.get('delimiter')
            transform_csv(file, email_column_name)
        else:
            response = transform_excel(file, email_column_name)



        return Response({'h': 'h'}, status.HTTP_200_OK)
    except Exception as e:
        return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)


