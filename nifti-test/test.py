import matplotlib

from matplotlib import pylab as plt 
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D

fn="chuxue.nii.gz"
# fn="120-ok.nii.gz"
img=nib.load(fn)
# print(img)
OrthoSlicer3D(img.dataobj).show()
# print(img.dataobj[::1])
# plt.imshow(img.dataobj[::1])
# plt.show()