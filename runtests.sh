#!/bin/bash

args=("$@")
num_args=${#args[@]}
index=0

suite='shop payments'

coverage=false
documentation=false

while [ "$index" -lt "$num_args" ]
do
	case "${args[$index]}" in
		"--with-docs")
			documentation=true
			;;
		"--with-coverage")
			coverage=true
			;;
		*)
			suite="shop.${args[$index]}"
	esac
let "index = $index + 1"
done

if [ $coverage == true ]; then
	pushd .
	cd magna 
	coverage run manage.py test $suite
	coverage html
	x-www-browser htmlcov/index.html
	popd

else

	# the default case...
	pushd .
	cd magna
	python manage.py test $suite
	popd

fi

if [ $documentation == true ]; then
	pushd .
	cd docs/
	make html
	x-www-browser _build/html/index.html
	popd
fi
