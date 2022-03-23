'''
此脚本用于删除某些特殊部分的首页页码，其原理为
自动写入 \thispagestyle{empty} 到特殊的tex文件。
目前支持的文件有：
1. 索引文件 .ind
2. 符号说明文件 .nls
3. 表格引用文件 .lot
4. 图片引用文件 .lof
5. 目录文件     .toc
6. 参考文件文件 .bbl
'''

import os
import shutil


# 判断是否为需要处理的文件
# 是：返回 True  
# 否：返回 False
def IsTargetFile(filename):
    Target_Files = ['.ind', '.nls', '.lot', '.lof', '.toc', '.bbl']
    for target in Target_Files:
        if os.path.splitext(filename)[1] == target:
            return True
    return False


# 判断文件类型：是否存在环境（即\begin{XXX}）
# 是：若不存在返回\begin{XXX}所在行号 + 1
# 否：返回 0
def IsEnv(file):
    with open(file,"r") as f:
        lines = f.readlines()
        hit = 0
        judge = 0

        # 判断每一行是否存在begin，从前往后，存在即读取行号并停止
        for index, line in enumerate(lines):
            # 删除每行开头的空格或tab
            line.lstrip()
            line.lstrip('\t')
            # 如果遇到空行或注释，则跳过
            if line[0] == '\n' or line[0] == '%':
                continue
            # 如果遇到\begin，则说明为环境，否则不是
            # 注意：由于 '\' 是需要转义的字符，所以 '\' 算两个字符
            if judge == 0 and line[0:6] == "\\begin":
                hit = index + 1
            else:
                if judge == 0:
                    hit = 0
            # 判断是否已经存在 \thispagestyle，若存在则输出 -1
            if line[0:14] == "\\thispagestyle":
                hit = -1
                judge = 1
            if judge == 1:
                return hit
            judge = 1


# 写入文件
def WriteFile(file, hit):
    origin_filename = os.path.splitext(file)[0]
    origin_extend = os.path.splitext(file)[1]
    new_filename = origin_filename + 'new'
    new_extend = origin_extend
    newfile = new_filename + new_extend
    with open(file,'r') as origin, open(newfile,"w") as new:
        for index, line in enumerate(origin):
            if index == hit:
                text = '\\thispagestyle{empty}\n'
                text = ''.join((text,line))
                new.write(text)
            else:
                new.write(line)
    shutil.move(newfile, file)
    #print('已经成功写入文件' + origin_filename + origin_extend + '!')


# 主函数
if __name__=="__main__":
    root = os.path.abspath(os.path.join(os.getcwd(), "..")) 
    source = os.path.join(root, 'source')
    folders = []
    for list in os.listdir(source):
        dir = os.path.join(source, list)
        if os.path.isdir(dir):
            folders.append(dir)
    for folder in folders:
        for list in os.listdir(folder):
            file = os.path.join(folder, list)
            if os.path.isdir(file):
                continue
            if IsTargetFile(file):
                hit = IsEnv(file)
                if hit == -1:
                    continue
                WriteFile(file, hit)
