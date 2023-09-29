wind = float(input())
if(wind >= 0 and wind <= 0.2):
    print("Logn")
elif(wind >= 0.3 and wind <= 1.5):
    print("Andvari")
elif(wind >= 1.6 and wind <= 3.3):
    print("Kul")
elif(wind >= 3.4 and wind <= 5.4):
    print("Gola")
elif(wind >= 5.5 and wind <= 7.9):
    print("Stinningsgola")
elif(wind >= 8.0 and wind <= 10.7):
    print("Kaldi")
elif(wind >= 10.8 and wind <= 13.8):
    print("Stinningskaldi")
elif(wind >= 13.9 and wind <= 17.1):
    print("Allhvass vindur")
elif(wind >= 17.2 and wind <= 20.7):
    print("Hvassvidri")
elif(wind >= 20.8 and wind <= 24.4):
    print("Stormur")
elif(wind >= 24.5 and wind <= 28.4):
    print("Rok")
elif(wind >= 28.5 and wind <= 32.6):
    print("Ofsavedur")
elif(wind >= 32.7):
    print("Farvidri")