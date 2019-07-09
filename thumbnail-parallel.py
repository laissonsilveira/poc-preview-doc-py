from preview_generator.manager import PreviewManager
from os import listdir, stat
from multiprocessing import Pool
import time

start_total = time.time()

manager = PreviewManager("preview", create_folder=True)

def make_preview(file):
        path_file = "files-to-convert/" + file
        statinfo = stat(path_file)
        print("File '%s' - size: %s bytes" % (file, statinfo.st_size))

        start = time.time()
        path_to_preview_image = manager.get_jpeg_preview(path_file)
        end = time.time()
        print("%s: %s seconds" % (path_to_preview_image, end - start))

        start = time.time()
        path_to_preview_image = manager.get_jpeg_preview(
        path_file, width=140)
        end = time.time()
        print("%s: %s seconds" % (path_to_preview_image, end - start))

        start = time.time()
        path_to_preview_image = manager.get_jpeg_preview(
        path_file, width=140, page=0)
        end = time.time()
        print("One page - %s: %s seconds" % (path_to_preview_image, end - start))
        print("--------------------")

            
p = Pool(4)
p.map(make_preview, listdir("files-to-convert"))

end_total = time.time()
print("Total time: %s seconds" % (end_total - start_total))
