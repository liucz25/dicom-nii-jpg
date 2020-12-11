from dcm_zhaochu_tool import get_file
from dcm_zhaochu_tool import copy_to2
from dcm_zhaochu_tool import antoseries
import os
root=r"D:\code\deeplearn\pic-zhunbei\tu"
out=r"D:\code\deeplearn\pic-zhunbei\dcmfold"
out2=r"D:\code\deeplearn\pic-zhunbei\dcman"
root2=r"D:\code\deeplearn\pic-zhunbei\dcm"

# # 分文件夹代码
# fs=get_file(root2)
# for f in fs:
#     copy_to2(f,out2)


# 序列号变成an号代码
# s=os.sep
# for rt,dirs,files in os.walk(root2):
#     for file in files:
#         antoseries(rt+s+file)

# 分文件夹程序
s=os.sep
for rt,dirs,files in os.walk(root2):
    for file in files:
        copy_to2(rt+s+file,out2)