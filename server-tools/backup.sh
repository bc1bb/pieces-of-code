#!/usr/bin/env bash
# simple backup script (github:jusdepatate/shell-tools)
# Made for an Arch Linux server environment

if [ "$EUID" -ne 0 ]; then
  echo "[ERROR] Execute as Super User"
  exit 1
fi

cd ~

echo "Starting backup..."
echo "[START] Backup started on $(date -u)" > backup.log

echo "[mkdir] Creating required folders ($(date -u))" | tee -a backup.log
mkdir backup 2>>backup.log
mkdir backup/pacman 2>>backup.log

echo "[cp] Backing up /srv ($(date -u))" | tee -a backup.log
cp -R /srv backup/ 2>>backup.log

echo "[cp] Backing up /etc ($(date -u))" | tee -a backup.log
cp -R /etc backup/ 2>>backup.log

echo "[pacman] Backing up software installed thru Pacman ($(date -u))" | tee -a backup.log
pacman -Q 2>>backup.log > backup/pacman/installed

echo "[mysqldump] Backing up MySQL databases ($(date -u))" | tee -a backup.log
mysqldump -A -Y -C -f -u root > backup/mariadb.sql 2>>backup.log

echo "[tar] Compressing backup ($(date -u))" | tee -a backup.log
tar -cvpJf backup.tar.xz backup 2>>backup.log
rm -r ~/backup &>>backup.log

echo "[info] Backup log in file ~/backup.log"
echo "[info] Backup is in file backup.tar.xz"
echo "Ending Backup..."

echo "[END] Backup ended on $(date -u)" >> backup.log

cd - &>/etc/null
exit 0
