import os, shutil

def remove_trash_file(path):
    # path = r"D:\LIDC-IDRI"

    for i in os.listdir(path):
        new_path = os.path.join(path,i)
        for j in os.listdir(new_path):
            dicom_size = os.path.getsize(os.path.join(new_path,j))
            if dicom_size < 500000:
                os.remove(os.path.join(new_path,j))

def check_number_of_dicom_files(path):
    count=0
    for i in os.listdir(path):
        subfolder = os.path.join(path,i)
        if len(os.listdir(subfolder)) <=300:
            count += 1
            print(i) 
    print(count)

def take_n_dicom_files(n, path):
    exp_path = r'D:\LIDC-IDRI-256_256_256'
    
    for i in os.listdir(path):
        subfolder = os.path.join(path,i)
        new_folder = os.path.join(exp_path, i)
        os.mkdir(new_folder)
        count=0
        for j in os.listdir(subfolder):
            count+=1
            if count == 257:
                break
            shutil.copy(os.path.join(subfolder,j), new_folder)
def main():
    path = r'D:\LIDC-IDRI-suitable'
    take_n_dicom_files(256, path)

if __name__ == '__main__':
    main()