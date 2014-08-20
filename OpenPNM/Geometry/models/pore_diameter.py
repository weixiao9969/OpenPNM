r"""
===============================================================================
Submodule -- pore_diameter
===============================================================================

"""
import scipy as _sp

def sphere(geometry,
           psd_name,psd_shape,psd_loc,psd_scale,
           pore_seed='pore.seed',
           **kwargs):
    r"""
    Calculate pore diameter from seed values for a spherical pore body
    """
    import scipy.stats as spst
    prob_fn = getattr(spst,psd_name)
    P = prob_fn(psd_shape,loc=psd_loc,scale=psd_scale)
    value = P.ppf(geometry[pore_seed])
    return value

def sphere_from_radius(geometry,
           psd_name,psd_shape,psd_loc,psd_scale,
           pore_seed='pore.seed',
           **kwargs):
    r"""
    Calculate pore diameter from seed values for a spherical pore body
    """
    import scipy.stats as spst
    prob_fn = getattr(spst,psd_name)
    P = prob_fn(psd_shape,loc=psd_loc,scale=psd_scale)
    value = P.ppf(geometry[pore_seed])*2
    return value

def voronoi(network,
            pore_volume='pore.volume',
            **kwargs):
    r"""
    Calculate pore diameter from equivalent sphere - volumes must be calculated first
    """
    from scipy.special import cbrt
    pores = network.pores()
    pore_vols = network[pore_volume][pores]
    value = cbrt(6*pore_vols/_sp.pi)
    return value