#!/usr/bin/env python3
import sys
from os import path, rename, environ
from shutil import rmtree
from preview_generator.manager import PreviewManager

cache_path = "./tmp"

if len(sys.argv) < 2 or not(path.isfile(sys.argv[1])):
    sys.exit("Nome ou caminho do arquivo não informado corretamente")

try:
    file_source = sys.argv[1]
    file_name = path.basename(file_source)

    manager = PreviewManager(cache_path, create_folder= True)
    path_preview = manager.get_jpeg_preview(file_name, width=140)

    new_file_name = path.splitext(file_name)[0] + "_thumbnail.jpeg"
    rename(path_preview, new_file_name)

    rmtree(cache_path)
except FileNotFoundError as e:
    error = "File[{0}] - FileNotFoundError({1}): {2}".format(file_source, e.errno, e.strerror)
    sys.exit(error)
except:
    error = "File[{0}] - Error Desconhecido".format(file_source)
    sys.exit(error)
