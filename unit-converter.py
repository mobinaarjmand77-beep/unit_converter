class Converter:
    def __init__(self):
        self.units_list = []
        self.base_unit_name = ""
    
    def convert(self, value, from_unit, to_unit):
        return 0
        
class LengthConverter(Converter):
    def __init__(self):
        Converter.__init__(self)
        self.base_unit_name = "meter"
        self.rates = {
            "meter": 1,
            "kilometer": 1000,
            "mile": 1609.34,
            "foot": 0.3048,
            "inch": 0.0254,
            "centimeter": 0.01
        }
        self.units_list = list(self.rates.keys())
    
    def convert(self, value, from_unit, to_unit):
        in_meter = value * self.rates[from_unit]
        result = in_meter / self.rates[to_unit]
        return result

class WeightConverter(Converter):
    def __init__(self):
        Converter.__init__(self)
        self.base_unit_name = "kilogram"
        self.rates = {
            "kilogram": 1,
            "gram": 0.001,
            "pound": 0.453592,
            "ounce": 0.0283495
        }
        self.units_list = list(self.rates.keys())
    
    def convert(self, value, from_unit, to_unit):
        in_kg = value * self.rates[from_unit]
        result = in_kg / self.rates[to_unit]
        return result

class TemperatureConverter(Converter):
    def __init__(self):
        Converter.__init__(self)
        self.base_unit_name = "celsius"
        self.units_list = ["celsius", "fahrenheit", "kelvin"]
    
    def convert(self, value, from_unit, to_unit):

        if from_unit == "celsius":
            celsius = value
        elif from_unit == "fahrenheit":
            celsius = (value - 32) * 5 / 9
        elif from_unit == "kelvin":
            celsius = value - 273.15
        
        if to_unit == "celsius":
            return celsius
        elif to_unit == "fahrenheit":
            return celsius * 9 / 5 + 32
        elif to_unit == "kelvin":
            return celsius + 273.15

def show_menu():
    print("1.tabdil tol")
    print("2. tabdil wazn")
    print("3. tabdil dama")
    print("0. khorooj")
    return input("entekhabe shoma: ")
    
