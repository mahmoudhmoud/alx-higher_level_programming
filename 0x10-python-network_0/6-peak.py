#!/usr/bin/python3
''' logarithm dyal kaima '''


def find_peak(list_of_integers):
    ''' lka lkayim dyalo man tam '''
 if not list_of_integers:
        return None
    length = len(list_of_integers)
        if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)
    mid = length // 2
        if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    elif mid + 1 < length and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    else:
        return list_of_integers[mid]
