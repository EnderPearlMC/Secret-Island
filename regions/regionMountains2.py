from regions.region import Region


# stores region mountain 2
class RegionMountains2(Region):

    def id(self):
        return 3

    def name(self):
        return "Mountains 2"

    def yaml_name(self):
        return "region_mountains_2"

    def description(self):
        return [
            "Once again !",
            "Let's see if you",
            "can still climb",
            "huge mountains !"
        ]
    
    def menu_settings(self):
        return {
            "background-path": "assets/images/historyMode/regions/regionMenu1.png"
        }

    def __init__(self):
        super().__init__('')
