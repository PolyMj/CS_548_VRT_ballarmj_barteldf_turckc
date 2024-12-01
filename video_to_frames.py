import sys
import os
import cv2


# Run program with arguments: "Video_filepath" "Frame directory"

def main():
    if len(sys.argv) < 3:
        print("NEED AT LEAST TWO ADDITIONAL ARGUMENTS: video_filepath | frame_dir")
        exit(-1)
    
    video_filepath = sys.argv[1]
    frame_dir = sys.argv[2]
    
    video_filename = os.path.splitext(os.path.basename(video_filepath))[0]
    
    os.makedirs(frame_dir)
    
    print("\nInfo: ")
    print("Video path = ", video_filepath)
    print("Video name = ", video_filename)
    print("Frame directory = ", frame_dir)
    
    capture = cv2.VideoCapture(video_filepath)
    frame_index = 0
    
    while True:
        ret, frame = capture.read()
        
        if not ret:
            print("Total frames:", frame_index+1)
            break
            
        output_frame_path = f"{frame_dir}/{frame_index:05d}.png"
        print(output_frame_path)
        
        if not cv2.imwrite(output_frame_path, frame):
            print("ERROR: Failed to write frame", frame_index)
        
        frame_index += 1
    

if __name__ == "__main__":
    main()