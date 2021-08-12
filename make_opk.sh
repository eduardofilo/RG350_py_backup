#!/bin/sh

# Stock version
OPK_NAME=py_backup_`cat v`_stock.opk

echo ${OPK_NAME}

# create default.gcw0.desktop
cat > default.gcw0.desktop <<EOF
[Desktop Entry]
Name=Py Backup
Comment=Backup of selected directories/files
Exec=py_backup.sh
Terminal=false
Type=Application
StartupNotify=true
Icon=py_backup
Categories=applications;
EOF

cp config2.py config.py

# create opk
FLIST="config.ini"
FLIST="${FLIST} app.py"
FLIST="${FLIST} config.py"
FLIST="${FLIST} footer.py"
FLIST="${FLIST} header.py"
FLIST="${FLIST} keys.py"
FLIST="${FLIST} main.py"
FLIST="${FLIST} settings.py"
FLIST="${FLIST} states.py"
FLIST="${FLIST} v"
FLIST="${FLIST} resources"
FLIST="${FLIST} py_backup.png"
FLIST="${FLIST} py_backup.sh"
FLIST="${FLIST} default.gcw0.desktop"

rm -f ${OPK_NAME}
mksquashfs ${FLIST} releases/${OPK_NAME} -all-root -no-xattrs -noappend -no-exports

cat default.gcw0.desktop
rm -f default.gcw0.desktop

echo ""
echo ${OPK_NAME} created in releases.

# ODBeta version
OPK_NAME=py_backup_`cat v`_odbeta.opk

echo ${OPK_NAME}

# create default.gcw0.desktop
cat > default.gcw0.desktop <<EOF
[Desktop Entry]
Name=Py Backup
Comment=Backup of selected directories/files
Exec=py_backup.sh
Terminal=false
Type=Application
StartupNotify=true
Icon=py_backup
Categories=applications;
EOF

cp config3.py config.py

# create opk
FLIST="config.ini"
FLIST="${FLIST} app.py"
FLIST="${FLIST} config.py"
FLIST="${FLIST} footer.py"
FLIST="${FLIST} header.py"
FLIST="${FLIST} keys.py"
FLIST="${FLIST} main.py"
FLIST="${FLIST} settings.py"
FLIST="${FLIST} states.py"
FLIST="${FLIST} v"
FLIST="${FLIST} resources"
FLIST="${FLIST} py_backup.png"
FLIST="${FLIST} py_backup.sh"
FLIST="${FLIST} default.gcw0.desktop"

rm -f ${OPK_NAME}
mksquashfs ${FLIST} releases/${OPK_NAME} -all-root -no-xattrs -noappend -no-exports

cat default.gcw0.desktop
rm -f default.gcw0.desktop

echo ""
echo ${OPK_NAME} created in releases.

#scp releases/${OPK_NAME} rg350:/media/data/apps
