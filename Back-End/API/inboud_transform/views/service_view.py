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
    valid_emails_exceptions = ['gmail.com.mx', 'gmail.com.co', 'hotmail.com.co',
                               'hotmail.com.mx']
    invalid_emails_exceptions = ['gimail.com', 'iclud.com', 'gamil.com',
                                 'hotamial.com', 'gnail.com', 'iclojd.com',]
    email = email.strip().lower()
    if type(email) != str or email == '' or email == ' ':
        return "Invalido"
        
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match == None:
        return "Invalido"

    domain = email.split('@')[1]

    if domain in invalid_emails_exceptions:
        return "Invalido"
    
    if domain in valid_emails_exceptions:
        return "Valido"

    try:
        dns.resolver.query(domain, 'MX')
    except Exception:
        return "Invalido"

    return "Valido"

@api_view(['POST'])
def service(request):
    try:
        #Get Data
        csv_file = request.FILES['file']
        column_email_name = str(request.data.get('email_column_name')).strip()
        column_status_email = str(request.data.get('column_status_email')).strip()
        delimiter = request.data.get('delimiter')
        #Proccess CSV
        dataframe = pd.read_csv(csv_file, sep=delimiter, quotechar="'", error_bad_lines=False, skip_blank_lines=False)
        dataframe.insert(dataframe.columns.get_loc(column_email_name) + 1, column_status_email, "Valido")
        dataframe[column_status_email] = dataframe[column_email_name].parallel_apply(verify_email)
        #Generate New CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={csv_file.name}'
        dataframe.to_csv(response, index=False, sep=delimiter)
        return response
    except Exception as e:
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({'500_internal_server_error':'Bad file'})
        else:
            return Response({'Error': e})