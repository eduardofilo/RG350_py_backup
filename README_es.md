![Py Backup Icon](images/logo.png)

# Py Backup

Py Backup es un programa que nos va a facilitar la gestión de los backups en las consolas RG350 y RG280. Está pensado principalmente para respaldar los directorios donde se almacenan los savestates (las partidas) de los emuladores, pero modificando su configuración podemos utilizarlo para hacer backup de cualquier fichero o directorio de la consola.

## Instalación

La aplicación tiene forma de OPK, por lo que se instalará como habitualmente copiando el fichero a una de las dos rutas que explora GMenu2X para mostrar los lanzadores, es decir:

* Tarjeta interna: `/media/data/apps`
* Tarjeta externa (en ODBeta sólo cuando la tarjeta no tiene label): `/media/sdcard/apps`

El OPK lo podemos bajar de la sección [releases](https://github.com/eduardofilo/RG350_py_backup/releases) de este repositorio.

Una vez instalada, podremos encontrar la aplicación en la sección *Applications* de los distintos lanzadores:

![GMenu2X](images/gmenu2x.png)
![PyMenu](images/pymenu.png)
![SimpleMenu](images/simplemenu.png)

## Configuración

La configuración de Py Backup se hace por medio del fichero que se crea en la siguiente ruta la primera vez que se ejecuta:

```
/media/data/local/home/.py_backup/config.ini
```

Por defecto viene con las rutas de los directorios de savestate de varios emuladores populares:

```
[DEFAULT]
destination_directory = /media/sdcard/backups
systems =
    Stella (A2600),True,/media/data/local/home/.stella/state
    FBA,True,/media/data/local/home/.fba/saves
    FCEUX (NES),True,/media/data/local/home/.fceux/fcs
    Gambatte (GB/GBC),True,/media/data/local/home/.gambatte/saves
    ReGBA (GBA),True,/media/data/local/home/.gpsp
    SMS Plus (GG/SMS),True,/media/data/local/home/.smsplus/state
    Genesis Plus (GG/SMS/MD),True,/media/data/local/home/.genplus/saves
    PicoDrive (MD),True,/media/data/local/home/.picodrive/mds
    Handy (LYNX),True,/media/data/local/home/.handy
    NGPCEmu (NGP),True,/media/data/local/home/.ngpcemu/sstates
    Temper (PCE),True,/media/data/local/home/.temper/save_states
    PCSX4All (PS),True,/media/data/local/home/.pcsx4all/sstates,/media/data/local/home/.pcsx4all/memcards
    PocketSNES (SNES),True,/media/data/local/home/.pocketsnes
    SwanEmu (WS),True,/media/data/local/home/.swanemu/sstates
    xMAME (ARCADE),True,/media/data/local/share/xmame/xmame52/sta,/media/data/local/share/xmame/xmame69/sta,/media/data/local/share/xmame/xmame84/sta
    ScummVM,True,/media/data/local/home/.local/share/scummvm/saves
    OpenBOR,True,/media/data/local/home/.OpenBOR/Saves
    Ports,True,/media/data/local/home/.nxengine,/media/data/local/home/.local/share/VVVVVV/saves,/media/data/local/home/.methane,/media/data/local/home/.sorrv5/savegame
    VBEmu (VB),True,/media/data/local/home/.vbemu/sstates
    RetroArch,True,/media/data/local/home/.retroarch/states,/media/data/local/home/.retroarch/config,/media/data/local/home/.retroarch/playlists,/media/data/local/home/.retroarch/records,/media/data/local/home/.retroarch/retroarch.cfg
    Amstrad CPC (AMSTRAD),True,/media/data/local/home/.dingux-cap32/save
    OpenMSX (MSX),True,/media/data/local/home/.openMSX/savestates
```

Como vemos dentro del fichero de tipo [INI](https://es.wikipedia.org/wiki/INI_(extensi%C3%B3n_de_archivo)) encontramos dos parámetros:

* `destination_directory`: Contiene la ruta sobre la que queremos que se dejen los backups.
* `systems`: Contiene los varios (uno por linea) ficheros de backup que podemos crear y gestionar por separado. Normalmente cada uno de estos ficheros estará asociado a un emulador o sistema.

Los ficheros de backup indicados en el parámetro `systems` se configuran por una serie de elementos separados por comas en el siguiente orden:

1. Nombre del fichero de backup. Una vez ejecutado el backup encontraremos un fichero con este nombre y extensión `tgz` en el directorio indicado en `destination_directory`.
2. `True` o `False` para indicar si queremos activar o desactivar el fichero de backup. Esto puede modificarse fácilmente desde el propio interfaz del programa como luego veremos.
3. Listado de ficheros o directorios (separados por comas) que se incluirán en el fichero de backup.

Es importante que las lineas que contienen las definiciones de los ficheros de backup estén indentados con 4 espacios o un tabulador.

Por ejemplo vamos a analizar la configuración del fichero de backup siguiente:

```
    PCSX4All (PS),True,/media/data/local/home/.pcsx4all/sstates,/media/data/local/home/.pcsx4all/memcards
```

Al ejecutar el backup, aparecerá un fichero de nombre `PCSX4All (PS).tgz` en el directorio `/media/sdcard/backups` y con el contenido de los dos siguientes directorios:

* `/media/data/local/home/.pcsx4all/sstates`
* `/media/data/local/home/.pcsx4all/memcards`

## Utilización

Cuando abramos la aplicación por primera vez encontraremos los ficheros de backup definidos en la configuración predeterminada. Dependiendo de si tenemos instalados en nuestra consola los emuladores relacionados con estos ficheros, éstos aparecerán coloreados de una u otra forma que luego explicaremos. En caso de tener todos los emuladores instalados, seguramente veremos algo como lo siguiente:

![First launch](images/first_launch.png)

En todo momento la aplicación indica los controles disponibles para su manejo. Según lo visto en la pantalla anterior, en este caso lo que podríamos hacer es navegar por los distintos ficheros con Arriba/Abajo, marcar o desmarcar (*toggle*) con la tecla `A` y finalmente ejecutar el backup con la tecla `B`.

Como decíamos antes, el color con que se representa cada fichero tiene un significado. Por ejemplo en el siguiente fragmento vemos los tres colores posibles:

![Backup colors](images/backup_colors.png)

El significado de cada color aplicado a estos tres ficheros se interpreta de la siguiente forma:

* Blanco: Se puede hacer backup y restaurar.
* Rojo: Se puede hacer backup pero no restaurar. Típicamente porque todavía no se ha hecho el primer backup.
* Gris: No se puede hacer backup ni restaurar. Típicamente porque no existen los ficheros o directorios configurados para este backup, seguramente porque no tenemos instalado el sistema correspondiente en nuestra máquina.

La marca que aparece a la izquierda de cada fichero de backup sirve para especificar si queremos que dicho fichero forme parte de las operaciones de backup o restauración que ejecutaremos a partir de entonces.

Cuando existan ficheros de backup ya realizados (color blanco) y alguno de éstos se encuentre marcado (marca a la izqierda), veremos que aparece un nuevo control que nos permite realizar la restauración, la tecla `X` (*restore*). La restauración sólo se realizará de los ficheros de los que exista backup. Por ejemplo en la siguiente configuracion, si ejecutamos una restauración de los backups, sólo se restaurará el primer fichero (`Stella (A2600)` que aparece en blanco) y no el del segundo (`FBA` que aparece en rojo) a pesar de que ambos están marcados para ser ejecutados:

![Selective backup](images/selective_backup.png)

La ejecución del backup sí se realizará sobre los dos ficheros, y de hecho al finalizar, el segundo pasará a tomar color blanco al permitir ya la restauración:

![Backup done](images/backup_done.png)

Podemos comprobar la generación de ambos backups (en realidad la repetición del primero y la creación del segundo) si exploramos los ficheros que existen en el directorio donde se dejan los backups (si no se modifica la configuración será `/media/sdcard/backups`):

![Check backup](images/check_backup.png)

Al ejecutar las operaciones de backup y restauración se nos pedirá confirmación por medio de un pequeño popup:

![Confirm backup](images/confirm_backup.png)

Por último, una vez confirmada la operación podremos ver el progreso del backup o la restauración, indicándose los ficheros de backup realizados o restaurados. Al realizar el primer backup observaremos además cómo cambia la coloración de rojo a blanco, indicando la aparición de los ficheros de backup que permiten la restauración a partir de entonces (al principio del video se desactiva el backup de PCSX4All por tardar demasiado para el propósito del vídeo):

[![Ver vídeo](https://img.youtube.com/vi/pDfXigJ-QiI/hqdefault.jpg)](https://www.youtube.com/watch?v=pDfXigJ-QiI "Ver vídeo")

La aplicación puede ser cerrada en cualquier momento pulsando la tecla `START`.
