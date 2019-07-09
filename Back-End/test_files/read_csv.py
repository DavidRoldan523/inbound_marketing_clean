import pandas as pd
from pandarallel import pandarallel  # pip install pandarallel
import re
import dns.resolver

pandarallel.initialize()

def verify_email(email):
    email = str(email).lower()
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match == None:
        return 0
    try:
        dns.resolver.query(email.split('@')[1], 'MX')
    except Exception:
        return 0
    return 1

if __name__ == "__main__":
    try:
        delimiter = ';'
        column_status_email = 'Status_Email'
        column_email_name = 'Email - Lead Capture Data'
        csv_file = 'pruebaGilleteFinal.csv'
        dataframe = pd.read_csv(csv_file, sep=delimiter, quotechar="'", error_bad_lines=False)
        dataframe.insert(dataframe.columns.get_loc(column_email_name) + 1, column_status_email, 0)
        dataframe[column_status_email] = dataframe[column_email_name].parallel_apply(verify_email)
        print(dataframe.iloc[:100])
    except Exception as e:
        print(e)
    