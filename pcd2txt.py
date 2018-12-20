#coding=utf-8
import os
import numpy as np
import glob
import shutil

# pcd v7 to .txt only include x y z info, starting with a 'v' so that meshlab can read

RAW_DATA_DIR = 'data/cornell' 
OUTPUT_DIR = 'data/txt' #生成.txt文件到这
# File name patterns 

_pcd_pattern = os.path.join(RAW_DATA_DIR, 'pcd%sr.png')


def get_image_ids():
    # Get all the input files, extract the numbers.
    pcd_images = glob.glob(_pcd_pattern % "*")
    pcd_images.sort()
    print(pcd_images)
    return [p[-9:-5] for p in pcd_images]


# Create the output directory
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


fields = [
    'img_id'
]

for img_id in get_image_ids():
    print('Processing: %s' % img_id)    
    try:    
        with open(RAW_DATA_DIR+"/pcd"+img_id+".txt") as f:
            for l in f.readlines():
                ls = l.split()

                if len(ls) != 5:
                    # Not a point line in the file.
                    continue
                try:
                    # Not a number, carry on.
                    float(ls[0])
                except ValueError:
                    continue
                x = str(ls[0])
                y = str(ls[1])
                z = str(ls[2])
                with open(OUTPUT_DIR+"/converted_pcd"+img_id+".txt",'a') as file_handle:
                    file_handle.write("v"+" "+x+" "+y+" "+z+"\n")
                    file_handle.close()

    except:
        continue

    







       


