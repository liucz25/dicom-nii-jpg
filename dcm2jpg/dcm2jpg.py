from pydicom import dcmread
import matplotlib.pyplot as plt
import numpy as np
import os
import imageio

import dcmtool


def dcm2jpg(fd, outdir):
    filelist = os.listdir(fd)
    for file in filelist:
        ds = dcmread(os.path.join(fd, file))
        arr = dcmtool.get_pixeldata(ds)
        out = dcmtool.setWwWc(arr, 80, 40)
        imageio.imsave(os.path.join(outdir, str(file) + '.jpg'), out)


if __name__ == "__main__":
    fd = r"D:\code\deeplearn\src\tu\iDose (1)1"
    # fn = "Image060.dcm"
    outdir = r"D:\code\deeplearn\src\tu\iDose (1)1\s"
    dcm2jpg(fd, outdir)
