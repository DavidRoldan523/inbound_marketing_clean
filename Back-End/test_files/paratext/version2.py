import dask.dataframe as dd
import random
import time


if __name__ == "__main__":
    time_initial = time.time()
    filename = "prueba_camila.csv" 
    dataframe = dd.read_csv(filename, sep=',', quotechar="'", error_bad_lines=False)
    print(dataframe.loc['Email - Lead Capture Data'])
    print(f'{time.time() - time_initial} seg')


    