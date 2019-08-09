# Feature Extraction Acoustic Scene Classification DCASE2016

This work builds scripts (Matlab & Python) to extract features (Spectrograms) from Acoustic Scene Classification (ASC) DCASE2016 dataset (http://www.cs.tut.fi/sgn/arg/dcase2016/index)

NOTES:
 + Using three kinds of spectrogram : Log-Mel (Librosa library), Gammatone filter(Auditory Toolbox), Constant Q-Transform (Librosa library)
 
 + Steps:
    + One-dimensional audio segment is transferred into entire spectrogram
        + 01_cqt(Python) 01_gam(Matlab) 01_mel(Python)
    
    + Shuffle files among diffrent classes to create multiple batches of data
        + 03_group_cqt 03_group_gam 03_group_mel  (All Matlab)
        
    + Entire spectrogram is split into patch with size at 128x128 that could be fed into backend learning model like CNN/RNN
        + 04_data_cqt 04_data_gam 04_data_mel  (All Python)
        
 + Training/Test audio files should be arranged:

   + data_train (Audio segment should be separated into certain Classes)
    
          |--train         
               |--<train_01>.wav               
               .....
          |--tram
               |--<tram_01>.wav
               ......
          
   + data_test (all audio segments in same folder)
    
          |--<train_01>.wav
          |--<tram_05>.wav
          |--<park_03>.wav
          .....
