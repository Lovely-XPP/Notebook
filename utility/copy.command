#!/bin/bash
Root=$(cd $(dirname ${BASH_SOURCE:-$0});pwd)
cd $Root
Root=$(cd '..';pwd)
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
		  	"Attitude Dynamics and Control of Spacecraft"
		  	"Advanced Mathematics"
		  	"Analytical Geometry"
		  	"Probability Statistics"
		  	"College Physics"
			"Slam"
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
		  	"高等数学"
		  	"空间解析几何"
		  	"概率论与数理统计"
		  	"大学物理上册"
			"视觉Slam笔记"
		  )
for (( i = 0; i < ${#notebook[@]}; i++ )); do
	source_file="${Root}/source/${notebook[i]}/${notebook[i]}.pdf"
	target_file="${Root}/笔记pdf/${notebkcn[i]}.pdf"
	cp -f "${source_file}" "${target_file}"
done