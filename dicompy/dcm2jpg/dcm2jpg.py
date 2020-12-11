import os

import dcmtool
import imageio
from pydicom import dcmread


# 把dcm图像按照特定的窗宽窗位，转换成jpg图像

def dcm2jpg(dcmdir, jpgdir):
    DcmToJpg(dcmdir, jpgdir,160,80)


def DcmToJpg(dcmdir, jpgdir, ww, wc):
    filelist = os.listdir(dcmdir)
    for file in filelist:
        ds = dcmread(os.path.join(dcmdir, file))
        arr = dcmtool.get_pixeldata(ds)
        out = dcmtool.setWwWc(arr, ww, wc)
        imageio.imsave(os.path.join(jpgdir, str(file) + '.jpg'), out)


if __name__ == "__main__":
    # dcmdir = r"D:\code\deeplearn\pic-zhunbei\dcm-select-all"
    dcmdir = r"D:\code\deeplearn\pic-zhunbei\dcm-select-part"
    # fn = "Image060.dcm"
    # jpgdir = r"D:\code\deeplearn\pic-zhunbei\jpg-select-all-dcm-160-80"
    jpgdir = r"D:\code\deeplearn\pic-zhunbei\jpg-select-part-dcm-160-80"
    dcm2jpg(dcmdir, jpgdir)
