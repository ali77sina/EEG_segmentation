
class segment:
  """
  Class to extract the indecies of the labels where they indicate
  some sort of an event happening.
  data: input data tensor
  label: continues labeling of the timeseries data
  mode = either 'binary' or 'multiple'
  """
  def __init__(self, data, label, mode = 'binary'):
    self.data = data
    self.label = label
    self.mode = mode
  
  def index_ext(self):
    inds = []
    start = False
    end = False
    start_ind = 0
    end_ind = 0
    l = len(self.label)
    if self.mode == 'binary':
      for num,i in enumerate(self.label):
        if num == 0 and i == 1:
          start = True
          start_ind = 0
        if num == l-1:
          if i == 1 and self.label[num-1] != 1:
            start = True
            start_ind = l-1
          if start:
            inds.append([start_ind, l-1])
          return inds
        if i == 1 and self.label[num-1] != 1:
          start = True
          start_ind = num
        if i == 1 and self.label[num+1] != 1:
          end = True
          end_ind = num
        if start and end:
          inds.append([start_ind, end_ind])
          start = False
          end = False
      return inds
    
    if self.mode == 'multiple':
      labels = set(self.label)
      for num,i in enumerate(self.label):
        event = False
        for j in labels:
          if j == i and j != 0:
            event = True
            event_id = j
            break
        if num == 0:
          start = True
        if event:
          if num == l-1:
            if i == event_id and self.label[num-1] != event_id:
              start = True
              start_ind = l-1
            if start:
              inds.append([[start_ind, l-1], event_id])
            return inds

            if start:
              inds.append([[start_ind, l-1], event_id])
            return inds
          if i == event_id and self.label[num-1] != event_id:
            start = True
            start_ind = num
          if i == event_id and self.label[num+1] != event_id:
            end = True
            end_ind = num
          if start and end:
            inds.append([[start_ind, end_ind],event_id])
            start = False
            end = False
      return inds
  
  def epochs(self):
    inds = self.index_ext()
    mode = self.mode
    epochs = []
    singe_ind = False
    if mode == 'binary':
      for i in inds:
        if i[0] == i[1]:
          singe_ind = True
          epochs.append(self.data[:, i[0]])
        else:
          epochs.append(self.data[:, i[0]:i[1]])
      if singe_ind:
        print("signle data points with labels detected")
      return epochs
    if mode == 'multiple':
      for i in inds:
        if i[0][0] == i[0][1]:
          singe_ind = True
          epochs.append(self.data[:, i[0][0]])
        else:
          epochs.append(self.data[:, i[0][0]: i[0][1]])
      if singe_ind:
        print("signle data points with labels detected")
      return epochs
