import os
import hashlib
# 思路：获取所有的文件，并且比较他们的md5，若是md5相同，则认为是相同文件，然后输出
# 返回自定义文件夹下的文件
def getAllList(root_path,allfile):
    file_path_list = os.listdir(root_path)
    for file_path_name in file_path_list:
        file_path = os.path.join(root_path,file_path_name)
        if os.path.isdir(file_path): #如果还有文件夹将深入获取
            getAllList(file_path,allfile)
        else :
            allfile.append(file_path)
    return allfile

# 读取文件中的所有内容
# keep保留几个，默认保留一个
def findMd5(files,keep=1):
    md5list = {}
    for filepath in files:
        # 如果是文件夹则跳过
        if os.path.isdir(filepath):
            continue
        md5obj = hashlib.md5()
        fd = open(filepath, 'rb')
        while True:
            buff = fd.read(2048)
            if not buff:
                break
            md5obj.update(buff)
        fd.close()
        # 获取哈希md5
        filemd5 = str(md5obj.hexdigest()).lower()
        if filemd5 in md5list:
            md5list[filemd5].add(filepath)
        else:
            md5list[filemd5] = set([filepath])
    for key in md5list:
        list = md5list[key]
        if len(list) > 1:
            for i,v in enumerate(list):
                print ('删除第{}个具有相同的md5的文件'.format(i))
                if i> keep-1:
                  os.remove(v)
                else:
                  continue

if __name__ == "__main__":
    result = getAllList('./avatar',[])
    findMd5(result)
