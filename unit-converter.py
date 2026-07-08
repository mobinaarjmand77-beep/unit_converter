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
    
def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("adade motabar vared kon!")

def run_converter(converter, name):
    units = converter.units_list
    print(f"\nVahedhaye {name}:")
    for i, u in enumerate(units, 1):
        print(f" {i}. {u}")
    
    while True:
        try:
            fi = int(input("Shomareh mabda ra vared konid: ")) - 1
            if 0 <= fi < len(units):
                from_u = units[fi]
                break
        except:
            pass
        print("Shomareh eshtebah!")
    
    while True:
        try:
            ti = int(input("Shomareh maghsad ra vared konid: ")) - 1
            if 0 <= ti < len(units):
                to_u = units[ti]
                break
        except:
            pass
        print("Shomareh eshtebah!")
    
    val = get_number("Maghadar ra vared konid: ")
    result = converter.convert(val, from_u, to_u)
    print(f"\n{val} {from_u} = {result} {to_u}")
    
def main():
    length_conv = LengthConverter()
    weight_conv = WeightConverter()
    temp_conv = TemperatureConverter()
    
    while True:
        choice = show_menu()
        
        if choice == "0":
            print("Khodahafez!")
            break
        elif choice == "1":
            run_converter(length_conv, "Length")
        elif choice == "2":
            run_converter(weight_conv, "Weight")
        elif choice == "3":
            run_converter(temp_conv, "Temperature")
        else:
            print("gozineh namotabar!")
            continue
        
        again = input("\nEdameh? (y/n): ")
        if again != "y":
            print("Khodahafez!")
            break

if __name__ == "__main__":
    main()
