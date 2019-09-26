import time, os
from shutil import rmtree

start_total = time.time()

from preview_generator.manager import PreviewManager

pathPreview = "preview"
pathIn = "files"
rmtree(pathPreview)

manager = PreviewManager(pathPreview, create_folder= True)

total_size = 0
total_size_preview = 0
for r, d, f in os.walk(pathIn):
    for file in f:
        path_file = pathIn + "/" + file
        size = os.stat(path_file).st_size
        print("FILE -> '%s' - size: %s bytes" % (file, size))
        total_size = total_size + size

        start = time.time()
        try:
            path_to_preview_image = manager.get_jpeg_preview(path_file, width=140)
        except FileNotFoundError as e:
            print("ERROR -> File[{0}] - FileNotFoundError({1}): {2}".format(file, e.errno, e.strerror))
        except KeyError as e:
            print("ERROR -> File[{0}] - KeyError({1}): {2}".format(file, e.errno, e.strerror))
        except:
            print("ERROR -> File[{0}] - Error Desconhecido".format(file))
        
        end = time.time()

        size_preview = os.stat(path_to_preview_image).st_size
        total_size_preview = total_size_preview + size_preview
        
        print("PREVIEW -> %s: %s seconds / size: %s bytes" % (path_to_preview_image.replace(pathPreview + "/", ""), end - start, size_preview))
        print("--------------------")

end_total = time.time()

print("Total size: %s bytes" % (total_size))
print("Total size preview: %s bytes" % (total_size_preview))
print("Total time: %s seconds" % (end_total - start_total))