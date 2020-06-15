#! /usr/bin/sh
for file in `find /home/ec2-user/gitrepo/BasicPython/scripts -iname "*.py"`
do
	linenumber=$(sed -n '$=' $file);
	i=1;
	while [ $i -le $linenumber ]
	do
        	linedata=$(sed -n "$i p" $file);
        	if [ "$linedata" == "print(Problem:" ]
        	then
                	sed -i "$i d" $file;
		elif [ "$linedata" == ")" ]
		then
			sed -i "$i d" $file;
	 	elif [ "$linedata" == "\")" ]
        	then
                	sed -i "$i d" $file;
		elif [ "$linedata" == "print(\"" ]
		then 
			sed -i "$i d" $file;
		elif [ "$linedata" == "print(\"Solution:" ]
        	then
                	sed -i "$i d" $file;
		fi
	i=`expr $i + 1`;
	done
done
