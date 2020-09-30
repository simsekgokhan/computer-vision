# computer-vision

### A. Cheat Sheet

// Install opencv-python  
pip install opencv-python  // macOS: use pip3, python3  
// Sample images  
https://github.com/opencv/opencv/tree/master/samples/data  
// Doc  
https://docs.opencv.org/4.3.0/d4/da8/group__imgcodecs.html#gga61d9b0126a3e57d9277ac48327799c80af660544735200cbe942eea09232eb822  
// OpenCV.js for Node.js  
https://docs.opencv.org/master/dc/de6/tutorial_js_nodejs.html  
// Opencv.js for WEB  
https://docs.opencv.org/3.4.3/d0/d84/tutorial_js_usage.html  

### B. How to call OpenCV C++ and Python programs from Node.JS:
Ref: https://nodejs.org/api/child_process.html#child_process_child_process_exec_command_options_callback


####  1. Call C++ program from NodeJS 

```
//C++
  int main()
  {
      auto const msg = "Sally Whittaker, 2018, McCarren House, 312, 3.75, Belinda Jameson, "
                       "2017, Cushing House, 148, 3.52, Jeff Smith, 2018, Prescott House, "
                       "17 - D, 3.20, Sandy Allen, 2019, Oliver House, 108, 3.48";
      std::cout << msg;
  }

// NodeJS
  const { exec } = require('child_process');
  const exeDir = 'E:\\c++\opencv-1\';
  exec('temp.exe img1.png', {cwd: exeDir}, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);  
    console.error(`stderr: ${stderr}`);
    // or make an array from stdout 
    const arr = stdout.split(',');
    console.log("arr:", arr);
    console.log("arr.len:", arr.length);
  });
  // 
  stdout: Sally Whittaker, 2018, McCarren House, 312, 3.75, Belinda Jameson, 2017, 
          Cushing House, 148, 3.52, Jeff Smith, 2018, Prescott House, 17 - D, 3.20, 
          Sandy Allen, 2019, Oliver House, 108, 3.48
  stderr:
    
  arr: [
    'Sally Whittaker', ' 2018',
    ' McCarren House', ' 312',
    ' 3.75',           ' Belinda Jameson',
    ' 2017',           ' Cushing House',
    ' 148',            ' 3.52',
    ' Jeff Smith',     ' 2018',
    ' Prescott House', ' 17 - D',
    ' 3.20',           ' Sandy Allen',
    ' 2019',           ' Oliver House',
    ' 108',            ' 3.48'
  ]
  arr.len: 20
```  

####  2. Call Python program from NodeJS 

```  
// Node.JS
  const { exec } = require('child_process');
  const exeDir = 'E:\PycharmProjects\\opencv-1';
  exec('python.exe main.py image.png', {cwd: exeDir}, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);  
    console.error(`stderr: ${stderr}`);
  });


// Python
  import sys
  import cv2
  import numpy as np

  def noop(x): return None

  print(cv2.__version__)

  image = cv2.imread('paralect.png')
  imageHsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

  # print ("Msg from python: 1st arg is", sys.argv[1])
  # print ('Number of arguments:', len(sys.argv), 'arguments.')
  # print ('Argument List:', str(sys.argv))
  # print ('Arg-1:', sys.argv[1])
````
  
