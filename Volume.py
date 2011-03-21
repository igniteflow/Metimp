class Volume:
    
    # metric ti imperial
    def cm3ToIn3(self, cm3):
        return cm3 * 0.0610
        
    def dm3ToFt3(self, dm3):
        return dm3 * 0.0353
        
    def m3ToYd3(self, m3):
        return m3 * 1.3080 
    
    def litresToPints(self, l):
        return l * 1.76
    
    def hectolitresToGallons(self, hl):
        return hl * 21.997
        
    # imperial to metric
    def in3ToCm3(self, i):
        return i * 16.387
        
    def feet3ToMetres3(self, ft):
        return ft * 0.0283
        
    def flozToMl(self, floz):
        return floz * 28.413
        
    def pintsToLitres(self, p):
        # after 3 you won't care
        return p * 0.5683
        
    def gallonsToLitres(self, g):
        return g * 4.5461
        
    # USA measures
    def usaFlozToMl(self, floz):
        return floz * 29.574 
        
    def usaPintsToLitres(self, p):
        return p * 0.4731
        
    def usaGallonsToLitres(self, g):
        return g * 3.7854
        
    # USA to UK
    def usaToUkFloz(self, floz):
        return floz * 1.0408
        
    def usaToUkPints(self, p):
        return p * 0.8327
        
    def usaToUkGallons(self, g):
        return g * 0.8327
    
    # USA to UK
    def ukToUsaFloz(self, floz):
        return floz / 1.0408

    def ukToUsaPints(self, p):
        return p / 0.8327

    def ukToUsaGallons(self, g):
        return g / 0.8327
    