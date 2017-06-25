def convert(array):
    list_farenheit = []
    for temp in array:
        farenheit = float((temp * 1.8) + 32)
        list_farenheit.append(farenheit)
    return list_farenheit
