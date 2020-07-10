# Dataset-Tool-Segmentation

**This is an Auto-Process Tool to Download and Reorganize some Common Segmentation Datasets**

&nbsp;

### Available Datasets are as follows:
- [x] VOC2011
- [x] VOC2012
- [x] SBD
- [x] VOC2012AUG
- [x] CamVid

&nbsp;

### VOC  (VOC2011 & VOC2012 & SBD & VOC2012AUG)

&emsp;&emsp;**It can achieve the following terms：**
+ Auto Download VOC2011, VOC2012, SBD dataset from the official website
+ Reorganize the Downloaded dataset in a clear manner
+ Convert SBD Ground-truth Annotation files from .mat to .png
+ Generate "subval.txt" for VOC2011 and VOC2012
+ Generate "train_aug.txt", "val_aug.txt" and "trainval_aug.txt" for VOC2012AUG
+ Collect the Ground-truth Annotation .png files of VOC2012AUG into one folder for convenient post-processing

&emsp;&emsp;**Follow steps below:**  

```
1 You need to register an account at http://host.robots.ox.ac.uk:8080/accounts/login/?next=/ to download the test set
2 Change "yourname" and "yourpassword" in lines 14 and 35 of voc.sh to your registered username and password
3 cd Dataset-Tool-Segmentation
4 sh voc.sh 
```
After these steps, the dataset is located in './data/' 

&nbsp;

### CamVid

&emsp;&emsp;**It can achieve the following terms：**
+ Auto Download CamVid Dataset for Segmentation(11 semantic classes)
+ Generate "train.txt", "val.txt", "trainval.txt" and "test.txt"

&emsp;&emsp;**Follow steps below:**  
```
1 cd Dataset-Tool-Segmentation
2 sh camvid.sh
```
After these steps, the dataset is located in './data/' 


