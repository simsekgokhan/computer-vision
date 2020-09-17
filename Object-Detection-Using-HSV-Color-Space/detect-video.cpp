#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

/** Object detection from video using HSV color space
**  (HSV -> Hue, Saturation, Value)
**/

int main()
{
    //// 1. Create mask control window with default HSV range to detect blue color
    auto const MASK_WINDOW = "Mask Settings";
    cv::namedWindow(MASK_WINDOW, CV_WINDOW_AUTOSIZE);

    // HSV range to detect blue color
    int minHue = 90, maxHue = 140;
    int minSat = 74, maxSat = 255;
    int minVal =  0, maxVal = 255;

    // Create trackbars in mask settings window
    cvCreateTrackbar("Min Hue", MASK_WINDOW, &minHue, 179);
    cvCreateTrackbar("Max Hue", MASK_WINDOW, &maxHue, 179);
    cvCreateTrackbar("Min Sat", MASK_WINDOW, &minSat, 255);
    cvCreateTrackbar("Max Sat", MASK_WINDOW, &maxSat, 255);
    cvCreateTrackbar("Min Val", MASK_WINDOW, &minVal, 255);
    cvCreateTrackbar("Max Val", MASK_WINDOW, &maxVal, 255);

    //// 2. Capture from default camera
    cv::VideoCapture videoCapture(0);

    while (true) {
        //// 3. Capture and convert video to HSV color space
        cv::Mat inputVideo;
        videoCapture.read(inputVideo);
        cv::flip(inputVideo, inputVideo, 1);
        cv::Mat inputVideoHSV;
        cv::cvtColor(inputVideo, inputVideoHSV, cv::COLOR_BGR2HSV);

        //// 4. Create mask and result (masked) video
        cv::Mat mask;
        inRange(inputVideoHSV, cv::Scalar(minHue, minSat, minVal), cv::Scalar(maxHue, maxSat, maxVal), mask);
        cv::Mat resultVideo;
        bitwise_and(inputVideo, inputVideo, resultVideo, mask);

        //// 5. Show videos        
        imshow("Input Video", inputVideo);
        imshow("Result (Masked) Video", resultVideo);
        // imshow("Mask", mask);

        //// Wait for 'esc' (27) key press for 30ms. If pressed, end program.
        if (cv::waitKey(30) == 27) break;
    }
}