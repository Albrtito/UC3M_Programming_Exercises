# range_copy takes (stop, start, step) -> The stop has to be part of the start-step series.
def range_copy(stop: float or int, start=0, step=1):
    final_tup = ()
    final_list = []
    term = start
    final_list.append(term)
    if step < 0:
        while (term + step) >= stop:
            term = term + step
            final_list.append(term)
        final_tup = tuple(final_list)
    else:
        while (term + step) <= stop:
            term = term + step
            final_list.append(term)
        final_tup = tuple(final_list)
    return final_tup


print(range_copy(2,4,-2))
