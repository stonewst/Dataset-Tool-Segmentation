import os
import collections
import numpy as np
from PIL import Image
import scipy.io as io
from shutil import copyfile
import fire


def check_VOC2011_contain_SBD_or_not():
    SBD_img_path = "data/VOC/SBD/benchmark_RELEASE/dataset/img/"
    SBD_img_list = os.listdir(SBD_img_path)
    print('SBD images num in "img" folder: %d' % len(SBD_img_list))

    VOC2011_img_path = "data/VOC/VOC2011/TrainVal/JPEGImages/"
    VOC2011_img_list = os.listdir(VOC2011_img_path)
    print('VOC2011 images num in "JPEGImages" folder: %d' % len(VOC2011_img_list))

    for i in SBD_img_list:
        try:
            if i in VOC2011_img_list:
                pass
        except:
            print("SBD image %s is not in VOC2011 JPEGImages folder" % i)
    print("All the SBD images are contained in VOC2011 JPEGImages folder")


def check_img_of_11_12_same_or_not():
    VOC2011_img_path = "data/VOC/VOC2012/TrainVal/JPEGImages/"
    VOC2011_img_list = os.listdir(VOC2011_img_path)
    print('VOC2011 images num in "JPEGImages" folder: %d' % len(VOC2011_img_list))

    VOC2012_img_path = "data/VOC/VOC2012/TrainVal/JPEGImages/"
    VOC2012_img_list = os.listdir(VOC2011_img_path)
    print('VOC2012 images num in "JPEGImages" folder: %d' % len(VOC2012_img_list))

    for i in VOC2012_img_list:
        try:
            if i in VOC2011_img_list:
                pass
        except:
            print("VOC2012 image %s is not in VOC2011 JPEGImages folder" % i)
    print("All the VOC2012 images are contained in VOC2011 JPEGImages folder")


def check_SBD_VOC2012_repeat():
    # --- SBD ---
    SBD_train_txt_file = 'data/VOC/SBD/benchmark_RELEASE/dataset/train.txt'
    SBD_val_txt_file = 'data/VOC/SBD/benchmark_RELEASE/dataset/val.txt'

    SBD_train_list = []
    for idx in open(SBD_train_txt_file):
        idx = idx.strip()
        SBD_train_list.append(idx)
    print('\nSBD train num: %d' % len(SBD_train_list))

    SBD_val_list = []
    for idx in open(SBD_val_txt_file):
        idx = idx.strip()
        SBD_val_list.append(idx)
    print('SBD val num: %d' % len(SBD_val_list))

    # --- VOC2012 ---
    VOC2012_train_txt_file = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/train.txt"
    VOC2012_val_txt_file = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/val.txt"

    VOC2012_train_list = []
    for idx in open(VOC2012_train_txt_file):
        idx = idx.strip()
        VOC2012_train_list.append(idx)
    print('\nVOC2012 train num: %d' % len(VOC2012_train_list))

    VOC2012_val_list = []
    for idx in open(VOC2012_val_txt_file):
        idx = idx.strip()
        VOC2012_val_list.append(idx)
    print('VOC2012 val num: %d' % len(VOC2012_val_list))

    # ----- begin check repeat -----
    num = 0
    for i in VOC2012_train_list:
        if i not in SBD_train_list:
            num += 1
    print('\n%d images of VOC2012 train set are not contained in SBD train set' % num)

    num = 0
    for i in VOC2012_train_list:
        if i in SBD_train_list:
            num += 1
    print('\n%d images of VOC2012 train set are contained in SBD train set' % num)

    num = 0
    for i in SBD_val_list:
        if i in VOC2012_val_list:
            num += 1
    print('\n%d images of SBD val set are contained in VOC2012 val set' % num)


