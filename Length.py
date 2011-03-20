class LengthConversions():
    
    # imperial to metric    
    def inchToCm(self, inch):
        return inch * 2.54
    
    def feetToMetre(self, foot):
        return foot * 0.3048
        
    def yardToMetre(self, yard):
        return yard * 0.9144
        
    def mileToKm(self, mile):
        return mile * 1.6093
    
    def nauticalMileToKm(self, nm):
        return nm * 1.853
        
    # metric to imperial
    def mmToInch(self, mm):
        return mm * 0.03937
        
    def centimetreToInch(self, cm):
        return cm * 0.393700787
        
    def centimetreToFoot(self, cm):
        return cm / 30.48
    
    def metreToYard(self, m):
        return m * 1.0936
        
    # metric conversions
    def cmToMm(self, cm):
        return cm * 10
    
    def mmToCm(self, mm):
        return mm / 10
    
    def metreToCm(self, m):
        return m * 100
        
    def cmToMetre(self, cm):
        return cm / 100
    
    def metreToMm(self, m):
        return m * 1000
        
    def mmToMetre(self, mm):
        return mm / 1000
    
    # imperial conversions
    def inchesToFeet(self, inches):
        return inches / 12
    
    def feetToInches(self, feet):
        return feet * 12
        
    def yardsToFeet(self, yard):
        return yard * 3
        
    def feetToYards(self, feet):
        return feet / 3
        
    def milesToYards(self, miles):
        return miles * 1760
        
    def yardsToMiles(self, yards):
        return yards / 1760
        
    def nauticalMileToYards(self, nm):
        return nm * 2025.4
        
    def yardsToNauticalMiles(self, yards):
        return yards / 2025.4