Repository for "Unveiling the dark matter nature with reionization relics"
==========================================================================

This repository contains the data and code used in the work "Unveiling the dark matter nature with reionization relics".

## Code requirements
__classy__ (which also requires __cython__)

https://cobaya.readthedocs.io/en/latest/theory_class.html

## Meaning in the filename

### [realization]
We have 4 realizations (r1-r4) and the average of them (ave).

### [model]
First kind: **[DM]\_[sigma8]** with DM={3keV,4keV,6keV,9keV,cdm}, sigma8={s8(0.8159),sminus(0.7659),splus(0.8659)}, zeta=30.

Second kind: **zeta\_[p#]** with p#=p1-p8. Used for 3-parameter MCMC analysis.

p1=(cdm,sigma8=0.7659,zeta=20)  

p2=(cdm,sigma8=0.7659,zeta=40)

p3=(cdm,sigma8=0.8659,zeta=20)

p4=(cdm,sigma8=0.8659,zeta=40)

p5=(3keV,sigma8=0.7659,zeta=20)

p6=(3keV,sigma8=0.7659,zeta=40)

p7=(3keV,sigma8=0.8659,zeta=20)

p8=(3keV,sigma8=0.8659,zeta=40)


## data/

- dNdzdg_QSO.dat

&emsp;&emsp;DESI quasar luminosity function

- sn-spec-lya-g[magnitude]-t4000.dat

&emsp;&emsp;DESI spectrograph performance

- skalow1_density_baseline.csv
  
&emsp;&emsp;reference: Figure 6 in arXiv:1410.7393

&emsp;&emsp;e.g. u/nu [MHz^-1] n(u)*nu^2 [MHz^2]

&emsp;&emsp;0.11903168444605486 63095.73444801943

&emsp;&emsp;......

&emsp;&emsp;u = k_transverse * comving_distance / (2*pi), n(u): baseline number density

### data/21cmFAST/

- cross_21cm_[realization]_[model].txt
  
&emsp;&emsp;cross-power spectrum (dimensionless, P(k)\*k^3/(2\*pi^2)) of matter density and neutral hydrogen fraction (xHI) generated by 21cmFAST

&emsp;&emsp;e.g. redshift k(Mpc^-1) dimensionless power spectrum

&emsp;&emsp;5.e+00 1.570796e-02 0.e+00

&emsp;&emsp;......

- matter_cross_21cm_[realization]_[model].txt
  
&emsp;&emsp;cross-power spectrum of matter density and xHI after implementing biasing procedure for large-scale mode

&emsp;&emsp;e.g. redshift k(Mpc^-1) P(k)(Mpc^3)

&emsp;&emsp;5.000000e+00 1.000000e-03 0.000000e+00

&emsp;&emsp;......

- xH_21cm_[realization]_[model].txt
  
&emsp;&emsp;evolution of volume-weighted global neutral hydrogen fraction

&emsp;&emsp;e.g. redshift xHI

&emsp;&emsp;3.537197473298937211e+01 9.997801780700683594e-01

&emsp;&emsp;......


### data/gadget/

- transp_gadget_[realization]_[model]_f.txt
  
&emsp;&emsp;column 1-7: psi(z_re,z_obs) in Equation (4), relative transparency of gas reionized at z_re compared to gas reionized at z=8 in CDM

&emsp;&emsp;column 8: radiation bias b_Gamma in Equation (2)

&emsp;&emsp;e.g.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;psi(z_re=6) psi(z_re=7) psi(z_re=8) psi(z_re=9) psi(z_re=10) psi(z_re=11) psi(z_re=12) b_Gamma
          
&emsp;&emsp;z_obs=2.0&emsp;0.01809 -0.00997 -0.01894 -0.02173 -0.02280 -0.02350 -0.02405 0.08886

&emsp;&emsp;z_obs=2.5&emsp;0.04902 0.01060 -0.00081 -0.00319 -0.00236 -0.00168 -0.00201 0.15411

&emsp;&emsp;z_obs=3.0&emsp;......

&emsp;&emsp;z_obs=3.5&emsp;......

&emsp;&emsp;z_obs=4.0&emsp;......



## pickles/

[fast_realization]: realization of 21cmFAST simulation; [gadget_realization]: realization of Gadget simulation.

- p_mpsi_[fast_realization]\_[model]\_[gadget_realization]\_[model].pkl
  
&emsp;&emsp;pickle of the function P_m_psi(z_obs, k) where P_m_psi is the cross-power spectrum of matter density and psi (IGM transparency), Equation (1) for Lyman alpha forest

- p_mXi_[fast_realization]\_[model]\_[gadget_realization]\_[model].pkl
  
&emsp;&emsp;pickle of the function P_m_Xi(z_obs, k) where P_m_Xi is the cross-power spectrum of matter density and Xi (HI density fluctuation), Equation (1) for 21 cm IM

- pat_[realization]_[model].pkl
  
&emsp;&emsp;pickle of the interpolator of P_m_xHI(z, k) where P_m_xHI is the cross-power spectrum of matter density and xHI in Equation (1)

- psi_[realization]_[model].pkl
  
&emsp;&emsp;pickle of the interpolator of psi(z_re,z_obs) in Equation (4)

- rho_HI_func_[realization]_[model].pkl
  
&emsp;&emsp;pickle of the interpolator of rho_HI(z_re,z_obs) in Equation (9)


## code/

Each .py file is described at the beginning of the file.

Note that the ncdm.py and scales.py are adopted from https://github.com/jstuecker/ncdm-mass-functions to calculate WDM halo mass function. **Reference: arXiv:2109.09760**

In general,

- theory_P_lyas_arinyo.py

&emsp;&emsp;calculates the 3D lyman alpha forest power spectrum:

&emsp;&emsp;P_F^3D(z,k_Mpc,mu) = LyaLya_base_Mpc_norm(z, k_Mpc, mu) + LyaLya_reio_Mpc_norm(z, k_Mpc, mu),

&emsp;&emsp;where LyaLya_base_Mpc_norm() is the first term on the RHS of Equation (6),

&emsp;&emsp;and LyaLya_reio_Mpc_norm() is the second term on the RHS of Equation (6), which is the leading-order term of the impact of reionization on the 3D lyman alpha forest power spectrum.

- theory_P_21cm.py

&emsp;&emsp;calculates the 3D 21 cm IM power spectrum:

&emsp;&emsp;P3D_21_Mpc_norm(z, k_Mpc, mu) = HIHI_base_Mpc_norm(z, k_Mpc, mu) + HIHI_reio_Mpc_norm(z, k_Mpc, mu),

&emsp;&emsp;where HIHI_base_Mpc_norm() is the first term on the RHS of Equation (15) divided by Tb^2, i.e. (b_HI+mu^2\*f)^2\*P_m;

&emsp;&emsp;HIHI_reio_Mpc_norm() is the second term on the RHS of Equation (15) divided by Tb^2, i.e. 2*(b_HI+mu^2*f)*P_mXi.

- mcmc_lya.py, mcmc_21cm.py, mcmc_combine.py

&emsp;&emsp; 2-parameter mcmc analysis in Figure 3 (m_WDM,sigma8)

- mcmc3d_lya.py, mcmc3d_21cm.py, mcmc3d_combine.py

&emsp;&emsp; 3-parameter mcmc analysis in Figure A6 (m_WDM,sigma8,zeta)

