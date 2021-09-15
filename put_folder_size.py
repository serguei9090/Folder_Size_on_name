#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
import os
def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)


def pause():
   programPause = input("Press the <ENTER> key to continue...")
print("******************************************************************************************")
print("*Este Script Añade el tamaño total de la carpeta a su nombre, Gracias (Market)           *")
print("******************************************************************************************")
pause()
actual_dir = os.listdir(os.getcwd())
for dirs in actual_dir:
   if os.path.isdir(dirs):
      root_directory = Path(dirs)
      size_file = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
      size_file_calc=humanbytes(size_file)
      old_name=str(dirs)
      new_name=str(dirs) + ' ' + '(' + str(size_file_calc) + ')'
      os.rename(old_name, new_name)
print("******************************************************************************************")
print("*Gracias por usar el Software, Producido por Market                                      *")
print("*Prestamos Servicio de Creacion de Catalogos para Bancos de Audiovisuales                *")
print("*Tel-Whatsapp:+53 52472074                                                               *")
print("******************************************************************************************")

pause()







