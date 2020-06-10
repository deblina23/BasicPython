#! /usr/bin/sh
for file in `find /home/ec2-user/gitrepo/BasicPython/scripts -iname "*.py"`
do
	number=$(echo $file|sed -n 's|/home/ec2-user/gitrepo/BasicPython/scripts/exercise\(.*\)\.py|\1| p');
	linenumber=$(sed -n '$=' /home/ec2-user/gitrepo/BasicPython/scripts/test1.txt);
	i=1;
	while [ $i -le $linenumber ]
	do
		value=$(sed -n "$i s/\.\(.*\)/ / p" /home/ec2-user/gitrepo/BasicPython/scripts/test1.txt) ;
		if [ $value -eq $number ]
        	then
                	problem=$(sed -n "$i s/[0-9]*\./ / p" /home/ec2-user/gitrepo/BasicPython/scripts/test1.txt);
			sed -i "1a print(\"Problem:\"\)\nprint\(\" $problem \"\)\nprint\(\"Solution:\"\)" $file;
		fi
	i=`expr $i + 1`;
	done
done
