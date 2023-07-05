from abc import ABC, abstractmethod

class CoordinateProcessor(ABC):
    @abstractmethod
    def process(self, coordinate):
        pass

class DecimalCoordinateProcessor(CoordinateProcessor):
    def process(self, coordinate):
        return float(coordinate)

class IntegerCoordinateProcessor(CoordinateProcessor):
    def process(self, coordinate):
        return int(coordinate)

# Sử dụng Strategy Pattern
coordinates = ["3.14", "2.718", "1.618"]

processor = DecimalCoordinateProcessor()  # Chọn strategy DecimalCoordinateProcessor
processed_coordinates = []

for coordinate in coordinates:
    processed_coordinate = processor.process(coordinate)
    processed_coordinates.append(processed_coordinate)

print(processed_coordinates)
