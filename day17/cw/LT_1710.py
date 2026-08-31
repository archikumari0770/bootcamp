def maximumUnits(boxTypes: list[list[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    total_units = 0
    for count, units in boxTypes:
        take = min(truckSize, count)
        total_units += take * units
        truckSize -= take
        if truckSize == 0: break
    return total_units