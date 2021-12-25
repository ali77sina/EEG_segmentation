import numpy as np
inds = [[100,120],[200,250]]
data = np.zeros(shape = (5,500))
labels = np.zeros(500)
for i in inds:
  lab = np.random.random()*10
  lab = int(lab)
  data[:,i[0]:i[1]] = lab
  labels[i[0]:i[1]] = lab
segs = segment(data,labels,mode = 'multiple')
epochs = segs.epochs()
