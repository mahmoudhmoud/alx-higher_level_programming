#!/usr/bin/python3
''' logarithm dyal kaima '''

def find_peak(list_of_integers):
    ''' lka lkayim dyalo '''
        if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
