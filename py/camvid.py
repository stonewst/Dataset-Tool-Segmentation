import os
import fire


def gen_camvid_txt():
    camvid_train_list = []
    camvid_val_list = []
    camvid_test_list = []

    camvid_train_img_folder = "data/CamVid/train"
    camvid_val_img_folder = "data/CamVid/val"
    camvid_test_img_folder = "data/CamVid/test"

    camvid_train_img_list = os.listdir(camvid_train_img_folder)
    camvid_val_img_list = os.listdir(camvid_val_img_folder)
    camvid_test_img_list = os.listdir(camvid_test_img_folder)

    for i in camvid_train_img_list:
        (former_name, extension) = os.path.splitext(i)
        camvid_train_list.append(former_name)
    txt_path = "data/CamVid/train.txt"
    list2txt(camvid_train_list, txt_path)

    for i in camvid_val_img_list:
        (former_name, extension) = os.path.splitext(i)
        camvid_val_list.append(former_name)
    txt_path = "data/CamVid/val.txt"
    list2txt(camvid_val_list, txt_path)

    for i in camvid_test_img_list:
        (former_name, extension) = os.path.splitext(i)
        camvid_test_list.append(former_name)
    txt_path = "data/CamVid/test.txt"
    list2txt(camvid_test_list, txt_path)


def list2txt(list, txt_path):
    if os.path.exists(txt_path):
        os.remove(txt_path)
    with open(txt_path, 'a') as f:
        for i in list:
            f.write(i)
            f.write('\n')
    print('Save txt file: {} with {} terms'.format(txt_path, len(list)))



if __name__ == '__main__':
    fire.Fire()

# python3 camvid.py gen_camvid_txt