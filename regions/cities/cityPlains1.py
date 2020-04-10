from regions.cities.city import City


# class which stores the city of the Plains1 region
class CityPlains1(City):

    def name(self):
        return ""

    def yaml_name(self):
        return "region_plains_1"

    def plots(self):
        return [
            {
                "id": 1,
                "cells": [
                    {
                        "x_cell": 2,
                        "y_cell": 2
                    }
                ]
            },
            {
                "id": 2,
                "cells": [
                    {
                        "x_cell": 5,
                        "y_cell": 3
                    },
                    {
                        "x_cell": 6,
                        "y_cell": 3
                    }
                ]
            }
        ]

    # construct method
    def __init__(self):
        super().__init__()

    def update_draw(self, screen):
        pass
