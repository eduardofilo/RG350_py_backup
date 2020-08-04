#!/bin/sh

OPK_NAME=pystatesbackup.opk

echo ${OPK_NAME}

# create default.gcw0.desktop
cat > default.gcw0.desktop <<EOF
[Desktop Entry]
Name=Py States Backup
Comment=Savestates directories backup
Exec=pystatesbackup.sh
Terminal=false
Type=Application
StartupNotify=true
Icon=pystatesbackup
Categories=applications;
EOF

# create opk
FLIST="config.txt"
FLIST="${FLIST} main.py"
FLIST="${FLIST} keys.py"
FLIST="${FLIST} app.py"
FLIST="${FLIST} resources"
FLIST="${FLIST} pystatesbackup.png"
FLIST="${FLIST} pystatesbackup.sh"
FLIST="${FLIST} default.gcw0.desktop"

rm -f ${OPK_NAME}
mksquashfs ${FLIST} releases/${OPK_NAME} -all-root -no-xattrs -noappend -no-exports

cat default.gcw0.desktop
rm -f default.gcw0.desktop

echo ""
echo ${OPK_NAME} created in releases.

scp releases/${OPK_NAME} rg350:/media/data/apps
