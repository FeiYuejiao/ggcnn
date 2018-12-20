# Visualize point cloud depth image with meshlab
### pcd2txt
Read raw data from cornell dataset and ongly extract x y z, as well as adding a 'v'at the start of each line, so that meshlab can read it. Output converted_pcd****.txt file.
### txt2obj
Create a obj folder to contain .obj files that meshlab can read. Attention, obj folder cannot be existed before, otherwise shutil.copytree can cause an error.


