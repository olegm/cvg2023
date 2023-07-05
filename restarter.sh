
Mm=$(date +%M | cut -c 2)

M=$(date +%M)


if [ $Mm = 9 ] 
then
	cd /home/lmiller/cvg2023
	git pull origin master
fi

if [ $Mm = 0 ] 
then
	sudo systemctl restart sensors
fi
#echo we are $M minutes
