# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 10:48:14 2017
2017-7-7 11:37:54
@author: wangxj
"""
import time
import numpy as np
import matplotlib.pyplot as plt
start =time.clock()

def initCenters(dataSet,k):
#    numSamples,dim=dataSet.shape
#    centers=np.zeros((k,dim))
#    for i in range(k):
#        index =int(np.random.uniform(0,numSamples))#random get k centers
#        centers[i,:]=dataSet[index,:]
    index=np.random.choice(dataSet.shape[0],k)
    centers=dataSet[index,:]
    print(centers)
    return centers

def Dist2Centers(sample,centers):
    k=centers.shape[0]
    dis2cents=np.zeros(k)
    for i in range(k):
        dis2cents[i]=np.sqrt(np.sum(np.power(sample-centers[i,:],2)))
    return dis2cents

def kmeans(dataSet,k,iterNum):
    numsamples=dataSet.shape[0]
    iterCount=0
    #clusterAssignment stores which cluster this sample belongs to,
    clusterAssignment=np.zeros(numsamples)
    clusterChanged=True

    ##step 1 initialize centers
    centers=initCenters(dataSet,k)
    while clusterChanged and iterCount<iterNum:
        clusterChanged=False
        iterCount+=1
        ##for each sample
        for i in range(numsamples):
            dis2cent=Dist2Centers(dataSet[i,:],centers)
            minindex=np.argmin(dis2cent)
            ##step 3 update its belonged cluster
            if clusterAssignment[i]!=minindex:
                clusterChanged=True
                clusterAssignment[i]=minindex
        ##step4 update centers
        for j in range(k):
            pointsInCluster=dataSet[np.nonzero(clusterAssignment[:]==j)[0]]
            centers[j,:]=np.mean(pointsInCluster,axis=0)
    print ('congrations,Cluster Achieved!')
    return centers,clusterAssignment

def showcluster(dataSet,k,centers,clusterAssignment):
    numsamples,dim=dataSet.shape
    mark=['or','ob','og','om']
    #draw all samples
    for i in range(numsamples):
        markindex=int(clusterAssignment[i])
        plt.plot(dataSet[i,0],dataSet[i,1],mark[markindex])
    mark=['Dr','Db','Dg','Dm']
    for i in range(k):
        plt.plot(centers[i,0],centers[i,1],mark[i],markersize=12)
    plt.show


def main():
#    step 1: load dataset
    print ('step 1: loading data...')
    dataSet=[]
    dataSetFile=open('./testSet.txt')
    for line in dataSetFile:
        linearr=line.strip().split('\t')
        dataSet.append([float(linearr[0]),float(linearr[1])])
#    step 2:clustering...
    print("step 2:clustering...")
    dataSet=np.mat(dataSet)
    k=4
    centers_result,clusterAssignment_result=kmeans(dataSet,k,100)

#    step 3:show the result
    print ('step 3: showing the result...')
    showcluster(dataSet,k,centers_result,clusterAssignment_result)

if __name__ == "__main__":
      main()

end=time.clock()
print ("Running duration: %f s" % (end-start))
