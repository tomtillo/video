# ---------------------------- Function to get frames every second ( and not all the frames)
# Using tqdm to show progressbar
# Usage :extract_frames_every_second(videos1,OUT_DIR)
# Returns: times taken

def extract_frames_every_second(video_file, output_folder):
    import tqdm
    t1= time.time()

    cap = cv2.VideoCapture(video_file)
    duration_seconds= cap.get(7) / cap.get(5)
    pbar = tqdm.tqdm(total=duration_seconds)

    ret = 1
    frame_number = 1
    frameRate = cap.get(5)  # frame rate
    while (ret):

        frame_number += 1
        frameId = cap.get(1)  # current frame number
        if (ret != True):
            break
        ret, frame = cap.read()
        if (frameId % math.floor(frameRate) == 0):
            pbar.update(1)
            out_k2 = cv2.imwrite(output_folder + "im_" + str(frame_number) + ".jpg", frame)

    cap.release()
    t2 = time.time()
    time_taken= t2-t1
    return(time_taken)
# ----------------------------------- End Function ------------    

videos1 = "./videos/video1.mp4"
OUT_DIR = "./output/"
t1 = extract_frames_every_second(videos1,OUT_DIR)
print("Time taken = %s " %(t1))
