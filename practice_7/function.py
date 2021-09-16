def get_sum(one, two, delimiter = '&'):   
    one = str(one)
    two = str(two)
    delimiter = str(delimiter)
    return(one + delimiter + two)
print(get_sum('Learn ', ' Pyhton').upper())