
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/dnn.hpp>
#include <opencv2/highgui.hpp>
#include <fstream>
#include <iostream>
#include <opencv2/core/ocl.hpp>
#include "tensorflow/lite/interpreter.h"
#include "tensorflow/lite/kernels/register.h"
#include "tensorflow/lite/string_util.h"
#include "tensorflow/lite/model.h"
#include <cmath>

using namespace cv;
using namespace std;

int main(){
    chrono::steady_clock::time_point Tbegin, Tend;

    Tbegin = chrono::steady_clock::now();
    Tend = chrono::steady_clock::now();
    f = chrono::duration_cast <chrono::milliseconds> (Tend - Tbegin).count();

    cout << f <<endl;
    return 0



}
