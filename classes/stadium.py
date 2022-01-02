class Stadium:
    def __init__(self,name='',capacity=0,location_city='',location_state='',surface='',team='',opened='',center_field_distance_english=0,center_field_distance_metric=0,stadium_type='',roof_type=''):
        self.name = name#American Family Fielddouble-dagger
        self.capacity = capacity#41900
        self.location_city = location_city#Milwaukee
        self.location_state = location_state#Wisconsin
        self.surface = surface#Grass
        self.team = team#Milwaukee Brewers
        self.opened = opened#2001
        self.center_field_distance_english = center_field_distance_english#400
        self.center_field_distance_metric = center_field_distance_metric#122
        self.stadium_type = stadium_type#Retro-modern
        self.roof_type = roof_type#Retractable
        
    def get_name(self):
        return self.name

    def get_capacity(self):
        return self.capacity

    def get_location_city(self):
        return self.location_city

    def get_location_state(self):
        return self.location_state

    def get_surface(self):
        return self.surface

    def get_team(self):
        return self.team

    def get_opened(self):
        return self.opened

    def get_center_field_distance_english(self):
        return self.center_field_distance_english

    def get_center_field_distance_metric(self):
        return self.center_field_distance_metric

    def get_stadium_type(self):
        return self.stadium_type

    def get_roof_type(self):
        return self.roof_type

