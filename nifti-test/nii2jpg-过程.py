import matplotlib
from matplotlib import pylab as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D
import os
# from scipy import misc
import imageio
import numpy as np

def uint16to8(bands, lower_percent=0.001, higher_percent=99.999):
    out = np.zeros_like(bands,dtype = np.uint8)
    n = bands.shape[0]
    for i in range(n):
        a = 0 # np.min(band)
        b = 255 # np.max(band)
        c = np.percentile(bands[i, :], lower_percent)
        d = np.percentile(bands[i, :], higher_percent)
        t = a + (bands[i, :] - c) * (b - a) / (d - c)
        t[t<a] = a
        t[t>b] = b
        out[i, :] = t
    return out
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

        # # img_i = img_arr.rotate(90)
        # plt.axis('off')
        # fig = plt.gcf()
        # plt.gca().xaxis.set_major_locator(plt.NullLocator())
        # plt.gca().yaxis.set_major_locator(plt.NullLocator())
        # plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        #
        # plt.margins(0, 0)
        # plt.imshow(img_arr.T, cmap='gray')
        #
        # plt.savefig(os.path.join(outdir, outfilename + str(num) + '.jpg'))
        img8=uint16to8(img_arr.T)
        imageio.imsave(os.path.join(outdir, outfilename + str(num) + '.jpg'),img8)

        num += 1
    # plt.show()


if __name__ == '__main__':
    fn = "120-huan.nii.gz"
    nii2jpg(filename=fn, step=30, out_dir="120-all", out_filename="120-all-T")
