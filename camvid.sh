#!/bin/bash


# ----- CamVid -----

git clone https://github.com/StoneWST/CamVid-for-Segmentation.git "data/CamVid"

rm -rf "data/CamVid/.git"
rm -rf "data/CamVid/LICENSE"
rm -rf "data/CamVid/README.md"

# generate txt file 
python3 py/camvid.py gen_camvid_txt