class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

        if not isinstance(self.comfort_class, int):
            raise TypeError("comfort_class must be an integer")
        if not 1 <= self.comfort_class <= 7:
            raise ValueError("comfort_class must be between 1 and 7")

        if not isinstance(self.clean_mark, int):
            raise TypeError("clean_mark must be an integer")
        if not 1 <= self.clean_mark <= 10:
            raise ValueError("clean_mark must be between 1 and 10")

        if not isinstance(self.brand, str):
            raise ValueError("brand must be string")
        self.brand = brand.upper()


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int = 0) -> None:

        # Walidacja distance_from_city_center
        if not isinstance(distance_from_city_center, (int, float)):
            raise TypeError("distance_from_city_center must be numeric")
        self.distance_from_city_center = (
            round(float(distance_from_city_center), 1))
        if not 1.0 <= self.distance_from_city_center <= 10.0:
            raise ValueError("distance_from_city_center "
                             "must be between 1.0 and 10.0")

        # Walidacja clean_power
        if not isinstance(clean_power, int):
            raise TypeError("clean_power must be integer")
        if not 1 <= clean_power <= 10:
            raise ValueError("clean_power must be between 1 and 10")
        self.clean_power = clean_power

        # Walidacja average_rating
        if not isinstance(average_rating, (int, float)):
            raise TypeError("average_rating must be numeric")
        self.average_rating = round(float(average_rating), 1)
        if not 1.0 <= self.average_rating <= 5.0:
            raise ValueError("average_rating must be between 1.0 and 5.0")

        # Inicjalizacja pozostałych atrybutów
        self.served_cars = []
        self.total_income = 0.0
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list["Car"]) -> float:
        self.total_income = 0.0
        for car in cars:
            income = self.wash_single_car(car)
            self.total_income += income
        return round(self.total_income, 1)

    def calculate_washing_price(self, car: "Car") -> float:
        clean_diff = self.clean_power - car.clean_mark
        price = (car.comfort_class * clean_diff * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: "Car") -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            self.served_cars.append(car)
            return price
        return 0.0

    def rate_service(self, rate: int) -> None:
        if not isinstance(rate, int) or not 1 <= rate <= 5:
            raise ValueError("Rate must be integer between 1 and 5")

        if self.count_of_ratings == 0:
            self.average_rating = float(rate)
        else:
            total = self.average_rating * self.count_of_ratings + rate
            self.average_rating = round(total / (self.count_of_ratings + 1), 1)

        self.count_of_ratings += 1
