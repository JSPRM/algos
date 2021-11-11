import math 
def getTriangleArea(x, y):
    lado1=distancia([x[0],y[0]],[x[1],y[1]])
    lado2=distancia([x[0],y[0]],[x[2],y[2]])
    lado3=distancia([x[1],y[1]],[x[2],y[2]])
    
    s= (lado1 + lado2 +lado3)/2
    
    area = math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
    
    return area
    
def distancia(uno,dos) -> float:
    return math.sqrt((uno[0]-dos[0])**2 + (uno[1]- dos[1])**2)

if __name__ == "__main__":
    print(([0,0],[0,2]))