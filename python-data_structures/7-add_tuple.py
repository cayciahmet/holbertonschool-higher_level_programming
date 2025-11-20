#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Tuple-lara 0, 0 elave edirik ki, xeta vermesin
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    
    # Ilk iki elementi toplayib qaytaririq
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
