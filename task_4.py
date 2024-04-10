class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list
        self._pi = 3.141  # Private variable for pi

    def area(self):
        """
        Calculate the area of circles with given radii.
        """
        areas = []
        for radius in self.radius_list:
            area = self._pi * radius ** 2
            areas.append(area)
        return areas

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of circles with given radii.
        """
        perimeters = []
        for radius in self.radius_list:
            perimeter = 2 * self._pi * radius
            perimeters.append(perimeter)
        return perimeters

# Example usage
circle_radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(circle_radii)

# Calculate and print areas
print("Areas of circles:", circle.area())

# Calculate and print perimeters
print("Perimeters of circles:", circle.perimeter())


class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = None  # You can set an actual price if needed
        self.inches = None  # You can set actual inches if needed
        self.OnOFF = False
        self._volume = 50  # Private variable for volume

    def increase_volume(self):
        self._volume = min(self._volume + 1, 100)

    def decrease_volume(self):
        self._volume = max(self._volume - 1, 0)

    def set_channel(self, channel_number):
        self.channel = max(1, min(channel_number, 50))

    def reset_tv(self):
        self.channel = 1
        self._volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self._volume}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate


# Example usage
panasonic_led = LedTV(brand="Panasonic", screen_thickness="Slim", energy_usage="Low", lifespan="10 years", refresh_rate=120)
panasonic_led.increase_volume()
panasonic_led.set_channel(8)
print(panasonic_led.status())
