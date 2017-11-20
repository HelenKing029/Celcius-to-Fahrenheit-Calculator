def cTof(celsius):
    f = float(celsius) * 9/5 + 32
    return (f)

celsius = float(input("Enter temperature in celsius: "))
if celsius < float(-273.15):
    print("That's colder than physical matter can reach!")
else: print(cTof(celsius))
