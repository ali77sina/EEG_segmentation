import numpy as np
from seg_class import segment
inds = [[100,120],[200,250]]
data = np.zeros(shape = (5,500))
labels = np.zeros(500)
for i in inds:
  data[:,i[0]:i[1]] = 1
  labels[i[0]:i[1]] = 1
segs = segment(data,labels)
epochs = segs.epochs()
