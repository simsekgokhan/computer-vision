#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

/** Object Detection from Image Using HSV Color Space
**  (HSV -> Hue, Saturation, Value)
**/

int main(int argc, char** argv)
{
    //// 1. Create mask settings UI with default HSV range to detect blue color
    auto const MASK_WINDOW = "Mask Settings";
    cv::namedWindow(MASK_WINDOW, CV_WINDOW_AUTOSIZE);
    
    // HSV range to detect blue color
    int minHue = 90, maxHue = 140;
    int minSat = 74, maxSat = 255;
    int minVal =  0, maxVal = 255;

    // Create trackbars in mask settings window
    cvCreateTrackbar("Min Hue", MASK_WINDOW, &minHue, 255);
    cvCreateTrackbar("Max Hue", MASK_WINDOW, &maxHue, 255);
    cvCreateTrackbar("Min Sat", MASK_WINDOW, &minSat, 255);
    cvCreateTrackbar("Max Sat", MASK_WINDOW, &maxSat, 255);
    cvCreateTrackbar("Min Val", MASK_WINDOW, &minVal, 255);
    cvCreateTrackbar("Max Val", MASK_WINDOW, &maxVal, 255);

    while (true) {
        //// 2. Read and convert image to HSV color space
        cv::Mat inputImage { cv::imread("E:\\cv\\paralect.png", cv::IMREAD_COLOR) };
        cv::Mat inputImageHSV;
        cvtColor(inputImage, inputImageHSV, cv::COLOR_BGR2HSV);

        //// 3. Create mask and result (masked) image
        cv::Mat mask;
        inRange(inputImageHSV, cv::Scalar(minHue, minSat, minVal), cv::Scalar(maxHue, maxSat, maxVal), mask);
        cv::Mat resultImage;
        bitwise_and(inputImage, inputImage, resultImage, mask);

        //// 4. Show images        
        cv::imshow("Input Image", inputImage);
        cv::imshow("Result (Masked) Image", resultImage);
        // imshow("Mask", mask);

        //// Wait for 'esc' (27) key press for 30ms. If pressed, end program.
        if (cv::waitKey(30) == 27) break;
    }    
}