def maximumUnits(boxTypes: list[list[int]], truckSize: int) -> int:
    cubetas = [0] * (max(boxTypes, key=lambda i: i[1])[1]+1)
    
    cajas_restantes = truckSize
    cajas_cargadas = 0
    mayor = menor = 0

    for item in boxTypes:
        if (cubetas[item[1]]==0):
            cubetas[item[1]] = item[0]
            if (item[1] > mayor): mayor = item[1]
            if (item[1] < menor or menor == 0): menor = item[1]
        else:
            cubetas[item[1]] += item[0]
            if (item[1] > mayor): mayor = item[1]
            if (item[1] < menor or menor == 0): menor = item[1]

    for i in range(mayor,menor-1,-1):
        if cubetas[i] == 0: continue
        if cubetas[i] > cajas_restantes:
            cajas_cargadas += cajas_restantes*i
            return cajas_cargadas
        else:
            cajas_cargadas += cubetas[i]*i
            cajas_restantes -= cubetas[i] 
    return cajas_cargadas
    

if __name__ == "__main__":
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    print(maximumUnits(boxTypes,10))