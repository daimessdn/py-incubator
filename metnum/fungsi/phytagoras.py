from math import sqrt
from pangkat import pangkat

def phytagoras(a,b):
    kwA = pangkat(a,2)
    kwB = pangkat(b,2)
    kwC = kwA + kwB
    
    c = sqrt(kwC)
    
    return c