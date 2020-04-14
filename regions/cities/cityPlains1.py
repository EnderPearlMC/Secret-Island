from regions.cities.city import City


# class which stores the city of the Plains1 region
class CityPlains1(City):

    def name(self):
        return ""

    def yaml_name(self):
        return "region_plains_1"

    def unlocked_items(self):
        return {
            "Ground": [0, 1],
            "Builds": []
        }

    # construct method
    def __init__(self):
        super().__init__()

    def update_draw(self, screen):
        pass
