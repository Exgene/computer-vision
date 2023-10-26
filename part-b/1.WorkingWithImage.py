import cv2
# Function to process images


def process_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("OriginalImage", image)
    # Wait for key press to close the image
    cv2.waitKey(0)
    cv2.imshow("GrayScaleImage", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def process_video(video_path):
    # Open a video capture object
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Display the video frame
        cv2.imshow("Video", frame)
        # Press 'q' to exit the playback
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()


choice = input("Enter 'I' for images and 'V' for Video:")

if choice.lower() == 'i':
    image = cv2.imread('/home/student/Downloads/JOJO.jpg')
    process_image(image)
elif choice.lower() == 'v':
    # Load a video
    video_path = f'/home/student/Downloads/m2-res_270p.mp4'
    process_video(video_path)
else:
    print("Invalid af")
