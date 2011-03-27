class Area():
    
    # imperial to metric 
    def in2ToCm2(self, in2):
        return in2 * 6.4516
        
    def ft2ToMetres2(self, ft2):
        return ft2 * 0.0929
        
    def yd2ToMetres2(self, yd2):
        return yd2 * 0.8361
        
    def acresToMetres2(self, a):
        return a * 4046.9
        
    def miles2ToKm2(self, miles2):
        return miles2 * 2.59
        
    # metric to imperial
    def cm2ToIn2(self, cm2):
        return cm2 * 0.1550

    def m2ToYd2(self, m2):
        return m2 * 1.1960

    def haToAcres(self, ha):
        return ha * 2.4711

    def km2ToMiles2(self, km2):
        return km2 * 0.3861
        
    # metric to metric
    def cm2ToMm2(self, cm2):
        return cm2 * 100
        
    def metres2ToCm2(self, m2):
        return m2 * 10000
        
    def hectaresToMetres2(self, h):
        return h * 10000
        
    def km2ToHectares(self, km2):
        return km2 * 100
        
    # imperial to imperial
    def ft2ToIn2(self, ft2):
        return ft2 * 144
        
    def yd2ToFt2(self, yd2):
        return yd * 9
        
    def acreToYd2(self, yd2):
        return yd2 * 4840
        
    def miles2ToAcres(self, m2):
        return m2 * 640