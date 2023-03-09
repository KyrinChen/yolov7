import os
paths= "./images/train/"
f=open('val.txt', 'w')
filenames=os.listdir(paths)
filenames.sort()
for filename in filenames:
 
    out_path="D:/Downloads/tzb/yolov7/datasets/defect/images/train/" + filename
    print(out_path)
    f.write(out_path+'\n')
f.close()