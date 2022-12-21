import os
from define import get_mongo_uri

os.environ['MONGO_URI'] = get_mongo_uri(mongo_cloud='OVH_MONGO')

from ovh_api.PymongoDB.models import aliment_table, tray_table, sample_table

from datetime import datetime


def test():
    val1 = aliment_table.get(1)
    aliment = aliment_table.get(2)
    print(val1.aliment_id)
    # print(aliment_table.doc())
    # print(dict(aliment))
    # aliment_table.delete(aliment)
    # aliment_table.save(aliment)
    # print(aliment_table.list_all_elements())

    #time = val2[0].created_at #2021-05-11T13:31:16.000+00:00
    #print(time)
    # print(datetime.strptime(time, r'(\d{4})_(\d{2})_(\d{2})_(\d{2}):(\d{2}):(\d{2})'))


def test_create():
    alim = aliment_table.create(2)
    alim.aliment_cat_id = 217
    alim.aliment_cat_name = "Légumes verts"
    alim.aliment_name = "Asperge"
    alim.cat_eMin = 4.083
    alim.cat_eMoy = 12.667
    alim.cat_volumic_mass = 0.71
    alim.eMin = 5
    alim.eMoy = 17
    alim.volumic_mass = 0.89
    aliment_table.save(alim, forced=True)
    # alimget = aliment_table.get(2)
    # print(alimget)


def test_modify():
    trays = tray_table.get({'$regex': '^FOCH_2022_10_24'}, one=False)
    print(trays)
    for tray in trays:
        tray.status = "volume_done"
        tray_table.save(tray)


def test_delete():
    restaurant = 'Restest5555'
    date = '2022_07_21'
    tray_table.delete({'$regex': f"^{restaurant.upper() + '_' + date}"}, with_regex=True)
