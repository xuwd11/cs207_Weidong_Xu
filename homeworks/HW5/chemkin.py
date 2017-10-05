import numpy as np
import reaction_coeffs

def progress_rate_1(nu, x, k):
    '''Returns the progress rate for a reaction of the form: nu_A A + nu_B B -> nu_C C
    
    INPUTS
    =======
    nu: 3-element list or array
       Stoichiometric coefficient vector which specifies the stoichiometric coefficients of 
       species A, B and C
    x: 3-element list or array
       Concentration vector which specifies the concentrations of species A, B and C
    k: float
       reaction rate coefficient
    
    RETURNS
    ========
    omega: float, except the following cases:
       If nu or x is not a 3-element list or array, a TypeError will be raised;
       if nu contains non-positive element(s), a ValueError will be raised;
       if x contains negative element(s), a ValueError will be raised;
       if k <= 0, a ValueError will be raised.
    
    EXAMPLES
    >>> progress_rate_1([2, 1, 1], [1, 2, 3], 10)
    20
    >>> progress_rate_1([1, 1, 1], [4, 2, 3], 10)
    80
    '''
    try:
        if len(nu) != 3:
            raise TypeError('nu must be a 3 element list or array.')
    except:
        raise TypeError('nu must be a 3 element list or array.')
    if not all([nu_ > 0 for nu_ in nu]):
        raise ValueError('All elements in nu must be positive.')
    try:
        if len(x) != 3:
            raise TypeError('x must be a 3 element list or array.')
    except:
        raise TypeError('x must be a 3 element list or array.')
    if any([x_ < 0 for x_ in x]):
        raise ValueError('All elements in x must be non-negative.')
    if k <= 0:
        raise ValueError('k must be positive.')
    omega = k*x[0]**nu[0]*x[1]**nu[1]
    return omega

def progress_rate_2(nu_1, nu_2, x, k):
    '''Returns the progress rate for a system of reactions of the form:
       nu'_11 A + nu'_21 B -> nu''_31 C
       nu'_12 A + nu'_32 C -> nu''_22 B + nu''_32 C
    
    INPUTS
    =======
    nu_1: array of shape (3, 2)
       Stoichiometric coefficient vector which specifies the stoichiometric coefficients of reactants.
       If nu_1 is not an array, a conversion is attempted.
    nu_2: array of shape (3, 2)
       Stoichiometric coefficient vector which specifies the stoichiometric coefficients of products.
       If nu_2 is not an array, a conversion is attempted.
    x: 3-element list or array
       Concentration vector which specifies the concentrations of species A, B and C
    k: float
       reaction rate coefficient
    
    RETURNS
    ========
    omega: 2-element tuple
       Has the form (float, float) which corresponds to the progress rates of 2 reactions, except 
       the following cases:
       If nu_1 or nu_2 cannot be converted to an array of shape (3, 2), a TypeError will be raised;
       if nu_1 or nu_2 contains negative element(s), a ValueError will be raised;
       if x is not a 3-element list or array, a TypeError will be raised;
       if x contains negative element(s), a ValueError will be raised;
       if k <= 0, a ValueError will be raised.
    
    EXAMPLES
    >>> progress_rate_2([[1, 2], [2, 0], [0, 2]], [[0, 0], [0, 1], [2, 1]], [1, 2, 1], 10)
    (40, 10)
    >>> progress_rate_2([[1, 1], [2, 0], [0, 2]], [[0, 0], [0, 1], [2, 1]], [1, 2, 3], 10)
    (40, 90)
    '''
    try:
        nu_1 = np.array(nu_1)
        if nu_1.shape != (3, 2):
            raise TypeError('nu_1 must be able to converted to a 3 X 2 array.')
    except:
        raise TypeError('nu_1 must be able to converted to a 3 X 2 array.')
    try:
        nu_2 = np.array(nu_2)
        if nu_2.shape != (3, 2):
            raise TypeError('nu_2 must be able to converted to a 3 X 2 array.')
    except:
        raise TypeError('nu_2 must be able to converted to a 3 X 2 array.')
    if np.any(nu_1 < 0):
        raise ValueError('All elements in nu_1 must be non-negative.')
    if np.any(nu_2 < 0):
        raise ValueError('All elements in nu_2 must be non-negative.')
    try:
        if len(x) != 3:
            raise TypeError('x must be a 3 element list or array.')
    except:
        raise TypeError('x must be a 3 element list or array.')
    if any([x_ < 0 for x_ in x]):
        raise ValueError('All elements in x must be non-negative.')
    if k <= 0:
        raise ValueError('k must be positive.')
    omega = (k*np.prod([x[i]**nu_1[i, 0] for i in range(3)]), k*np.prod([x[i]**nu_1[i, 1] for i in range(3)]))
    return omega

