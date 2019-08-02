import sys
import os
import re
import numpy as np
from general import *
import numpy as np
import librosa
import soundfile as sf
#from matplotlib.pyplot import imshow
#import matplotlib.pyplot as plt

def get_data_cqt_train(data_dir, store_dir, opt):
   
   n_bins = 128
   bins_per_octave = 24
   fmin = 10
   hop_length = 256
   eps = np.spacing(1)

   # Get list of class
   org_class_name_list = os.listdir(data_dir)
   class_name_list = []
   for i in range(0,len(org_class_name_list)):
      isHidden=re.match("\.",org_class_name_list[i])
      if (isHidden is None):
         class_name_list.append(org_class_name_list[i])
   class_name_list = sorted(class_name_list)        
   class_name_num  = len(class_name_list)

   # For every class
   for nClass in range(0, class_name_num): 
   #for nClass in range(0, 1): 
       #3.1 Collect the file Name List
       class_name  = class_name_list[nClass]
       class_open  = data_dir + class_name + '/'

       class_store = store_dir + '/' + class_name
       if not os.path.exists(class_store):
          os.makedirs(class_store)

       org_file_name_list = os.listdir(class_open)
       file_name_list = []  #remove .file
       for i in range(0,len(org_file_name_list)):
          isHidden=re.match("\.",org_file_name_list[i])
          if (isHidden is None):
             file_name_list.append(org_file_name_list[i])
       file_name_list = sorted(file_name_list)
       file_name_num  = len(file_name_list)

       # For every file in class
       for nFile in range(0, file_name_num):
       #for nFile in range(0, 1):
          file_name  = file_name_list[nFile]
          file_open  = class_open + file_name

          org_wav, fs = sf.read(file_open)
          wav = org_wav[:,0] + eps
         
          ##CQT spectrogram
          spec_data = np.abs(librosa.cqt(wav, 
                                         sr     = fs,
                                         fmin   = fmin,
                                         n_bins = n_bins,
                                         bins_per_octave = bins_per_octave,
                                         hop_length = hop_length
                                        ))
          data01 = spec_data

          #Store data
          new_file_name = os.path.splitext(file_name)[0]
          file_des = class_store + '/' + new_file_name
          np.save(file_des, data01)
      
       if opt==1:
          print ("Done extracting training feature for class {} \n".format(nClass))   
       else:   
          print ("Done extracting testing feature for class {} \n".format(nClass))   
          
   if opt==1:
      print ("==================== Done extracting training feature \n\n")   
   else:
      print ("==================== Done extracting testing feature \n\n")   
        


