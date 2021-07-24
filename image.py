import os
import multiprocessing
import time
from PIL import Image, ImageFilter

img_names = os.listdir("./images")
size = (1200, 1200)


def process_sync():
    print("Synchronous")
    start = time.perf_counter()
    for img_name in img_names:
        process_image(img_name)

    end = time.perf_counter()
    print(f"Finished in {round(end-start, 2)} seconds")
    print()


def process_async():
    print("Asynchronous")
    start = time.perf_counter()

    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        pool.map(process_image, img_names)

    end = time.perf_counter()
    print(f"Finished in {round(end-start, 2)} seconds")
    print()


def process_image(img_name):
    img = Image.open(f"./images/{img_name}")

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f"processed/{img_name}")
    print(f"{img_name} was processed...")


if __name__ == "__main__":
    process_sync()
    process_async()
