import math


def dotProduct(D1, D2): 
    Sum = 0.0
    
    for key in D1:
        if key in D2:
            Sum += (D1[key] * D2[key])
            
    return Sum
  
  
def vector_angle(D1, D2): 
    numerator = dotProduct(D1, D2)
    denominator = math.sqrt(dotProduct(D1, D1) * dotProduct(D2, D2))
      
    return math.acos(numerator / denominator)