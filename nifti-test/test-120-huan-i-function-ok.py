import matplotlib

from matplotlib import pylab as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D
import os


def nii2jpg(filename, out_dir, out_filename, step=1):
    fn = filename
    step = step
    outdir = out_dir
    outfilename = out_filename
    img = nib.load(fn)
    # print(img)
    width, height, queue = img.dataobj.shape
    num = 1
    for i in range(0, queue, step):
        img_arr = img.dataobj[:, :, i]

        # img_i = img_arr.rotate(90)
        plt.imshow(img_arr, cmap='gray')

        plt.savefig(os.path.join(outdir, outfilename + str(num) + '.jpg'))
        num += 1
    # plt.show()


if __name__ == '__main__':
    fn = "120-huan.nii.gz"
    nii2jpg(filename=fn, step=30, out_dir="120-all", out_filename="120-all")
