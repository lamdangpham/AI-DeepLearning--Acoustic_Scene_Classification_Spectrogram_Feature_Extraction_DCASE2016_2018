import numpy as np
import os
import re

def get_train_data(save_dir, data_dir):  
    mul_batch_num = 26  #TODO
    nF = 128 
    nT = 128 
    
    org_class_list = os.listdir(data_dir)
    class_list = []  #remove .file
    for nClass in range(0,len(org_class_list)):
        isHidden=re.match("\.",org_class_list[nClass])
        if (isHidden is None):
            class_list.append(org_class_list[nClass])
    class_num  = len(class_list)
    class_list = sorted(class_list)
    
    for nMulBatch in range(mul_batch_num):
    #for nMulBatch in range(1):
        file_save = save_dir + 'mulbatch_' + str(nMulBatch)
        print('\n===========  Start extracting from multi-batch {}; Output [{}]\n'.format(nMulBatch, file_save));  

        nImage=0
        for nClass in range(class_num):
        #for nClass in range(2):
            # 01/ Expected class
            expectedClass = np.zeros([1,class_num])
            expectedClass[0,nClass] = 1
        
            # 02/ Handle file directory 
            class_name = class_list[nClass]  
            input_dir = data_dir + class_name + '/' + 'group_' + str(nMulBatch + 1)

            org_file_list = os.listdir(input_dir)
            file_list = []  #remove .file
            for nFile in range(0,len(org_file_list)):
                isHidden=re.match("\.",org_file_list[nFile])
                if (isHidden is None):
                    file_list.append(org_file_list[nFile])
            file_num  = len(file_list)
            file_list = sorted(file_list)
            
            #--------------------------------------------------------------------------------  
            for nFile in range(file_num):
            #for nFile in range(5):
                # 01. Reading file
                file_name = file_list[nFile]
                file_open = input_dir + '/' + file_name
                
                data_str = np.load(file_open)  
                [nFreq, nTime] = np.shape(data_str)

                feat_num = np.floor(nTime/nT) 
                for m in range(int(feat_num)):
                    tStart = m*nT  
                    tStop  = tStart + nT
                    one_image = data_str[:,tStart:tStop]
                    [row_num, col_num] = np.shape(one_image)
                    one_image = np.reshape(one_image,[1,row_num,col_num])
                    if (nImage == 0):
                       seq_x = one_image
                       seq_y = expectedClass
                    else:            
                       seq_x = np.concatenate((seq_x, one_image), axis=0)  
                       seq_y = np.concatenate((seq_y,expectedClass), axis=0)  

                    # for test  
                    if(np.size(seq_x[nImage,:,:]) != nT*nF):  
                        print('ERROR: Frame {} [{}:{}] of {} [exit]\n'.format(m,tStart,tStop, nTime))               
                        np.shape(seq_x[nImage,:,:])  
                        exit()
                    nImage=nImage+1  
            print('Done extracting training features for class {}: [{}] \n'.format(nClass, class_name)) 
            
        # multiple of 100
        [feat_num, freq_num, time_num] = np.shape(seq_x)
        dim = int(np.ceil(feat_num/100 + 1)*100)
        for i in range(dim - feat_num):
            rd_ps = np.random.randint(feat_num)
            ins_seq_x = seq_x[rd_ps,:,:]
            ins_seq_y = seq_y[rd_ps,:]
            ins_seq_x = np.reshape(ins_seq_x,[1,freq_num, time_num])
            ins_seq_y = np.reshape(ins_seq_y,[1,class_num])
        
            seq_x = np.concatenate((seq_x, ins_seq_x), axis=0)
            seq_y = np.concatenate((seq_y, ins_seq_y), axis=0)
        
        # Random positon
        mul_seq_x = np.zeros((dim, freq_num, time_num))
        mul_seq_y = np.zeros((dim, class_num))
        
        kk = np.random.permutation(dim)
        for i in range(dim):
            mul_seq_x[i,:,:] = seq_x[kk[i],:,:]
            mul_seq_y[i,:]   = seq_y[kk[i],:]
        # Save file
        np.savez(file_save, seq_x=mul_seq_x, seq_y=mul_seq_y)
        print('============================== Done extracting training features for multi-batch {}\n'.format(nMulBatch))  
