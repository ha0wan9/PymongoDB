from ovh_api.PymongoDB.pymongodb import DefaultCol, AbstractModel
from ovh_api.PymongoDB.configs import AWSConfig, OVHConfig

__all__ = ["tray_non_orga_table_aws", "tray_non_orga_table_ovh"]


class TrayNonOrgaModel(AbstractModel):

    id: str = 'DATE_RESTAURANT'
    nbTrays: int = 0
    restaurant_name: str = 'restaurant'.upper()


class TrayNonOrgaColAWS(DefaultCol[TrayNonOrgaModel]):

    class Meta:
        mongodb_settings = AWSConfig()
        identifier = mongodb_settings.URI
        database_name = mongodb_settings.DB
        collection_name = mongodb_settings.COL['TrayNonOrga']['name']
        primary_key = mongodb_settings.COL['TrayNonOrga']['primary key']


class TrayNonOrgaColOVH(DefaultCol[TrayNonOrgaModel]):

    class Meta:
        mongodb_settings = OVHConfig()
        identifier = mongodb_settings.URI
        database_name = mongodb_settings.DB
        collection_name = mongodb_settings.COL['TrayNonOrga']['name']
        primary_key = mongodb_settings.COL['TrayNonOrga']['primary key']


tray_non_orga_table_aws = TrayNonOrgaColAWS(TrayNonOrgaModel)
tray_non_orga_table_ovh = TrayNonOrgaColOVH(TrayNonOrgaModel)
