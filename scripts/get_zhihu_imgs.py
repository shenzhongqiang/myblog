import os
import re
import sys
import requests

IMAGE_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "images")

def download_image(url):
    r = requests.get(url, verify=False)
    filename = url.split("/")[-1]
    img_path = os.path.join(IMAGE_DIR, filename)
    with open(img_path, "wb") as f:
        f.write(r.content)
        print("downloaded {}".format(filename))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    filepath = sys.argv[1]
    with open(filepath, "r") as f:
        content = f.read()
        matched = re.findall(r"(https://.*?zhimg.com/.*?jpg)", content, re.M)
        for url in matched:
            download_image(url)
