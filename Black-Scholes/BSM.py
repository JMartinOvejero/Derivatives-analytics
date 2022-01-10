#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_cell_magic('writefile', 'BSM.py', "\nimport math\nimport numpy as np\nimport matplotlib as mpl\nimport matplotlib.pyplot as plt\nmpl.rcParams['font.family']='serif'\nfrom scipy.integrate import quad\n\n#Auxiliary functions\n#===============================================================================================================\ndef dN(x):\n    return math.exp(-0.5*x**2)/math.sqrt(2*math.pi) #Prob. density function standard normal random variable x\n\ndef N(d):\n    return quad(lambda x:dN(x),-20,d,limit=50)[0]  #Cumulative density function of standard normal random variable x\n\ndef dif(St,K,t,T,r,sigma): #d1 function Black-Scholes\n    d1=(math.log(St/K)+(r+0.5*sigma**2)*(T-t))/(sigma*math.sqrt(T-t))\n    return(d1)\n\n#Valuation functions\n#===============================================================================================================\ndef BSM_call_value(St,K,t,T,r,sigma): #Black Scholes European call option value\n    #Parameters\n    #=====================================\n    St:float #stock/index level at time t\n    K:float #strike price\n    t:float #valuation date\n    T:float #date of maturity\n    r:float #risk-less short rate constant\n    sigma:float #volatility\n        \n    #Returns\n    #=====================================\n    \n    call_value: float #European call present value at t\n    \n    d1=dif(St,K,t,T,r,sigma)\n    d2=d1-sigma*math.sqrt(T-t)\n    call_value=St*N(d1)-math.exp(-r*(T-t))*K*N(d2)\n    return call_value\n\ndef BSM_put_value(St,K,t,T,r,sigma): #Black Scholes European put option value\n    \n    #Parameters\n    #=====================================\n    St:float #stock/index level at time t\n    K:float #strike price\n    t:float #valuation date\n    T:float #date of maturity\n    r:float #risk-less short rate constant\n    sigma:float #volatility\n        \n    #Returns\n    #=====================================\n    put_value: float #European put present value at t\n        \n    put_value=BSM_call_value(St,K,t,T,r,sigma) -St+math.exp(-r*(T-t))*K\n    \n    return put_value\n")


# In[ ]:




