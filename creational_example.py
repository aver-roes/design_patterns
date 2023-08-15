
# The Product
class House:
    def __init__(self, builder):
        self.stories = builder.stories
        self.door_type = builder.door_type
        self.roof_type = builder.roof_type

# The Builder
class HouseBuilder:
    def __init__(self):
        self.stories = None
        self.door_type = None
        self.roof_type = None

    # define the setters
    def set_stories(self, stories):
        self.stories = stories
        # return an instance of the HouseBuilder with the populated value
        return self
    
    def set_door_type(self, door_type):
        self.door_type = door_type
        return self

    def set_roof_type(self, roof_type):
        self.roof_type = roof_type
        return self

    # The Build method
    def build(self):
        # passing an instance of the builder class to the house class
        return House(self)


# The director: a class that manages the buliders
class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_1_story_house(self):
        return self.builder.set_stories(1).set_roof_type("single").set_roof_type("pointy").build()

    def build_2_story_house(self):
        return self.builder.set_stories(2).set_roof_type("double").set_roof_type("flat").build()

# usage
house_builder = HouseBuilder()
# setting the attributes separately
# one_stroy_house = house_builder.set_stories(1)
# one_stroy_house.set_door_type("single").set_roof_type("pointy")
# # Note that till now the house still an instance of the HouseBuilder class
# # not the House class yet

# # Now the it's a House class instance after calling the build method
# one_stroy_house.build()

director = Director(house_builder)
one_story_house = director.build_1_story_house()
two_story_house = director.build_2_story_house()


