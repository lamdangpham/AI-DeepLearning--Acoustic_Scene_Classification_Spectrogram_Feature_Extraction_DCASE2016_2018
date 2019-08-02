desDirList = { './../11_01_gam_spec/data_train/'
               './../data_train/';
         };
               %'./../11_01_gam_spec/data_test/';
               %'./../data_test/';

[dir_num, nCol] = size(desDirList);
fileID  = fopen('./count.log','w');

for i =1:dir_num 
    desDir = char(desDirList(i));

    classStruct = dir(desDir);
    classList   = {classStruct.name};
    classList(strncmp(classList, '.', 1)) = [];  
    [row, classNum] = size(classList);
    
    totalNum = 0;
    for j=1:classNum
        fprintf(fileID,  '============ %s ==============\n', classList{j});
        fileDir    = [desDir,classList{j},'/'];
        fileStruct = dir(fileDir);
        fileList   = {fileStruct.name};
        fileList(strncmp(fileList, '.', 1)) = [];  
        [row, fileNum] = size(fileList);
        totalNum = totalNum + fileNum;
        fprintf(fileID,' %10d \n', fileNum);
    end 
    fprintf(fileID,  'Total : %d \n',totalNum);
    fprintf(fileID,  '\n');
end
fclose(fileID);
