class Length():
    
    # imperial to metric    
    def inchesToCm(self, inches):
        return inches * 2.54
    
    def feetToMetres(self, feet):
        return feet * 0.3048
        
    def yardsToMetres(self, yards):
        return yards * 0.9144
        
    def milesToKms(self, miles):
        return miles * 1.6093
    
    def nauticalMilesToKms(self, nm):
        return nm * 1.853
        
    # metric to imperial
    def mmsToInches(self, mm):
        return mm * 0.03937
        
    def centimetresToInches(self, cm):
        return cm * 0.393700787
        
    def centimetresToFeet(self, cm):
        return cm / 30.48
    
    def metresToYards(self, m):
        return m * 1.0936
        
    # metric conversions
    def cmToMm(self, cm):
        return cm * 10
    
    def mmToCm(self, mm):
        return mm / 10
    
    def metresToCm(self, m):
        return m * 100
        
    def cmToMetres(self, cm):
        return cm / 100
    
    def metresToMm(self, m):
        return m * 1000
        
    def mmToMetres(self, mm):
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
        
    def nauticalMilesToYards(self, nm):
        return nm * 2025.4
        
    def yardsToNauticalMiles(self, yards):
        return yards / 2025.4