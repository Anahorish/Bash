#!/bin/bash
#Automatically create or remove a variable number of users, create home directory, include welcome file in home directory and set passwords for accounts.

if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root"
	exit 1
fi

read -p "Would you like to create or remove users?: " ACTION

if ! [[ $ACTION =~ ^[a-z]*$ ]]
then
	echo "Please type either 'create' or 'remove'.";
	exit 1
fi

read -p "How many?: " NUMBER

if ! [[ $NUMBER =~ ^[0-9]*$ ]]
then
	echo "Please input a number between 1 and 20.";
	exit 1
fi

if [[ $NUMBER -gt 20 ]]
then
	echo "Please choose a number smaller than 20.";
fi

if [[ $NUMBER -lt 20 && $ACTION == "create" ]]
then
	until [[ $NUMBER -eq 0 ]]
	do
		while
			i=$(($i+1))
			USERNAM="user$i"
			id $USERNAM > logfile 2> errorlog
		do :
	 	done	
		useradd -s /usr/bin/bash -m $USERNAM;
		cat <<-EOF> /home/$USERNAM/welcome.txt
		Welcome to your new Linux account!
EOF
		echo "Please set a password for the new user."
		passwd $USERNAM
	let NUMBER=$NUMBER-1;
	echo "$USERNAM has been created."
	done;
fi

if [[ $NUMBER -lt 20 && $ACTION == "remove" ]]
then
	until [[ $NUMBER -eq 0 ]]
	do
		read -p "Which user would you like to remove?: " USERDEL
		userdel -r $USERDEL > logfile 2> errorlog
		let NUMBER=$NUMBER-1;
		echo "$USERDEL has been removed."
	done;
fi
