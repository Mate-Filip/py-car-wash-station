class Car:

   def __init__(self,comfort_class: int, clean_mark: int, brand: str, *args) -> None:
       self.comfort_class = comfort_class
       self.clean_mark = clean_mark
       self.brand = brand

       if not isinstance(self.comfort_class, int):
          raise TypeError("comfort_class must be an integer")
       if 1 > self.comfort_class > 7:
          raise ValueError('comfort_class must be between 1 and 7')

       if not isinstance(self.clean_mark, int):
          raise TypeError("clean_mark must be an integer")
       if 1 >= self.clean_mark >= 10:
          raise ValueError("clean_mark must be between 1 and 10")

       if not isinstance(self.brand, str):
          raise ValueError('brand must be string')
       self.brand = brand.upper()

class CarWashStation:


    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating

        #1. `distance_from_city_center` - how far station from
        #the city center, from 1.0 to 10.0
        if not isinstance(distance_from_city_center, float):
            if 1 >= round(self.distance_from_city_center, 1) >= 10:
                raise ValueError('distance_from_city_center must '
                                 'be between 1.0 and 10.0 and must be float')
        self.distance_from_city_center = round(distance_from_city_center, 1)

        #2. `clean_power` - `clean_mark` to which this car wash station
        #washes (yes, not all stations can clean your car completely)
        if not isinstance(self.clean_power, int):
            if 1 >= self.clean_power <= 10:
                raise ValueError('clean_power must '
                                 'be between 1 and 10 and must be int')

        #3. `average_rating` - average rating of the station,
        #from 1.0 to 5.0, rounded to 1 decimal
        if not isinstance(avarage_rating, float):
            if 1 >= round(self.avarage_rating, 1) <= 5:
                raise ValueError('average_rating must '
                                 'be between 1.0 and 5.0 and must be float')
        self.average_rating = round(avarage_rating, 1)
        self.served_cars_list = []
        self.total_income = 0
        #4. `count_of_ratings` - number of people who rated
        self.count_of_ratings = 0


        # `CarWashStation` should have such methods:
        # 1. `serve_cars` - method, that takes a list of `Car`'s, washes only
        # cars with `clean_mark` < `clean_power` of wash station
        # and returns income of `CarWashStation` for serving this list of Car's,
        # rounded to 1 decimal:
    def serve_cars(self, car: list) -> None:
        for car in cars:
            self.wash_single_car(car)

        #2. `calculate_washing_price` - method, that calculates cost for a
        #single car wash,
        #cost is calculated as: car's comfort class * difference between
        #wash station's clean power and car's clean mark * car wash station
        #rating / car wash station
        #distance to the center of the city, returns number rounded
        #to 1 decimal;
    def calculate_washing_price(self, car: Car) -> float:
        self.washing_price = round(car.comfort_class * (self.clean_power -
        ((car.clean_mark * self.average_rating) / self.distance_from_city_center)), 1)
        return self.washing_price

        #3. `wash_single_car` - method, that washes a single car, so it should
        #have `clean_mark` equals wash station's `clean_power`, if
        #`wash_station.clean_power` is greater than `car.clean_mark`;
    def wash_single_car(self, car: Car) -> None:
        self.income = 0
        if car in served_cars_list:
            self.calculate_washing_price(car)
            self.single_car_income += self.washing_price
            print('Car is served')
            print(income)
            print(car.clean_mark)
        else:
            if car.clean_mark < self.clean_power:
                served_cars_list.append(car)
                self.calculate_washing_price(car)
                self.single_car_income += self.washing_price
                print('Car is served')
                print(income)
                print(car.clean_mark)
            else:
                print('Car is NOT served')

        #4. `rate_service` - method that adds a single rate to
        # the wash station, and based on this single rate
        #`average_rating` and `count_of_ratings` should be changed:
    def rate_service(self, rate: int) -> None:
        self.rate = rate
        self.average_rating = (self.average_rating * self.count_of_ratings + self.rate) / self.count_of_ratings + 1
        self.count_of_ratings += 1
