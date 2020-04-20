from regions.region import Region
from UI.popup import Popup
from regions.cities.cityPlains1 import CityPlains1


# stores region plains 1
class RegionPlains1(Region):

    def id(self):
        return 1

    def name(self):
        return "Plains"

    def yaml_name(self):
        return "region_plains_1"

    def description(self):
        return [
            "The first region !",
            "Just an infinite plain.",
            "You can find trees",
            "Only if you're lucky"
        ]

    def menu_settings(self):
        return {
            "background-path": "assets/images/historyMode/regions/regionMenu1.png"
        }

    def quests(self):
        return [
            {
                "id": 1,
                "name": "Wake up!",
                "x": 1.2,
                "y": 1.4,
                "unlocked": False,
                "finished": False
            },
            {
                "id": 2,
                "name": "Build your city!",
                "x": 1.8,
                "y": 1.6,
                "unlocked": False,
                "finished": False,
            },
            {
                "id": 3,
                "name": "Your First Dungeon",
                "x": 2.7,
                "y": 1.8,
                "unlocked": False,
                "finished": False,
            }
        ]

    def __init__(self):
        super().__init__(CityPlains1())

        self.explain = Popup("Help", [
            "Here is the menu of a region.",
            "The quests are represented by",
            "padlocks. You'll have to do them !"
        ])

    def update_draw(self, screen):
        self.explain.draw_popup(screen)

    def mouse_event(self, e):
        self.explain.click(e)
