#!/bin/bash

if [[ ! -w /srv/files/HOWTO ]] ; then echo "Unable to write in /srv/files" ; exit 1 ; fi

cd /srv/files/ && du -sh > totalsize
echo -n "$(sed 's/	.//' /srv/files/totalsize)" > /srv/files/totalsize

cd /srv/files/ && du -h --max-depth=2 eve/ > eve/size