import scipy.special
import scipyx as scx
import numpy as np
class Cauer:
    def __init__(self, k= None):
        self.k = k

    def SenoEliptico(self, z, k):
        sn, cn, dn, ph = scx.ellipj(u=z, m=k**2)
        return sn

    def L_SN(self, k):
        return float(np.real(scipy.special.ellipk(k**2)))

    def Li_SN(self, k):
        return float(scipy.special.ellipk(1 - k**2))
    



