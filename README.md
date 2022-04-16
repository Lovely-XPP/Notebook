# 中山大学航空航天课程笔记
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## 文件目录说明

├── LICENSE ── 开源许可证

├── README.md ── 本说明文档

├── copy.command ── 复制笔记文件的命令

├── utility —— 笔记的实用工具

├── source ── 笔记的`tex`源文件

└── 笔记pdf ── 已经生成好的笔记文件，可以直接查看和下载

## 目前正在更新的笔记

* 航天器姿态动力学与控制

## 已完成的笔记

* 大学物理上册
* 空间解析几何
* 数学物理方法（Essential Mathematical Methods for Physicists）(尤其感谢我的授课老师和指导老师胡战超老师的指导和勘误)
* 高等数学

## 暂时停更的笔记

* Matlab与科学计算（Matlab）
* 概率论与数理统计
* 自动控制原理（Principle of Automatic Control）
* 工程热力学和传热学（Engineering Thermodynamics and Heat Transfer）



## 编译原始文件的说明

**编写语言：`Tex`**

(1) 首先，如果没有下载`Texlive`（`Windows`/`Linux` ）或`MacTex`（`MacOS`），建议前往清华镜像源下载：https://mirrors.tuna.tsinghua.edu.cn。

(2) 如果已经安装好`Texlive`或`MacTex`，请下载或克隆源码。

(3) 下载完成后，由于文档的字体是基于`MacOS`的内置字体，对于`Windows`和`Linux`系统的用户，还需将每个笔记源文件主目录中的`main.tex`文件中的以下代码（在导入宏包后的首个设置，一般在60行前）

```tex
%字体设置
\setCJKmainfont[BoldFont={PingFangSC-Medium}]{PingFangSC-Regular}
```

注释或改为其对应系统的可用字体，这里以注释为例，只需要在代码前添加一个`%`即可：

```tex
%字体设置
%\setCJKmainfont[BoldFont={PingFangSC-Medium}]{PingFangSC-Regular}
```

(4) 编译方式请选择为`XeLaTeX`. 

## 联系方式

基于相应的课本和自己的心得编写，如有错误，请联系：

![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)   

* sunray617550202@gmail.com

 ![微信](https://aleen42.github.io/badges/src/wechat.svg)  
 * Ray617550202

谢谢大家的支持～
希望对大家有一点点的帮助～～
祝大家学业进步
