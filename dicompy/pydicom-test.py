from pydicom import dcmread
from pydicom import dcmwrite

import os

def copyto(from_file,to):
    s=os.sep
    g="-"
    ds=dcmread(from_file)
    date=str(ds.StudyDate)
    # print(ds.PatientName)
    pid=str(ds.PatientID)
    an=str(ds.AccessionNumber)
    xh=str(ds.InstanceNumber)
    out=to+s+date+g+pid+g+an+g+xh+".dcm"
    # print(out)
    dcmwrite(out,ds)
def dcmtojpg(from_file,to_dir):
    ds=dcmread(from_file)
    arr=ds.pixel_array()




if __name__=="__main__":
    filepath = r"/pic-zhunbei/tu/2019.01.17/00149257.00469478/1.2.840.113704.1.111.4572.1547672348.9"
    filename = "\\1.2.840.113704.1.111.2324.1547672379.31281.dcm"
    fi = "\\1.2.840.113704.1.111.2324.1547672385.31288.dcm"
    from_file=filepath+filename
    to = r"D:\code\deeplearn\pic-zhunbei\dcm"

    # copyto(from_file,to)