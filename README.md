# EEG_segmentation
returning EEG epochs for continually labelled data sets (e.g. grasp and lift challenge on Kaggle) 

The class contains 2 functions:

index_ext(): extracting the start and end index for different events

epochs(): returns the epochs based on the said indecies.

The input data should be a numpy array, in shape: (No. Channels, Length), with a 1D array as label like [0,0,0,0,1,1,1,0,0,....]
it also accepts multiple events so each one should have unique event id (e.g. 1,2,3). 
