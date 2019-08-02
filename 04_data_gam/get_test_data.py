import numpy as np
import os
import re

def get_test_data(save_dir, data_dir):  

    nF = 128  
    nT = 128  
    
    org_file_list = os.listdir(data_dir)
    file_list = []  #remove .file
    for nFile in range(0,len(org_file_list)):
        isHidden=re.match("\.",org_file_list[nFile])
        if (isHidden is None):
            file_list.append(org_file_list[nFile])
    file_num  = len(file_list)
    file_list = sorted(file_list)
    
    #--------------------------------------------------------------------------------  
    for nFile in range(file_num):
        nImage=0
        # 01. Reading file
        file_name = file_list[nFile]
        file_open = data_dir + '/' + file_name
        
        file_save = os.path.splitext(file_name)[0]
        file_save = save_dir + '/' + file_save
        
        data_str = np.load(file_open)  
        [nFreq, nTime] = np.shape(data_str)

        feat_num = np.floor(nTime/nT) 
        for m in range(int(feat_num)):
            tStart = m*nT  
            tStop  = tStart + nT
            one_image = data_str[:,tStart:tStop]
            [row_num, col_num] = np.shape(one_image)
            one_image = np.reshape(one_image,[1,row_num,col_num])
            if (m == 0):
               seq_x = one_image
            else:            
               seq_x = np.concatenate((seq_x, one_image), axis=0)  

            # for test  
            if(np.size(seq_x[nImage,:,:]) != nT*nF):  
                print('ERROR: Frame {} [{}:{}] of {} [exit]\n'.format(m,tStart,tStop, nTime))               
                np.shape(seq_x[nImage,:,:])  
                exit()
            nImage=nImage+1  
        np.savez(file_save, seq_x=seq_x)  

    print('\n============================== Done extracting testing features \n')  
    
