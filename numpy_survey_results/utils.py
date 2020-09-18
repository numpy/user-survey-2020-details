"""
Utilities to aid in analysis and publication of NumPy Community Survey results.
"""

def flatten(data, delimiter=','):
    """
    Expand ragged unicode arrays with ``delimiter``-separated rows into a
    flat array of individual entries.

    Parameters
    ----------
    data : numpy.ndarray with unicode dtype
        Array whose row-data will be flattened
    delimiter : str, default=','
        Delimiter separating individual entries within each row

    Returns
    -------
    out : list
        List of flattened entries

    Examples
    --------
    >>> a = np.array(["one,two", "three", "four,five,six"], dtype='U')
    >>> flatten(a)
    ['one', 'two', 'three', 'four', 'five', 'six']
    """
    out = []
    for row in data:
        out.extend(row.split(delimiter))
    return out
