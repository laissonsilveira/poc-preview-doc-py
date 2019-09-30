#!/usr/bin/env python3
import sys, traceback
from os import path, rename, environ
from shutil import rmtree
from preview_generator.manager import PreviewManager

cache_path = ".tmp"

if len(sys.argv) < 2 or not(path.isfile(sys.argv[1])):
    sys.exit("Nome ou caminho do arquivo não informado corretamente")

def show_error(err):
    traceback.print_tb(sys.exc_info()[2])
    sys.exit(err)
    return

try:
    file_source = sys.argv[1]
    file_name = path.basename(file_source)
    manager = PreviewManager(cache_path, create_folder= True)
    path_preview = manager.get_jpeg_preview(file_name, width=140)
    new_file_name = path.splitext(file_name)[0] + "_thumbnail.jpeg"
    # path_preview = manager.get_text_preview(file_name)
    # new_file_name = path.splitext(file_name)[0] + "_thumbnail.txt"
    rename(path_preview, new_file_name)
except FileNotFoundError as e:
    error = "File[{0}] - FileNotFoundError({1}): {2}".format(file_source, e.errno, e.strerror)
    show_error(error)
except:
    error = "File[{0}] - Erro Desconhecido".format(file_source)
    show_error(error)
finally:
    rmtree(cache_path)
