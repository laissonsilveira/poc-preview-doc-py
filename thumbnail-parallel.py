from preview_generator.manager import PreviewManager
from os import listdir, stat
from multiprocessing import Pool
from shutil import rmtree
import time

start_total = time.time()

pathPreview = "preview"
rmtree(pathPreview)

manager = PreviewManager(pathPreview, create_folder=True)

def make_preview(file):
        path_file = "files-to-convert/" + file
        start = time.time()
        path_to_preview_image = manager.get_jpeg_preview(path_file, width=140)
        end = time.time()
        print("PREVIEW -> %s: %s seconds" % (path_to_preview_image.replace(pathPreview + "/", ""), end - start))
        print("--------------------")

p = Pool(4)
p.map(make_preview, listdir("files-to-convert"))

end_total = time.time()
print("Total time: %s seconds" % (end_total - start_total))
