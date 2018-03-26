def litery(x):
    slownik = ["zero","jeden","dwa","trzy","cztery",
               "piec","szesc","siedem","osiem","dziewiec"]
    return map(lambda x:slownik[int(x)], str(x))
x = raw_input("podaj liczbe: ")
print litery(x)
