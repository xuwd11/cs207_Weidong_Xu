import numpy as np

def L2(v, *args):
    """Returns the L2 norm of a vector v
    
    INPUTS
    =======
    v: list
       Vector of which the L2 norm to be calculated
    *arg: list, optional
       Weight vector
       
    RETURNS
    ========
    L2_norm: float
       float unless len(v) != len(args[0])
       in which case a ValueError exception is raised
       
    EXAMPLES
    =========
    >>> L2([3, 4])
    5.0
    >>> L2([3, 4], [1, 1])
    5.0
    """
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)