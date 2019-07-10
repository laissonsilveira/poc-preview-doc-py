import time, os
from shutil import rmtree

start_total = time.time()

from preview_generator.manager import PreviewManager

pathPreview = "preview"
rmtree(pathPreview)

manager = PreviewManager(pathPreview, create_folder= True)

total_size = 0
total_size_preview = 0
for r, d, f in os.walk("files-to-convert"):
    for file in f:
        path_file = "files-to-convert/" + file
        size = os.stat(path_file).st_size
        print("FILE -> '%s' - size: %s bytes" % (file, size))
        total_size = total_size + size

        start = time.time()
        path_to_preview_image = manager.get_jpeg_preview(path_file, width=140)
        end = time.time()

        size_preview = os.stat(path_to_preview_image).st_size
        total_size_preview = total_size_preview + size_preview
        
        print("PREVIEW -> %s: %s seconds / size: %s bytes" % (path_to_preview_image.replace(pathPreview + "/", ""), end - start, size_preview))
        print("--------------------")

end_total = time.time()

print("Total size: %s bytes" % (total_size))
print("Total size preview: %s bytes" % (total_size_preview))
print("Total time: %s seconds" % (end_total - start_total))