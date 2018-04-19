#! /bin/sh
# This file is for pushing graded assignments to GitHub Classroom repositories
# It will add all new files and commit them with a given message
# It requires the folder name and a message
# sample use  ./push_all.sh spring-2018-assignment-2

if [[ $# -ne 1 ]];
	then
	echo "This script requires 1 parameter."
	echo "1. The folder name the assignments are in"
else
	assignment=$1
	date=`date +%m-%d-%Y`
	time=`date +%H:%M:%S`
	for f in ../${assignment}/*
		do
			cd $f
			git add mortgage.py
			git commit -m "Grader Comments Q1 ${date} ${time}"
			git push -f origin master
			echo $f
			cd ..
		done
fi
