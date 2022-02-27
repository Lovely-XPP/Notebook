#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")
notebook=(	
			"Engineering Thermodynamics and Heat Transfer"
			"Essential Mathematical Methods for Physicists"
		  	"Matlab"
		  	"Principle of Automatic Control"
		  	"Missle Flight Dynamics"
		  	"Rocket Propulsion Theory"
		  	"Aircraft structural mechanics"
		  	"Aerodynamics"
		  	"Orbital Mechanics"
		  	"航天器姿态动力学与控制"
		  )

notebkcn=(	
			"工程热力学和传热学" 
			"数学物理方法"
		  	"Matlab"
		  	"自动控制原理"
		  	"导弹飞行力学"
		  	"火箭推进理论"
		  	"飞行器结构力学"
		  	"空气动力学"
		  	"轨道力学"
		  	"航天器姿态动力学与控制"
		  )
for (( i = 0; i < ${#notebook[@]}; i++ )); do
	source_file="./source/${notebook[i]}/${notebook[i]}.pdf"
	target_file="./笔记pdf/${notebkcn[i]}.pdf"
	cp -f "${source_file}" "${target_file}"
done
cp -f ./source/大学物理上册/DXWL.pdf ./笔记pdf/大学物理上册.pdf
cp -f ./source/概率论与数理统计/概率统计.pdf ./笔记pdf/概率论与数理统计.pdf
cp -f ./source/高等数学/高等数学.pdf ./笔记pdf/高等数学.pdf
cp -f ./source/空间解析几何/JXJH.pdf ./笔记pdf/空间解析几何.pdf