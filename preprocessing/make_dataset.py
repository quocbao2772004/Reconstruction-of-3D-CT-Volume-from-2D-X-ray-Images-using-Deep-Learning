import os, shutil

path = r'F:\project\AI-Medical-Image-Processing\Reconstruction-of-3D-CT-Volume-from-2D-X-ray-Images-using-Deep-Learning\resized_folder'
# print(len(os.listdir(path)))
dts = r'D:\dataset'
train = r'D:\dataset\train'
val = r'D:\dataset\val'
app = r'D:\dataset\app'
# os.mkdir(dts)
os.mkdir(val)
os.mkdir(train)
os.mkdir(app)
index = 0
for i in os.listdir(path):
    folder = os.path.join(path, i)
    index+=1
    if index <= 13:
        subfolder = os.path.join(train, i)    
    elif index <= 17:
        subfolder = os.path.join(val, i)   
    else:
        subfolder = os.path.join(app, i)   
    os.mkdir(subfolder)
    shutil.copytree(folder, subfolder, dirs_exist_ok = True)