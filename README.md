# Feature Extraction Acoustic Scene Classification DCASE2016

This work buils self scripts (Matlab & Python) to generate features (Spectrograms) from Acoustic Scene Classification (ASCD) CASE2016 dataset 

NOTES:
+ Using three spectrogram : Log-Mel, Gammatone filter, Constant Q-Transform
+ Steps:
    + One-dimensional audio segment is transferred into entire spectrogram
        + 01_cqt 01_gam 01_mel
    
    + Shuffle files among diffrent classes to create multipe batches of data
        + 03_group_cqt 03_group_gam 03_group_mel
        
    + Entire spectrogram is splited into patch sized 128x128 that could be fed into backend learning model like CNN/RNN
        + 04_data_cqt 04_data_gam 04_data_mel
        
+ Training/Test audio files should be arranged:

    + data_train (Classes should be separated)
    
          |--train         
               |--<train_01>.wav               
           .....
          |--tram
               |--<tram_01>.wav
    
    + data_test (no need to separated into classes inside)
          |--<train_01>.wav
          |--<tram_05>.wav
          |--<park_03>.wav
