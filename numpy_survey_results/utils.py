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

def gluval(value, denom=1):
    return f"{value} ({100 * value / denom:1.0f}%)"

def gen_mdlist(data, fname, title="Comments"):
    """
    Generate a list in single-column Markdown table from a 1D data.

    To be used for including write-in comments.

    Examples
    --------
    The following example will generated a file at _generated/mytable.md
    with the following contents::

        |Comments|
        |--------|
        |I like x|
        |I like y|
        |I don't like anything|

    >>> data = [
    ...     "I like x",
    ...     "I like y",
    ...     "I don't like anything",
    ... ]
    >>> gen_mdlist(data, "mytable.md")
    """
    with open(f"_generated/{fname}", "w") as outf:
        outf.write(f"|{title}|\n")
        outf.write(f"|{'-' * len(title)}|\n")
        for row in data:
            outf.write(f"|{row}|\n")
