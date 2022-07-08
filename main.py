#take folder of images as arguemtn
#run each image through yolo
#add results to a text file


def my_function (NName, fpath):
    
    for file in os.listdir("/mydir"):
        if file.endswith(".jpg" or ".png"):
            print(os.path.join("/mydir", file))
        for
