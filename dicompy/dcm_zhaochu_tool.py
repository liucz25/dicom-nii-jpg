import glob
import os
from pydicom import dcmread
from pydicom import dcmwrite


def get_file(file_path):
    # 获取指定文件夹下dcm文件个数为19-40个的所有dcm文件名称
    s = os.sep
    file = "*.dcm"
    filename = []
    for rt, dirs, files in os.walk(file_path):
        for d in dirs:
            # print(rt+s+d+s+file)
            l = len(glob.glob(rt + s + d + s + file))
            if l > 19 and l < 40:
                filename += glob.glob(rt + s + d + s + file)
    return filename


def copy_to(from_file, to):
    s = os.sep
    g = "-"
    ds = dcmread(from_file)
    date = str(ds.StudyDate)
    # print(ds.PatientName)
    pid = str(ds.PatientID)
    an = str(ds.AccessionNumber)
    xh = str(ds.InstanceNumber)
    out = to + s + date + g + pid + g + an + g + xh + ".dcm"
    # print(out)
    dcmwrite(out, ds)


def antoseries(filename):
    ds = dcmread(filename)
    ds.SeriesNumber = ds.AccessionNumber
    ds.save_as(filename)

def copy_to2(from_file, to):
    s = os.sep
    g = "-"
    ds = dcmread(from_file)
    date = str(ds.StudyDate)
    # print(ds.PatientName)
    pid = str(ds.PatientID)
    an = str(ds.AccessionNumber)
    xh = str(ds.InstanceNumber)
    outFold = to + s + date + g + pid + g + an
    mkdir(outFold)
    out = to + s + date + g + pid + g + an + s + xh + ".dcm"
    print(out)
    dcmwrite(out, ds)


def mkdir(path):
    isExist=os.path.exists(path)
    if not isExist:
        os.makedirs(path)