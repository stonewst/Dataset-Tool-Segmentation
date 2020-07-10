#!/bin/bash


# ----- VOC2011 -----
# train & val
wget -c -O data/VOC2011_TrainVal.tar "http://host.robots.ox.ac.uk/pascal/VOC/voc2011/VOCtrainval_25-May-2011.tar"

mkdir -p "data/VOC/VOC2011"
tar -xvf data/VOC2011_TrainVal.tar -C "data/VOC/VOC2011"
mv data/VOC/VOC2011/TrainVal/VOCdevkit/VOC2011/* "data/VOC/VOC2011/TrainVal"
rm -rf data/VOC/VOC2011/TrainVal/VOCdevkit

# test
wget --post-data="username=yourname&password=yourpassword&submit=login" --save-cookies=voc_cookie.txt --keep-session-cookies http://host.robots.ox.ac.uk:8080/accounts/login/?next=/
wget -c -O data/VOC2011_Test.tar --load-cookies=voc_cookie.txt --keep-session-cookies "http://host.robots.ox.ac.uk:8080/eval/downloads/VOC2011test.tar"
rm -rf voc_cookie.txt
rm -rf index.html?next=%2F

tar -xvf data/VOC2011_Test.tar -C "data/VOC/VOC2011"
mv data/VOC/VOC2011/Test/VOCdevkit/VOC2011/* "data/VOC/VOC2011/Test"
rm -rf data/VOC/VOC2011/Test/VOCdevkit


# ----- VOC2012 -----
# train & val
wget -c -O data/VOC2012_TrainVal.tar "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar"

mkdir -p "data/VOC/VOC2012"
tar -xvf data/VOC2012_TrainVal.tar -C "data/VOC/VOC2012"
mkdir -p "data/VOC/VOC2012/TrainVal"
mv data/VOC/VOC2012/VOCdevkit/VOC2012/* "data/VOC/VOC2012/TrainVal"
rm -rf data/VOC/VOC2012/VOCdevkit

# test
wget --post-data="username=yourname&password=yourpassword&submit=login" --save-cookies=voc_cookie.txt --keep-session-cookies http://host.robots.ox.ac.uk:8080/accounts/login/?next=/
wget -c -O data/VOC2012_Test.tar --load-cookies=voc_cookie.txt --keep-session-cookies "http://host.robots.ox.ac.uk:8080/eval/downloads/VOC2012test.tar"
rm -rf voc_cookie.txt
rm -rf index.html?next=%2F

tar -xvf data/VOC2012_Test.tar -C "data/VOC/VOC2012"
mkdir -p "data/VOC/VOC2012/Test"
mv data/VOC/VOC2012/VOCdevkit/VOC2012/* "data/VOC/VOC2012/Test"
rm -rf data/VOC/VOC2012/VOCdevkit


# ----- SBD -----
# train & val
wget --no-check-certificate -c -O data/SBD_benchmark.tgz "http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/semantic_contours/benchmark.tgz"

mkdir -p "data/VOC/SBD"
tar -xvf data/SBD_benchmark.tgz -C "data/VOC/SBD"

# convert label.mat to .png
python3 py/voc.py SBD_label_mat2png

# generate VOC2011 subval.txt and VOC2012 subval.txt
python3 py/voc.py generate_VOC2011_VOC2012_subval_txt


# ----- VOC2012AUG -----
# generate train_aug.txt, val_aug.txt, trainval_aug.txt
python3 py/voc.py generate_VOC2012AUG_txt

# generate label.png of VOC2012AUG train¡¢val set
python3 py/voc.py generate_VOC2012AUG_label_folder


