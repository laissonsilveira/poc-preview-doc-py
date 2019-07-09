import time, os
start_total = time.time()

from preview_generator.manager import PreviewManager

manager = PreviewManager("preview", create_folder= True)

total_size = 0
for r, d, f in os.walk("files-to-convert"):
    for file in f:
        path_file = "files-to-convert/" + file
        statinfo = os.stat(path_file)
        print("File '%s' - size: %s bytes" % (file, statinfo.st_size))
        total_size = total_size + statinfo.st_size

        start = time.time()
        path_to_preview_image = manager.get_jpeg_preview(path_file)
        end = time.time()
        print("%s: %s seconds" % (path_to_preview_image, end - start))

        start = time.time()
        path_to_preview_image = manager.get_jpeg_preview(path_file, width=140)
        end = time.time()
        print("%s: %s seconds" % (path_to_preview_image, end - start))

        start = time.time()
        path_to_preview_image = manager.get_jpeg_preview(path_file, width=140, page=0)
        end = time.time()
        print("One page - %s: %s seconds" % (path_to_preview_image, end - start))
        print("--------------------")

end_total = time.time()
print("Total size: %s bytes" % (total_size))
print("Total time: %s seconds" % (end_total - start_total))