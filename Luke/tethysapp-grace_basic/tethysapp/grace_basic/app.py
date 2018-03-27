from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import SpatialDatasetServiceSetting


class GraceBasic(TethysAppBase):


    name = 'Grace Basic'
    index = 'grace_basic:home'
    icon = 'grace_basic/images/icon.gif'
    package = 'grace_basic'
    root_url = 'grace-basic'
    color = '#27ae60'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):

        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='grace-basic',
                controller='grace_basic.controllers.home'),
            UrlMap(name='home_graph',
                   url='grace-basic/home/{id}',
                   controller='grace_basic.controllers.home_graph')
        )


        return url_maps


    def spatial_dataset_service_settings(self):

        sds_settings = (
            SpatialDatasetServiceSetting(
                name='default',
                description='',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
        ),
    )

        return sds_settings