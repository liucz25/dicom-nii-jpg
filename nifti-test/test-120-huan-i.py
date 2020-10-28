import matplotlib

from matplotlib import pylab as plt 
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D
import os

# fn="chuxue.nii.gz"
# 做了一个颅骨的感兴趣区模板，看看效果
# print(os.getcwd())
# fn=os.path.join(os.getcwd(),'120-huan.nii.gz')
fn="120-huan.nii.gz"
img=nib.load(fn)
print(img)
# OrthoSlicer3D(img.dataobj[::20]).show()
# print(img.header['db-name'])
width,height,queue=img.dataobj.shape


num =1
for i in range(0,queue,1):
    img_arr=img.dataobj[:,:,i]
    # plt.subplot(12,10,num)
    # print(os.path.join(r'./',str(num)+'.jpg'))
    plt.imshow(img_arr,cmap='gray')
    plt.savefig(os.path.join('.\\120-all\\120-huan-i-'+str(num)+'.jpg'))
    num+=1

# print(img.dataobj[::1])
# plt.imshow(img.dataobj[::1])
# plt.show()