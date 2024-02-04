# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:05:33 2020

@author: theron
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data1 = pd.read_csv("cvvf_modified_rejection_test1.txt", header = None)

data2 = pd.read_csv("cvvf_modified_rejection_test2.txt", header = None)

#input1 = input('Enter the baseload for plot: \n')
input2 = int(input('Enter which type of plot is needed: \n'))
if input2 == 2:
    input3 = int(input('Enter the baseload needed: \n'))
FinalBaselineAug2514 = pd.concat([pd.read_csv("FinalBaselineAug2514.txt", header = None), pd.read_csv("FinalBaselineAug2514.txt", header = None)], axis=1)
FinalBaselineAug2514.columns = list(range(0,2880))

FinalBaselineSep1614 = pd.concat([pd.read_csv("FinalBaselineSep1614.txt", header = None), pd.read_csv("FinalBaselineSep1614.txt", header = None)], axis=1)
FinalBaselineSep1614.columns = list(range(0,2880))

FinalBaselineSep2514 = pd.concat([pd.read_csv("FinalBaselineSep2514.txt", header = None), pd.read_csv("FinalBaselineSep2514.txt", header = None)], axis=1)
FinalBaselineSep2514.columns = list(range(0,2880))



if input2 == 0:
    t=np.array([np.arange(0,2880)/60])
    plt.figure()
    plt.rcParams.update({'font.size': 20})
    plt.plot(t.T,75*np.ones([2880,1]),'b')
    plt.xlabel('Time of Two Days (Hours)')
    plt.ylabel('Load Demand (kW)')
    plt.axis([0,48,0,200])
    plt.plot(t[0,:],FinalBaselineSep2514.iloc[0,:],'r')
    plt.grid()
    plt.show()




#Uncontrolled Charging Plots
if input2 == 1:
    t=np.array([np.arange(0,2880)/60])
    plt.figure()
    plt.rcParams.update({'font.size': 20})
    plt.plot(time.iloc[0,:]/60,75*np.ones([2880,1]),'b')
    plt.xlabel('Time of Two Days (Hours)')
    plt.ylabel('Load Demand (kW)')
    plt.axis([0,48,0,200])
    for i in np.arange(0,2255):
        plt.plot(t[0,:],  transformer_profile[i,:]+base[0,:],'g')
        plt.plot(t[0,:],base[0,:],'r')
    plt.grid()
    plt.show()

#CVVF Charging Plots
elif input2 == 2:
    t=np.array([np.arange(0,2880)/60])
    if input3 == 1:
        plt.figure()
        plt.rcParams.update({'font.size': 20})
        plt.plot(t.T,75*np.ones([2880,1]),'b')
        plt.plot(t.T,45.79*np.ones([2880,1]),'k')
        plt.xlabel('Time of Two Days (Hours)')
        plt.ylabel('Load Demand (kW)')
        plt.axis([0,48,0,200])
        for i in np.arange(0,2255):
            plt.plot(t[0,:],  transformer_profile[i,:],'g')
            plt.plot(t[0,:],FinalBaselineAug2514.iloc[0,:],'r')
        plt.grid()
        plt.show()
        
    elif input3 == 2:
        plt.figure()
        plt.rcParams.update({'font.size': 20})
        plt.plot(t.T,75*np.ones([2880,1]),'b')
        plt.plot(t.T,112.35*np.ones([2880,1]),'k')
        plt.xlabel('Time of Two Days (Hours)')
        plt.ylabel('Load Demand (kW)')
        plt.axis([0,48,0,200])
        for i in np.arange(0,2255):
            plt.plot(t[0,:],  transformer_profile[i,:],'g')
            plt.plot(t[0,:],FinalBaselineSep1614.iloc[0,:],'r')
        plt.grid()
        plt.show()
        
    else:
        plt.figure()
        plt.rcParams.update({'font.size': 20})
        plt.plot(t.T,75*np.ones([2880,1]),'b')
        plt.plot(t.T,64.47*np.ones([2880,1]),'k')
        plt.xlabel('Time of Two Days (Hours)')
        plt.ylabel('Load Demand (kW)')
        plt.axis([0,48,0,200])
        for i in np.arange(0,2255):
            plt.plot(t[0,:],  transformer_profile[i,:],'g')
            plt.plot(t[0,:],FinalBaselineSep2514.iloc[0,:],'r')
        plt.grid()
        plt.show()

## SRVF && RIVF Charging Plots
elif input2 == 3:
    t=np.array([np.arange(0,2880)/60])
    plt.figure()
    plt.rcParams.update({'font.size': 20})
    plt.plot(t.T,75*np.ones([2880,1]),'b')
    plt.xlabel('Time of Two Days (Hours)')
    plt.ylabel('Load Demand (kW)')
    plt.axis([0,48,0,200])
    for i in np.arange(1804,2255):
        plt.plot(t[0,:], transformer_profile[i,:],'g')
        plt.plot(t[0,:],base.iloc[0,:],'r')
    plt.grid()
    plt.show()

##MLVF Carging PLots
else:
    fig = plt.figure() 
    plt.plot(time.iloc[0,:]/60,75*np.ones([2880,1]),'b')
    plt.rcParams.update({'font.size': 20})
    plt.xlabel('Time of Two Days (Hours)')
    plt.ylabel('Load Demand (kW)')
    plt.axis([0,48,0,200])
    for i in np.arange(1804,2255):
        plt.plot(time.iloc[0,:]/60, transformer_profile[i,:],'g')
        plt.plot(time.iloc[0,:]/60, base.iloc[0,:],'r')
    plt.grid()
    plt.show()
    
    


