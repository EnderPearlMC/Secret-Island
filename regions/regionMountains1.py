from regions.region import Region


# stores region mountain 1
class RegionMountains1(Region):

    def id(self):
        return 2

    def name(self):
        return "Mountains"

    def yaml_name(self):
        return "region_mountains_1"

    def description(self):
        return [
            "Can you climb it ?",
            "Improve your climbing",
            "skills in this beautyful",
            "landscape of mountain"
        ]

    def menu_settings(self):
        return {
            "background-path": "assets/images/historyMode/regions/regionMenu1.png"
        }
