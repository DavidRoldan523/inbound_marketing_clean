import pandas as pd
import re
import dns.resolver
import csv

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from pandarallel import pandarallel  # pip install pandarallel

pandarallel.initialize()

def verify_email(email):
    email = email.lower()
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match == None:
        return 0
    try:
        dns.resolver.query(email.split('@')[1], 'MX')
    except Exception:
        return 0
    return 1

@api_view(['POST'])
def service(request):
    try:
        #Get Data
        csv_file = request.FILES['file']
        column_email_name = request.data.get('email_column_name')
        column_status_email = request.data.get('colum_status_email')
        delimiter = request.data.get('delimiter')
        #Proccess CSV
        dataframe = pd.read_csv(csv_file, sep=delimiter, quotechar="'", error_bad_lines=False)
        dataframe.insert(dataframe.columns.get_loc(column_email_name) + 1, column_status_email, 0)
        dataframe[column_status_email] = dataframe[column_email_name].parallel_apply(verify_email)
        #Generate New CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={csv_file.name}'
        dataframe.to_csv(response, index=False, sep=delimiter)
        return response
    except Exception as e:
        return Response({'Error': e}, status.HTTP_400_BAD_REQUEST)