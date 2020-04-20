from UI.popup import Popup
from regions.cities.city import City


# class which stores the city of the Plains1 region
class CityPlains1(City):

    def name(self):
        return "City Plains 1"

    def yaml_name(self):
        return "region_plains_1"

    def unlocked_items(self):
        return {
            "Ground": [0, 1, 2, 3, 4],
            "Builds": [0]
        }

    # construct method
    def __init__(self):
        super().__init__()

        self.explain = Popup("Help", ['Lol'])

    def update_draw(self, screen):

        self.explain.draw_popup(screen)

    def mouse_event(self, e):
        self.explain.click(e)