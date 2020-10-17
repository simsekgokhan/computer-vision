#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/objdetect.hpp>

/** Face Detection from Video 
**  (using Haar feature-based cascade classifiers)
**/

int main()
{
    //// 1. Load Haar feature-based cascade classifiers 
    cv::CascadeClassifier faceCascade { "haarcascade_frontalface_default.xml" } ;
    cv::CascadeClassifier eyesCascade { "haarcascade_eye_tree_eyeglasses.xml" } ;

    //// 2. Read from video file
    cv::VideoCapture videoCapture("para.mp4");
    cv::Mat inputFrame;
    cv::Mat inputFrameGray;
    while (true) {
        // Read video frames and convert to grayscale
        videoCapture.read(inputFrame);
        cvtColor(inputFrame, inputFrameGray, cv::COLOR_BGR2GRAY);

        //// 3. Find areas with faces using Haar cascade classifier
        std::vector<cv::Rect> faces;
        faceCascade.detectMultiScale(inputFrameGray, faces);

        for (size_t i = 0; i < faces.size(); i++) {
            cv::Point faceCenter { faces[i].x + faces[i].width/2, faces[i].y + faces[i].height/2 };
            cv::Size halfFace { faces[i].width/2, faces[i].height/2 };
            // input, center, axes, angle=0, startAngle=0, endAngle=360, color, thickness=2
            cv::ellipse(inputFrame, faceCenter, halfFace, 0, 0, 360, cv::Scalar(255, 0, 255), 2);
            // Get the region of interest : face rectangle sub - image in gray and colored
            cv::Mat faceROIGray { inputFrameGray(faces[i]) };

            //// 4. Find areas with eyes in faces using Haar cascade classifier
            std::vector<cv::Rect> eyes;
            eyesCascade.detectMultiScale(faceROIGray, eyes);
            for (size_t j = 0; j < eyes.size(); j++) {
                cv::Point eyeCenter { faces[i].x + eyes[j].x + eyes[j].width/2,
                                      faces[i].y + eyes[j].y + eyes[j].height/2 };
                int radius { cvRound((eyes[j].width + eyes[j].height) * 0.25) };
                // input, center, radius, color, thickness=2
                cv::circle(inputFrame, eyeCenter, radius, cv::Scalar(255, 0, 0), 2);
            }
        }

        //// 5. Show the output video
        cv::imshow("Face Detection - OpenCV", inputFrame);
        // Wait for 'esc' (27) key press for 20ms. If pressed, end program.
        if (cv::waitKey(20) == 27) break;
    }
}