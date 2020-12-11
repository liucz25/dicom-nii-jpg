from pydicom import dcmread
from pydicom import dcmwrite

import os
from pydicom.valuerep import MultiString
import pydicom.valuerep
from pydicom.charset import default_encoding

def antoseries(filename):
    ds=dcmread(filename)
    # 测试用，各种不能保存，即使转换格式
    # # print(type(ds.SeriesNumber))
    # print(type(ds.AccessionNumber))
    # an=ds.AccessionNumber
    # # byte=an.encode()
    # # # an=an.encode(default_encoding)
    # # # print(type(byte))
    # #
    # # byte=byte.decode(default_encoding)
    # # # print(type(byte2))
    # # IS=MultiString(byte, valtype=pydicom.valuerep.IS)
    # # print(type(IS))
    # # ds.SeriesNumber=IS
    # # print(ds.SeriesNumber)
    # # print(ds.AccessionNumber)
    # print(type(ds.StationName))
    ds.SeriesNumber=ds.AccessionNumber

    # 原因未知，dcmwrite保存报错
    # dcmwrite(ds,"filename.dcm")
    ds.save_as(filename)

if __name__=="__main__":
    filepath = r"/pic-zhunbei"
    filename = "\\5.dcm"
    from_file=filepath+filename
    antoseries(from_file)