def check_SBD_clspng():
    SBD_clspng_dir = 'data/VOC/SBD/benchmark_RELEASE/dataset/cls_png'
    clspng_name_list = os.listdir(SBD_clspng_dir)
    clspng_path_list = []
    for name in clspng_name_list:
        clspng_path_list.append(os.path.join(SBD_clspng_dir, name))

    # open png
    for i in clspng_path_list:

        lbl = Image.open(i)
        lbl = np.array(lbl, dtype=np.int32)
        print(lbl.shape)
        print(lbl)


def assert_VOC2012AUG_same():
    our_dir = "data/VOC/VOC2012/TrainVal/SegmentationClassAUG/"
    other_dir = "data/VOC/VOC2012/TrainVal/SegmentationClassAug/"

    our_name_list = os.listdir(our_dir)
    other_name_list = os.listdir(other_dir)
    our_name_list.sort()
    other_name_list.sort()

    our_path_list = []
    for name in our_name_list:
        our_path_list.append(os.path.join(our_dir, name))

    other_path_list = []
    for name in other_name_list:
        other_path_list.append(os.path.join(other_dir, name))

    for i, j in zip(our_path_list, other_path_list):
        lbl1 = Image.open(i)
        lbl1 = np.array(lbl1, dtype=np.int32)

        lbl2 = Image.open(j)
        lbl2 = np.array(lbl2, dtype=np.int32)

        print(lbl1.shape, 'vs', lbl2.shape)
        assert (lbl1 == lbl2).all()



def SBD_label_mat2png():
    files = collections.defaultdict(list)
    palette = [255] * (256 * 3)
    palette[:(21 * 3)] = [0, 0, 0, 128, 0, 0, 0, 128, 0, 128, 128, 0, 0, 0, 128,
                          128, 0, 128, 0, 128, 128, 128, 128, 128, 64, 0, 0, 192, 0, 0,
                          64, 128, 0, 192, 128, 0, 64, 0, 128, 192, 0, 128, 64, 128, 128,
                          192, 128, 128, 0, 64, 0, 128, 64, 0, 0, 192, 0, 128, 192, 0, 0, 64, 128]

    SBD_root_dir = 'data/VOC/SBD/benchmark_RELEASE/dataset'

    # --- get all file list ---
    for split in ['train', 'val']:
        txt_file = os.path.join(SBD_root_dir, '%s.txt' % split)
        for idx in open(txt_file):
            idx = idx.strip()
            img_path = os.path.join(SBD_root_dir, 'img/%s.jpg' % idx)  # image file path
            lbl_mat_path = os.path.join(SBD_root_dir, 'cls/%s.mat' % idx)  # label mat file path
            files[split].append({
                'img_path': img_path,
                'lbl_mat_path': lbl_mat_path,
                'former_name': idx,
            })
    files['trainval'] = files['train'] + files['val']

    # --- convert mat to png ---
    cls_png_dir = os.path.join(SBD_root_dir, 'cls_png')
    if not os.path.exists(cls_png_dir):
        os.makedirs(cls_png_dir)

    for d in files['trainval']:
        # load label
        lbl_mat_path = d['lbl_mat_path']
        former_name = d['former_name']
        lbl_mat = io.loadmat(lbl_mat_path)
        lbl = lbl_mat['GTcls'][0]['Segmentation'][0].astype(np.uint8)
        lbl[lbl == 255] = -1
        lbl_img = Image.fromarray(lbl, 'P')
        lbl_img.putpalette(palette)
        lbl_img.save(os.path.join(cls_png_dir, '%s.png' % former_name))


