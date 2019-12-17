import anki_vector
from PIL import Image  
import PIL 
with anki_vector.Robot() as robot:
    image = robot.camera.capture_single_image()
    image.raw_image.show()
    image.raw_image.save("anh.jpg")

import requests
KERAS_REST_API_URL = "http://localhost:5000/predict"
IMAGE_PATH = "anh.jpg" 
# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read() 
payload = {"image": image}

# submit the request
r = requests.post(KERAS_REST_API_URL, files=payload).json()

# ensure the request was sucessful
if r["success"]:
    # loop over the predictions and display them
    #for (i, result) in enumerate(r["predictions"]):
        #print("{}. {}: {:.4f}".format(i + 1, result["label"],
            #result["probability"]))
                print("do la"+r["predictions"][0]['label'])

# otherwise, the request failed
else:
    print("Request failed")


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Say 'Hello World'...")
        robot.behavior.say_text("It's seem be a {}".format(r["predictions"][0]['label']))


if __name__ == "__main__":
    main()
