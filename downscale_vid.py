import cv2
import os

def downscale_images(input_folder, output_folder, scale_factor):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)

            # resize image down
            width = int(img.shape[1] * scale_factor)
            height = int(img.shape[0] * scale_factor)
            resized_img = cv2.resize(img, (width, height))

            # save
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resized_img)

if __name__ == "__main__":
    input_folder = "testsets/gopro_test_GT/GOPR0871_11_00_this_one"
    output_folder = "testsets/downscaled/gopro/00"
    downscale_images(input_folder, output_folder, 0.25)