def generate_VOC2011_VOC2012_subval_txt():
    # --- SBD ---
    SBD_train_txt_file = 'data/VOC/SBD/benchmark_RELEASE/dataset/train.txt'
    SBD_val_txt_file = 'data/VOC/SBD/benchmark_RELEASE/dataset/val.txt'

    SBD_train_list = []
    for idx in open(SBD_train_txt_file):
        idx = idx.strip()
        SBD_train_list.append(idx)
    SBD_train_num = len(SBD_train_list)
    print('\nSBD train num: %d' % SBD_train_num)

    SBD_val_list = []
    for idx in open(SBD_val_txt_file):
        idx = idx.strip()
        SBD_val_list.append(idx)
    SBD_val_num = len(SBD_val_list)
    print('SBD val num: %d' % SBD_val_num)

    # --- VOC2011 ---
    VOC2011_train_txt_file = "data/VOC/VOC2011/TrainVal/ImageSets/Segmentation/train.txt"
    VOC2011_val_txt_file = "data/VOC/VOC2011/TrainVal/ImageSets/Segmentation/val.txt"

    VOC2011_train_list = []
    for idx in open(VOC2011_train_txt_file):
        idx = idx.strip()
        VOC2011_train_list.append(idx)
    VOC2011_train_num = len(VOC2011_train_list)
    print('\nVOC2011 train num: %d' % VOC2011_train_num)

    VOC2011_val_list = []
    for idx in open(VOC2011_val_txt_file):
        idx = idx.strip()
        VOC2011_val_list.append(idx)
    VOC2011_val_num = len(VOC2011_val_list)
    print('VOC2011 val num: %d' % VOC2011_val_num)

    # --- VOC2012 ---
    VOC2012_train_txt_file = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/train.txt"
    VOC2012_val_txt_file = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/val.txt"

    VOC2012_train_list = []
    for idx in open(VOC2012_train_txt_file):
        idx = idx.strip()
        VOC2012_train_list.append(idx)
    VOC2012_train_num = len(VOC2012_train_list)
    print('\nVOC2012 train num: %d' % VOC2012_train_num)

    VOC2012_val_list = []
    for idx in open(VOC2012_val_txt_file):
        idx = idx.strip()
        VOC2012_val_list.append(idx)
    VOC2012_val_num = len(VOC2012_val_list)
    print('VOC2012 val num: %d' % VOC2012_val_num)

    # ----- 1. begin generate VOC2011_subval -----
    VOC2011_subval_list = VOC2011_val_list.copy()
    repeat_num = 0
    for i in VOC2011_val_list:
        if i in SBD_train_list:
            repeat_num += 1
            VOC2011_subval_list.remove(i)
    print('\n%d images of VOC2011 val set are contained in SBD train set' % repeat_num)

    txt_path = "data/VOC/VOC2011/TrainVal/ImageSets/Segmentation/subval.txt"
    list2txt(VOC2011_subval_list, txt_path)

    # ----- 2. begin generate VOC2012_subval -----
    VOC2012_subval_list = VOC2012_val_list.copy()
    repeat_num = 0
    for i in VOC2012_val_list:
        if i in SBD_train_list:
            repeat_num += 1
            VOC2012_subval_list.remove(i)
    print('\n%d images of VOC2012 val set are contained in SBD train set' % repeat_num)
    txt_path = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/subval.txt"
    list2txt(VOC2012_subval_list, txt_path)


