import os
import zipfile

def Compress():
    #-------------压缩文件----------
    #压缩文件
    lu_jing = "D:\\Tage_work\\diaodupingtai\\test_report\\data\\"  #获取文件夹路径
    lu_jing_2 = str(os.listdir(lu_jing)) #获取文件下的所有文件名称
    lu_jing_3 = lu_jing_2 +".zip" #文件名称夹后缀压缩名称
    lu_jing_3 = lu_jing_3.replace("[",'')
    lu_jing_3 = lu_jing_3.replace("]",'')
    lu_jing_3 = lu_jing_3.replace("'",'')
    z = zipfile.ZipFile(lu_jing_3, "w", zipfile.ZIP_DEFLATED)
    for dir_path,dir_name,file_name in os.walk(lu_jing):
        f_path = dir_path.replace(lu_jing ,"")
        f_path = f_path and f_path+os.sep or ""
        for file_name in file_name:
            z.write(os.path.join(dir_path,file_name),f_path+file_name)
        z.close()