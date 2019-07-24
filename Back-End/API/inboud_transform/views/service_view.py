import pandas as pd
import re
import dns.resolver
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from pandarallel import pandarallel  # pip install pandarallel

pandarallel.initialize()


def verify_email(email):
    valid_emails_exceptions = ['gmail.com.mx', 'gmail.com.co', 'hotmail.com.co',
                               'hotmail.com.mx']
    invalid_emails_exceptions = ['gimail.com', 'iclud.com', 'gamil.com', 'hotamial.com', 'gnail.com',
                                 'iclojd.com', 'hotmil.com', 'mail.com', 'hotmai.com', 'hotmsil.com',
                                 'yopmail.com', 'gail.com', 'outlok.com', 'hitmail.com', 'ourlook.com',
                                 'gmailm.com', 'iclod.com', 'honmail.com', 'ymail.com', 'vmail.com',
                                 'gmai.com', 'gmil.com', 'hotmll.com', 'hotmial.com', 'gmaio.com',
                                 'gmial.com', 'gmali.com', 'hotmatmail.com', 'hmail.com']
    if type(email) != str or email == "" or email == " ":
        return "Invalido"
    email = email.strip().lower()   
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
        # Get Data
        csv_file = request.FILES['file']
        column_email_name = request.data.get('email_column_name').strip()
        column_status_email = request.data.get('column_status_email').strip()
        delimiter = request.data.get('delimiter')
        # Proccess CSV
        dataframe = pd.read_csv(csv_file, sep=delimiter, quotechar="'", error_bad_lines=False, skip_blank_lines=False)
        dataframe.insert(dataframe.columns.get_loc(column_email_name) + 1, column_status_email, "Valido")
        dataframe[column_status_email] = dataframe[column_email_name].parallel_apply(verify_email)
        # Generate New CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={csv_file.name}'
        dataframe.to_csv(response, index=False, sep=delimiter)
        return response
    except Exception as e:
        return Response({'Error': e})
