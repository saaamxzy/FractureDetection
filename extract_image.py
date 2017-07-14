import os
from shutil import copyfile

PathDicom = '../Images/'

lstFilesDCM = []  # create an empty list
c = 0
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            #lstFilesDCM.append(os.path.join(dirName,filename))
            f = os.path.join(dirName,filename)
            if os.path.getsize(f) > 10000:
	            copyfile(os.path.join(dirName,filename), 
	            	os.path.join('./images_to_read','test_' + str(c) + '.dcm'))
	            c+=1