def reaction_rate_1(nu_1, nu_2, x, k):
    '''Returns the reaction rates for species in a system of reactions of the form:
       nu'_11 A + nu'_21 B -> nu''_31 C
       nu'_32 C -> nu''_12 A + nu''_22 B
    
    INPUTS
    =======
    nu_1: array of shape (3, 2)
       Stoichiometric coefficient vector which specifies the stoichiometric coefficients of reactants.
       If nu_1 is not an array, a conversion is attempted.
    nu_2: array of shape (3, 2)
       Stoichiometric coefficient vector which specifies the stoichiometric coefficients of products.
       If nu_2 is not an array, a conversion is attempted.
    x: 3-element list or array
       Concentration vector which specifies the concentrations of species A, B and C
    k: float
       reaction rate coefficient
    
    RETURNS
    ========
    f: 3-element array
       Has the form (float, float, float) which corresponds to the reaction rates of species A, B, C, 
       except the following cases:
       If nu_1 or nu_2 cannot be converted to an array of shape (3, 2), a TypeError will be raised;
       if nu_1 or nu_2 contains negative element(s), a ValueError will be raised;
       if x is not a 3-element list or array, a TypeError will be raised;
       if x contains negative element(s), a ValueError will be raised;
       if k <= 0, a ValueError will be raised.
    
    EXAMPLES
    >>> reaction_rate_1([[1, 0], [2, 0], [0, 2]], [[0, 1], [0, 2], [1, 0]], [1, 2, 1], 10)
    array([-30, -60,  20])
    >>> reaction_rate_1([[1, 0], [2, 0], [0, 1]], [[0, 1], [0, 2], [1, 0]], [1, 2, 3], 10)
    array([-10, -20,  10])
    '''
    try:
        nu_1 = np.array(nu_1)
        if nu_1.shape != (3, 2):
            raise TypeError('nu_1 must be able to converted to a 3 X 2 array.')
    except:
        raise TypeError('nu_1 must be able to converted to a 3 X 2 array.')
    try:
        nu_2 = np.array(nu_2)
        if nu_2.shape != (3, 2):
            raise TypeError('nu_2 must be able to converted to a 3 X 2 array.')
    except:
        raise TypeError('nu_2 must be able to converted to a 3 X 2 array.')
    if np.any(nu_1 < 0):
        raise ValueError('All elements in nu_1 must be non-negative.')
    if np.any(nu_2 < 0):
        raise ValueError('All elements in nu_2 must be non-negative.')
    try:
        if len(x) != 3:
            raise TypeError('x must be a 3 element list or array.')
    except:
        raise TypeError('x must be a 3 element list or array.')
    if any([x_ < 0 for x_ in x]):
        raise ValueError('All elements in x must be non-negative.')
    if k <= 0:
        raise ValueError('k must be positive.')
    omega = progress_rate_2(nu_1, nu_2, x, k)
    omega = np.array(omega).reshape((len(omega), 1))
    f = np.sum((np.dot(nu_2, omega) - np.dot(nu_1, omega)), axis=1)
    return f