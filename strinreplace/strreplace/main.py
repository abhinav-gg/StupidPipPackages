import itertools


def replace(s:str, d:dict) -> str:
    """
Function to take a string and a map of strings to find and replace allowing for simultaneous replacing of substrings.

Parameters
----------
first : 
    the 1st param should be main string that will be subject to the search and replace.
second :
    the 2nd param should be a dictionary map where each key and value is the substring to search for and its replacement.

Returns
-------
string
    the output from the search and replace.

Raises
------
Exception
    when there are clashes between two of the keys provided for the simultaneous search and replace.
    """



    try: assert isinstance(s, str)
    except: raise Exception("1st parameter must be of type string")
    try: assert isinstance(d, dict)
    except: raise Exception("2nd parameter must be of type dict")

    l = [ord(i) for i in s]
    x, y = d.keys(), d.values()

    try:
        for i in itertools.combinations(x, 2):
            assert not (i[0] in i[1] or i[1] in i[0])
    except:
        raise Exception("Key's may not be substrings of each other.")


    for _, j in enumerate(x):
        j = [ord(i) for i in j]
        b = len(j)
        for i in range(len(l) - b + 1):
            if list(l[i: i + b]) == list(j):
                l[i] = -1 * (1 + _)
                for __ in range(b - 1):
                    del l[i + 1]

    for _, j in enumerate(y):
        if -1 * (1+_) not in l: continue
        i = l.index(-1 * (1+_))
        del l[i]
        for p in [ord(o) for o in j]:
            l.insert(i, p)

    return "".join([chr(i) for i in l])


x = "aeiou"


print(replace(x, 
              {"i" : "a",
               "ae" : "u",
               "u" : "o",
               "o" : "e"}
              ))
