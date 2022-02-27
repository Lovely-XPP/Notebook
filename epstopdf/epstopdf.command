#!/bin/bash
cd $(dirname "${BASH_SOURCE[0]}")
num=0
pdf_files=(0)
for file in $(dirname "${BASH_SOURCE[0]}")/*.eps; do
	file_name=$(basename ${file})
	file_prefix=${file_name%.*}
	epstopdf --hires --outfile="${file_prefix}.pdf" ${file_name}
	if [ $? -eq 0 ]; then
			mv "${file_prefix}.eps" backup/
			echo "${file_prefix}.eps转换成功！"
			pdf_files[num]="${file_prefix}.pdf"
			num=`expr ${num} + 1`
	fi
done

if [[ "${pdf_files[0]}" == "0" ]]; then
	echo ""
	echo "转换文件失败或没有需要转换的文件！"
	echo ""
	echo "请按Enter键推出..."
	read quit
	exit
fi

while [[ 1 ]]; do
	echo ""
	echo "转换成功，是否选择复制到相应笔记本路径的pic/文件夹下："
	echo ""
	echo -n "是(1) / 否 (0): "
	read choose
	if [[ "${choose}" == "1" || "${choose}" == "0" ]]; then
		break
	else
		echo ""
		echo "请输入 0 或 1 ！"
		echo ""
		sleep 1
		clear
	fi
done
if [[ "${choose}" == "1" ]]; then
	notebook=(	
			"Engineering Thermodynamics and Heat Transfer"
			"Essential Mathematical Methods for Physicists"
		  	"Matlab"
		  	"Principle of Automatic Control"
		  	"Missle Flight Dynamics"
		  	"Orbital Mechanics"
		  	"Rocket Propulsion Theory"
		  	"Aircraft structural mechanics"
		  	"Aerodynamics"
		  	"Orbital Mechanics"
		  	"高等数学"
		  	"航天器姿态动力学与控制"
		  )
	j=0

	while [[ 1 ]]; do
		clear

		echo "现存所有的笔记本和对应序号如下："
		echo ""

		for (( i = 0; i < ${#notebook[@]}; i++ )); do
			number=`expr ${i} + 1`
			echo "${number}: ${notebook[i]}"
		done
		echo ""

		k=`expr	${j} + 1`
		echo -n "[第 ${k} 个 / 共 ${num} 个]  ${pdf_files[j]}"
		echo -e "\n"
		echo -n "请输入要存入笔记本的序号："
		read notebook_No

		if (( notebook_No < 0 || notebook_No > ${#notebook[@]} )); 
		then
			clear
			echo ""
			echo "不存在相应的序号的笔记本，请重试！"
			echo ""
			sleep 2
			continue
		
		else
			index=`expr ${notebook_No} - 1`
			source_file="./${pdf_files[${j}]}"
			target_file="../source/${notebook[index]}/pic/${pdf_files[${j}]}"
			pic_dir="../source/${notebook[index]}/pic/"
			if [ ! -d "${pic_dir}" ];
			then
				mkdir "${pic_dir}"
			fi
			mv -f "${source_file}" "${target_file}"
			j=`expr ${j} + 1`
		fi

		if (( j >= num ));
		then
			break;
		fi
	done
fi
clear
echo -e "\n 文件转换已完成！\n"
echo "请按Enter键推出..."
read quit
exit