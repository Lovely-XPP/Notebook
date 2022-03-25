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
# 版本号
global ver 
ver = "0.3"

import os
import shutil
import argparse
from termcolor import colored


# 添加信息输出样式
def Log(status, log):
    if status == "INFO":
        prefix = colored("[INFO]", "green")
    elif status == "ERROR":
        prefix = colored("[ERROR]", "red", attrs=["blink", "bold"])
    elif status == "WARNING":
        prefix = colored("[WARNING]", "yellow", attrs=["blink"])
    output = prefix + ' ' + log
    print(output)


# 判断是否为需要处理的文件
# 是：返回 True  
# 否：返回 False
def IsTargetFile(file):
    Target_Files = ['.ind', '.nls', '.lot', '.lof', '.toc', '.bbl']
    for target in Target_Files:
        if os.path.splitext(file)[1] == target:
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


# 输入文件绝对路径，写入文件
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
    output = "已经成功写入文件:" + " " + os.path.basename(file) + "!"
    Log("INFO", output)


# 输入tex文件夹绝对路径，完成整个过程（封装）
def RemoveFirstPageNo(folder):
    hit = 0
    handle = 0
    for file_list in os.listdir(folder):
        file = os.path.join(folder, file_list)
        if os.path.isdir(file):
            continue
        if IsTargetFile(file):
            hit = IsEnv(file)
        else:
            continue
        handle = 1
        if hit == -1:
            Log("WARNING", "文件已经处理过，无需再次处理:" + file_list)
            continue
        WriteFile(file, hit)
    if handle == 0:
        Log("WARNING", "该文件夹没有包含需要处理的文件！")


# 添加命令行参数
def GetArgs():
    root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    source = os.path.join(root, 'source')
    descrip = '此脚本用于删除某些特殊部分的首页页码，其原理为自动写入 \\thispagestyle{empty} 到特殊的tex文件。\n目前支持的文件有：\n    1. 索引文件  \t.ind \n    2. 符号说明文件\t.nls\n    3. 表格引用文件\t.lot \n    4. 图片引用文件\t.lof \n    5. 目录文件  \t.toc \n    6. 参考文件文件\t.bbl'
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description=descrip)
    parser.add_argument('--version', action='version',
                        version='RemoveFirstPageNo ' + ver)
    parser.add_argument('--folders', metavar="DIR",  nargs='?',
                    help='输入包含多个tex工程（子文件夹）的文件夹，用于批处理',
                    default=source)
    parser.add_argument('--folder', metavar="DIR", nargs='?',
                        help='输入单个tex工程文件夹，当 --folders 有参数时，此选项无效')
    return parser


# 主函数
if __name__ == "__main__":
    args = GetArgs().parse_args()
    folders = []
    fd = 0
    source = args.folders
    if os.path.isdir(source):
        fd = 1
        for folder_list in os.listdir(source):
            dir = os.path.join(source, folder_list)
            if os.path.isdir(dir):
                folders.append(dir)
    else:
        folders.append(args.folder)

    if folders == [None]:
        Log("ERROR", "没有需要处理的文件！\n")
        exit()
    if fd == 1:
        Log("INFO", "选择的模式：多文件夹批处理")
        Log("INFO", "输入的文件夹:" + args.folders)
    else:
        Log("INFO", "选择的模式：单文件夹处理")
        Log("INFO", "输入的文件夹:" + args.folder)
    if not os.path.isdir(folders[0]):
        Log("ERROR", "文件夹路径输入错误！\n")
        exit()
    
    Log("INFO", "开始处理文件")
    for folder in folders:
        Log("INFO", "正在进行文件夹处理:" + " " +folder)
        RemoveFirstPageNo(folder)
