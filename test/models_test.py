from ovh_api.PymongoDB.models import aliment_table, tray_table, sample_table
from datetime import datetime

def test1():
    val1 = aliment_table.get(1)
    val2 = sample_table.get()

    time = val2[0].created_at #2021-05-11T13:31:16.000+00:00
    print(time)
    # print(datetime.strptime(time, r'(\d{4})_(\d{2})_(\d{2})_(\d{2}):(\d{2}):(\d{2})'))