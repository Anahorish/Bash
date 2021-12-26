#!/bin/bash

ps -fC bash | grep ^root

if [[ $? -eq 0 ]]; then
	echo "root is active" | systemd-cat -p warning
fi

#if [[ ! -z $(ps -fC bash | grep ^root) ]]
#if [[ $(ps -fC bash | grep ^root | wc -l) -gt 0 ]]
