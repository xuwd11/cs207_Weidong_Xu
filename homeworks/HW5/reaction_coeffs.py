import numpy as np

def const(k):
    '''Returen the constant reaction rate coefficient k_const.
    
    INPUTS
    =======
    k: float
       Rection rate coefficient.
    
    RETURNS
    ========
    k_const: float, except the following cases:
       If k <= 0, a ValueError exception will be raised;
       if k = float('inf'), an OverflowError exception will be raised.
    
    EXAMPLES
    =========
    >>> const(100)
    100
    '''
    if k <= 0:
        raise ValueError('The reaction rate coefficient must be positive.')
    if abs(k) == float('inf'):
        raise OverflowError
    return k
    
def arr(A, E, T, R=8.314):
    '''Returns the Arrhenius reaction rate coefficient.
    
    INPUTS
    =======
    A: float
       The Arrhenius prefactor.
    E: float
       The activation energy for the reaction (in the same unit as R*T).
    T: float
       The absolute temperature (in Kelvins).
    R: float, optional, default value is 8.314
       The universal gas constant.
    
    RETURNS
    ========
    k_arr: float, except the following cases:
       If A <= 0, a ValueError exception will be raised;
       if T <= 0, a ValueError exception will be raised;
       if R <= 0, a ValueError exception will be raised;
       if A*exp(-E/R/T) = float('inf'), an OverflowError exception will be raised.
    
    EXAMPLES
    =========
    >>> arr(10**7, 10**3, 10**2)
    3003549.0889639617
    '''
    if A <= 0:
        raise ValueError('The Arrhenius prefactor A must be positive.')
    if T <= 0:
        raise ValueError('The temperature T must be positive.')
    if R <= 0:
        raise ValueError('The ideal gas constant R must be positive.')
    if R != 8.314:
        print('Warning! The ideal gas constant R has been changed from the default value (8.314).')
    k_arr = A * np.exp(-E/R/T)
    if k_arr == float('inf'):
        raise OverflowError
    if k_arr == 0:
        print('Warning! An underflow error might occur.')
    return k_arr

def mod_arr(A, b, E, T, R=8.314):
    '''Returns the modified Arrhenius reaction rate coefficient.
    
    INPUTS
    =======
    A: float
       The Arrhenius prefactor.
    b: float
       The modified Arrhenius parameter. If b is not a float number, a conversion is attempted.
    E: float
       The activation energy for the reaction (in the same unit as R*T).
    T: float
       The absolute temperature (in Kelvins).
    R: float, optional, default value is 8.314
       The universal gas constant.
       
    RETURNS
    ========
    k_mod_arr: float, except the following cases:
       If A <= 0, a ValueError exception will be raised;
       if b cannot be converted to a float number, a ValueError exception will be raised;
       if T <= 0, a ValueError exception will be raised;
       if R <= 0, a ValueError exception will be raised;
       if A*exp(-E/R/T) = float('inf'), an OverflowError exception will be raised.
    
    EXAMPLES
    =========
    >>> mod_arr(10**7, 0.5, 10**3, 10**2)
    30035490.889639616
    '''
    if A <= 0:
        raise ValueError('The Arrhenius prefactor A must be positive.')
    try:
        b = float(b)
    except:
        raise ValueError('The modified Arrhenius parameter b must be real.')
    if T <= 0:
        raise ValueError('The temperature T must be positive.')
    if R <= 0:
        raise ValueError('The ideal gas constant R must be positive.')
    if R != 8.314:
        print('Warning! The ideal gas constant R has been changed from the default value (8.314).')
    k_mod_arr = A*T**b*np.exp(-E/R/T)
    if k_mod_arr == float('inf'):
        raise OverflowError
    if k_mod_arr == 0:
        print('Warning! An underflow error might occur.')
    return k_mod_arr    