import sys
#sys.path.insert(0, '/home/cug/ldp7/.local/lib/python2.7/site-packages/librosa/')
import os
import re
import numpy as np
from general import *
import numpy as np
import librosa
import soundfile as sf

def get_data_mel_test(data_dir, store_dir, opt):
   
   n_mel = 128
   n_win = 1920 
   n_hop = 256  
   n_fft = 4096
   f_min = 10
   f_max = None
   htk   = False
   eps   = np.spacing(1)

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

      #mel
      stft_res = librosa.core.stft(wav, 
                                   n_fft      = n_fft,
                                   win_length = n_win,
                                   hop_length = n_hop,
                                   center     = True
                                  )

      mel_basis = librosa.filters.mel( sr     = fs,
                                       n_fft  = n_fft,
                                       n_mels = n_mel,
                                       fmin   = f_min,
                                       fmax   = f_max,
                                       htk    = htk
                                     )
      spec_data = np.dot(mel_basis, stft_res)
      spec_data = np.log(np.abs(spec_data))
      
      data01 = spec_data

      #Store data
      new_file_name = os.path.splitext(file_name)[0]
      file_des = store_dir + '/' + new_file_name
      np.save(file_des, data01)
   
   print ("==================== Done extracting testing feature \n\n")   
