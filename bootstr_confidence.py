def bootstr_confidence(sample,reps):
    import numpy as np
    
    bias_b=np.zeros(reps)    
    std_b=np.zeros(reps)
    rms_b=np.zeros(reps)
    xb = np.random.choice(sample, (len(sample), reps), replace=True)
    for i in range(reps): 
        bias_b[i]=np.mean(xb[:,i])
        std_b[i]= np.std(xb[:,i])
        rms_b[i]=np.sqrt(bias_b[i]**2+std_b[i]**2)
    
    #plt.hist(bias_b)
    bias_conf=np.std(bias_b)
    std_conf=np.std(std_b)
    rms_conf=np.std(rms_b)
    bias=np.mean(bias_b)
    std=np.mean(std_b)
    rms=np.mean(rms_b)

    return bias,std,rms,bias_conf,std_conf,rms_conf
