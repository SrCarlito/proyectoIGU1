from item1b import MomentoCentralNormalizado
# Momento De Hu 1
def MomentoDeHu_1(imgRoute):
    return (MomentoCentralNormalizado(imgRoute, 2, 0)
            + MomentoCentralNormalizado(imgRoute, 0, 2))


# Momento De Hu 2
def MomentoDeHu_2(imgRoute):
    return ((MomentoCentralNormalizado(imgRoute, 2, 0)
            - MomentoCentralNormalizado(imgRoute, 0, 2))**2
            + 4*(MomentoCentralNormalizado(imgRoute, 1, 1) ** 2))


# Momento De Hu 3
def MomentoDeHu_3(imgRoute):
    return ((MomentoCentralNormalizado(imgRoute, 3, 0) -
             3*MomentoCentralNormalizado(imgRoute, 1, 2))**2
            +
            (3*MomentoCentralNormalizado(imgRoute, 2, 1) -
             MomentoCentralNormalizado(imgRoute, 0, 3))**2)

def printData(IMAGE):
    print("Momento de Hu 1: " , MomentoDeHu_1(IMAGE))
    print("Momento de Hu 2: " , MomentoDeHu_2(IMAGE))
    print("Momento de Hu 3: " , MomentoDeHu_3(IMAGE))

printData("test.png")