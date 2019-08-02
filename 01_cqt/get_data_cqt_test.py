import sys
import os
import re
import numpy as np
from general import *
import numpy as np
import librosa
import soundfile as sf

def get_data_cqt_test(data_dir, store_dir, opt):
   
   n_bins = 128
   bins_per_octave = 24
   fmin = 10
   hop_length = 256
   eps = np.spacing(1)

   # Get list of file
   org_file_name_list = os.listdir(data_dir)
   file_name_list = []  #remove .file
   for i in range(0,len(org_file_name_list)):
      isHidden=re.match("\.",org_file_name_list[i])
      if (isHidden is None):
         file_name_list.append(org_file_name_list[i])
   file_name_list = sorted(file_name_list)
   file_name_num  = len(file_name_list)

   # For every file in class
   for nFile in range(0, file_name_num):
      file_name  = file_name_list[nFile]
      file_open  = data_dir + '/' + file_name

      org_wav, fs = sf.read(file_open)
      wav = org_wav[:,0] + eps
     
      # CQT spectrogram
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
      file_des = store_dir + '/' + new_file_name
      np.save(file_des, data01)
   
   print ("==================== Done extracting testing feature \n\n")   
