# Feature Extraction Acoustic Scene Classification DCASE2016

This work builds scripts (Matlab & Python) to extract features (Spectrograms) from Acoustic Scene Classification (ASC) DCASE2016 dataset (http://www.cs.tut.fi/sgn/arg/dcase2016/index)

Refer the papers stored in folder '05_Doc':
   + "A Robust Framework For Acoustic Scene Classification.pdf" In "Interspeech 2019 Conference"
   + "Bag-of-Features Models Based on C-DNN Network for Acoustic Scene Classification.pdf" in "AES 2019 Conference"
   
# NOTES:
 + Using three kinds of spectrogram : Log-Mel (Librosa library), Gammatone filter(Auditory Toolbox), Constant Q-Transform (Librosa library)
 
 + Runing Steps:
    + One-dimensional audio segment is transferred into entire spectrogram
        + 01_cqt(Python) 
        + 01_gam(Matlab) 
        + 01_mel(Python)
    
    + Shuffle files among diffrent classes to create multiple batches of data
        + 03_group_cqt (Matlab) 
        + 03_group_gam (Matlab) 
        + 03_group_mel (Matlab) 
        
    + Entire spectrogram is split into patch with size at 128x128 that could be fed into backend learning models 
        + 04_data_cqt (Python)
        + 04_data_gam (Python)
        + 04_data_mel (Python)
        
 + Training/Test audio segments should be arranged (This setup does not include audio segments):

   + data_train (Training audio segment should be separated into certain Classes)
    
          |--train         
               |--<train_01>.wav               
               .....
          |--tram
               |--<tram_01>.wav
               ......
          
   + data_test (all test audio segments are put into same folder 'data_test')
    
          |--<train_01>.wav
          |--<tram_05>.wav
          |--<park_03>.wav
          .....
