import os
import SimpleITK as sitk
dcm_directory=r"D:\code\deeplearn\pic\2019.09.27\00048931.00559175\2"
series_ids=sitk.ImageSeriesReader.GetGDCMSeriesIDs(dcm_directory)
series_file_names=sitk.ImageSeriesReader.GetGDCMSeriesFileNames(dcm_directory,series_ids[0])
series_reader=sitk.ImageSeriesReader()
series_reader.SetFileNames(series_file_names)
image3d=series_reader.Execute()
size=image3d.GetSize()
print(size)
image_array = sitk.GetArrayFromImage(image3d)
print(image_array.shape)
print(image_array[4,:,:])
# print(image_array)
folder_name=r"D:\code\deeplearn\pic\2019.09.27\00048931.00559175\3"
new_name = "new_MR_2.dcm"
print(os.path.join(folder_name,new_name))
origin = image3d.GetOrigin()
spacing = image3d.GetSpacing()
print(origin)
im=image_array[4,:,:]

    sitk.WriteImage(im,os.path.join(folder_name,new_name))
# file_writer = sitk.ImageFileWriter()
# file_writer.SetFileName(os.path.join(folder_name,new_name))
# file_writer.SetImageIO(imageio="GDCMImageIO")
# # file_writer.SetImageIO(image_array)
# file_writer.Execute(image_array)