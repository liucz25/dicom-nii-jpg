import glob
import os




def get_file(filepath):
#获取指定文件夹下dcm文件个数为19-40个的所有dcm文件名称
    s = os.sep
    file = "*.dcm"
    filename=[]
    for rt,dirs,files in os.walk(filepath):
        for d in dirs:
            # print(rt+s+d+s+file)
            l=len(glob.glob(rt+s+d+s+file))
            if l>19 and l<40:
                filename+=glob.glob(rt+s+d+s+file)

    return filename

if __name__=="__main__":
    filepath = r"/pic-zhunbei/tu"
    filepathfile = "D:\code\deeplearn\pic-zhunbei\tu\2019.01.17\00149257.00469478\1.2.840.113704.1.111.4572.1547672348.9"
    file = "*.dcm"
    # 获取文件
    # print(glob.glob(filepathfile + file), "\n")
    # 获取文件个数
    # print(len(glob.glob(filepathfile + file)))
    # 列出文件及目录
    # print(os.listdir(filepath))

    fliename=get_file(filepath)
    print(len(fliename))