def generate_VOC2012AUG_txt():
    # --- SBD ---
    SBD_train_txt_file = 'data/VOC/SBD/benchmark_RELEASE/dataset/train.txt'
    SBD_val_txt_file = 'data/VOC/SBD/benchmark_RELEASE/dataset/val.txt'

    SBD_train_list = []
    for idx in open(SBD_train_txt_file):
        idx = idx.strip()
        SBD_train_list.append(idx)
    print('\nSBD train num: %d' % len(SBD_train_list))

    SBD_val_list = []
    for idx in open(SBD_val_txt_file):
        idx = idx.strip()
        SBD_val_list.append(idx)
    print('SBD val num: %d' % len(SBD_val_list))

    # --- VOC2012 ---
    VOC2012_train_txt_file = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/train.txt"
    VOC2012_val_txt_file = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/val.txt"

    VOC2012_train_list = []
    for idx in open(VOC2012_train_txt_file):
        idx = idx.strip()
        VOC2012_train_list.append(idx)
    print('\nVOC2012 train num: %d' % len(VOC2012_train_list))

    VOC2012_val_list = []
    for idx in open(VOC2012_val_txt_file):
        idx = idx.strip()
        VOC2012_val_list.append(idx)
    print('VOC2012 val num: %d' % len(VOC2012_val_list))

    # ----- gen aug txt -----
    VOC2012AUG_train_list = VOC2012_train_list
    for i in SBD_train_list:
        if i not in VOC2012AUG_train_list:
            VOC2012AUG_train_list.append(i)

    for i in SBD_val_list:
        if i not in VOC2012AUG_train_list:
            VOC2012AUG_train_list.append(i)

    remove_list = []
    for i in VOC2012AUG_train_list:
        if i in VOC2012_val_list:
            remove_list.append(i)

    for i in remove_list:
        VOC2012AUG_train_list.remove(i)

    txt_path = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/train_aug.txt"
    list2txt(VOC2012AUG_train_list, txt_path)

    VOC2012AUG_val_list = VOC2012_val_list
    txt_path = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/val_aug.txt"
    list2txt(VOC2012AUG_val_list, txt_path)

    VOC2012AUG_trainval_list = VOC2012AUG_train_list + VOC2012AUG_val_list
    txt_path = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/trainval_aug.txt"
    list2txt(VOC2012AUG_trainval_list, txt_path)


def list2txt(list, txt_path):
    if os.path.exists(txt_path):
        os.remove(txt_path)
    with open(txt_path, 'a') as f:
        for i in list:
            f.write(i)
            f.write('\n')
    print('Save txt file: {} with {} terms'.format(txt_path, len(list)))


def generate_VOC2012AUG_label_folder():
    VOC2012AUG_trainval_txt_file = "data/VOC/VOC2012/TrainVal/ImageSets/Segmentation/trainval_aug.txt"

    VOC2012AUG_trainval_list = []
    for idx in open(VOC2012AUG_trainval_txt_file):
        idx = idx.strip()
        name = idx + '.png'
        VOC2012AUG_trainval_list.append(name)

    org_label_dir_SBD = "data/VOC/SBD/benchmark_RELEASE/dataset/cls_png"
    org_label_dir_2012 = "data/VOC/VOC2012/TrainVal/SegmentationClass"

    org_label_SBD_list = os.listdir(org_label_dir_SBD)
    org_label_2012_list = os.listdir(org_label_dir_2012)

    VOC2012AUG_label_dir = 'data/VOC/VOC2012/TrainVal/SegmentationClassAUG'
    os.makedirs(VOC2012AUG_label_dir, exist_ok=True)

    for i in VOC2012AUG_trainval_list:
        if i in org_label_2012_list:
            src = os.path.join(org_label_dir_2012, i)
            dst = os.path.join(VOC2012AUG_label_dir, i)
            copyfile(src, dst)
        elif i in org_label_SBD_list:
            src = os.path.join(org_label_dir_SBD, i)
            dst = os.path.join(VOC2012AUG_label_dir, i)
            copyfile(src, dst)
        else:
            print('Error: label file of {} is not contained in either VOC2012 or SBD label folder!')
            raise ValueError
    print('Finished!')

    # check again
    print('\nCheck Again...')
    l = os.listdir(VOC2012AUG_label_dir)

    assert len(l) == len(VOC2012AUG_trainval_list)
    for i in VOC2012AUG_trainval_list:
        assert i in l

    print('\nCheck Finished! All is Right!')




if __name__ == '__main__':
    fire.Fire()


# python3 voc.py SBD_label_mat2png
# python3 voc.py generate_VOC2011_VOC2012_subval_txt
# python3 voc.py generate_VOC2012AUG_txt
# python3 voc.py generate_VOC2012AUG_label_folder

# python3 voc.py check_VOC2011_contain_SBD_or_not
# python3 voc.py check_img_of_11_12_same_or_not
# python3 voc.py check_SBD_VOC2012_repeat

# python3 voc.py check_SBD_clspng
# python3 voc.py assert_VOC2012AUG_same