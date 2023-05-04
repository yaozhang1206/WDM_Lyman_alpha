import numpy as np
import pickle

"""
    Look! A pickle farmer?
    
    We run this script once per model.
    
"""

""" FIRST: carefully tune the parameters of the dictionary to your model """

# put attention to sigma8 value (and thus As value need to be consistend), m_wdm value

# after that put attention to the fast-model and fast-realization

# finally, adjust the gadget-realization and gadget-model


# dictionary
params={}
params['h'] = 0.6774
params['Obh2'] = 0.02230
params['Och2'] = 0.1188
params['mnu'] = 0.194
params['As'] = 2.142 # 10^9 * As
params['ns'] = 0.9667
params['alphas'] = -0.002
params['taure'] = 0.066
params['bHI'] = 2.82
params['OHI'] = 1.18e-3 * 1.e3
params['fast-model'] = '9keV_s8'
params['fast-realization'] = 'r1'
params['gadget-realization'] = 'r1'
params['gadget-model'] = '9keV_s8' # so it should be something like 9keV_s8 now
params['m_wdm'] = 9.0 #np.infty # for cdm is np.infty
params['band'] = 'g'
params['sigma8'] = 0.8159
params['telescope'] = 'skalow'
params['t_int'] = 1000
params['beam'] = 32 # think about this one
params['z_max_pk'] = 35 # 35 for running patchy class and 5.5 for everything else
params['pickle'] = True # this needs to be True for this script.

print('\n')
print('***********************************************************')
print('This is your dictionary, please check the sigma8, m_WDM values and others!!!')
print('***********************************************************')
print(params)
print('\n')
# let's import all the important classes and do their pickles one by one

""" Let's do the transparency """
print('***********************************************************')
print('Farmer is producing psi pickles, YUM')

import psi

psi_veggie = psi.transparency(params)
print('\n')

print('***********************************************************')
print('Farmer is producing patchy bubble pickles, YUM')
import patchy

pat = patchy.P_bubble(params)

pat.pickle_this()
print('\n')


print('***********************************************************')
print('Farmer is producing 21 cm pickles, YUM')
import patchy_reion_21 as p21

p_21 = p21.P_21_obs(params)

p_21.pickle_this()
print('\n')

print('***********************************************************')
print('Farmer is producing Lya pickles, YUM')
import theory_P_lyas_arinyo as plya

p_lya = plya.theory_P_lyas(params)

p_lya.pickle_this()
print('\n')

print('***********************************************************')
print('Farmer is done for today, here is a summary of your model')
print('\n')

print('***********************************************************')
print('21cmfast realization: ', params['fast-realization'])
print('21cmfast model: ', params['fast-model'])
print('Gadget realization: ', params['gadget-realization'])
print('Gadget model: ', params['gadget-model'])
print('AND a WDM mass [in keV] of ', params['m_wdm'])
