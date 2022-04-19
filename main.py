from cars.create_cars import Car
from cars.get_cars_info import get_cars_info

d = Car('BMW', 123)
d.stop_engine()
d.start_engine()
get_cars_info(d)
print(d)
