from ovh_api.PymongoDB.models import aliment_table, tray_table, sample_table
from datetime import datetime

def do():
    val1 = aliment_table.get(1)
    #aliment = aliment_table.create(1)
    print(val1.aliment_id)

    aliment = aliment_table.create(2)
    print(aliment.aliment_id)

    #time = val2[0].created_at #2021-05-11T13:31:16.000+00:00
    #print(time)
    # print(datetime.strptime(time, r'(\d{4})_(\d{2})_(\d{2})_(\d{2}):(\d{2}):(\d{2})'))

if __name__ == '__main__':
    do()