# class which manages all the regions
class RegionManager:

    # construct method
    def __init__(self):

        # regions | Stores every region
        self.regions = []

        # current_region | Stores the current region
        self.current_region = None

    # adds a region to the region list
    # @param region : the region to add
    def add_region(self, region):
        self.regions.append(region)

    # loads a region
    # @param id : the id of the region to be added
    def load_region(self, id):
        for r in self.regions:
            if r.id() == id:
                self.current_region = r

    # unloads the current region
    def unload_current_region(self):
        self.current_region.city.is_one_category_shown = False
        self.current_region.city.loaded = False
        for c in self.current_region.city.build_categories:
            c['shown'] = False
        self.current_region.city.selected_ground_tile = None
        self.current_region = None

    # draws the current region's menu
    # @param screen : The screen surface where components will be drawn
    # @param game : the instance of the class Game
    def draw_region_menu(self, screen, game):
        self.current_region.draw_menu(screen, game)

    # draws the current region's city
    # @param screen : The screen surface where components will be drawn
    # @param game : the instance of the class Game
    def draw_region_city(self, screen, game):
        self.current_region.city.draw_city(screen, game)
