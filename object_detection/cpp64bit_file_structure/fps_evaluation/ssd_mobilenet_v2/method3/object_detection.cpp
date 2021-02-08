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

const size_t width = 300;
const size_t height = 300;

std::vector<std::string> Labels;
std::unique_ptr<tflite::Interpreter> interpreter;

static bool getFileContent(std::string fileName)
{
	// Open the File
	std::ifstream in(fileName.c_str());
	// Check if object is valid
	if(!in.is_open()) return false;

	std::string str;
	// Read the next line from File untill it reaches the end.
	while (std::getline(in, str))
	{
		// Line contains string of length > 0 then save it in vector
		if(str.size()>0) Labels.push_back(str);
	}
	// Close The File
	in.close();
	return true;
}

float detect_from_video(Mat &src)
{
    Mat image;
    int cam_width =src.cols;
    int cam_height=src.rows;
    chrono::steady_clock::time_point Tbegin, Tend;
    float f;
    // copy image to input as input tensor

        //calculate frame rate

    Tbegin = chrono::steady_clock::now();
    cv::resize(src, image, Size(width,height));
    memcpy(interpreter->typed_input_tensor<uchar>(0), image.data, image.total() * image.elemSize());

    interpreter->SetAllowFp16PrecisionForFp32(true);
    interpreter->SetNumThreads(4);      //quad core

//        cout << "tensors size: " << interpreter->tensors_size() << "\n";
//        cout << "nodes size: " << interpreter->nodes_size() << "\n";
//        cout << "inputs: " << interpreter->inputs().size() << "\n";
//        cout << "input(0) name: " << interpreter->GetInputName(0) << "\n";
//        cout << "outputs: " << interpreter->outputs().size() << "\n";

    interpreter->Invoke();      // run your model


    const float* detection_locations = interpreter->tensor(interpreter->outputs()[0])->data.f;
    const float* detection_classes=interpreter->tensor(interpreter->outputs()[1])->data.f;
    const float* detection_scores = interpreter->tensor(interpreter->outputs()[2])->data.f;
    const int    num_detections = *interpreter->tensor(interpreter->outputs()[3])->data.f;

    Tend = chrono::steady_clock::now();
    f = chrono::duration_cast <chrono::milliseconds> (Tend - Tbegin).count();
    //there are ALWAYS 10 detections no matter how many objects are detectable
    //cout << "number of detections: " << num_detections << "\n";

    const float confidence_threshold = 0.5;
    for(int i = 0; i < num_detections; i++){
        if(detection_scores[i] > confidence_threshold){
            int  det_index = (int)detection_classes[i]+1;
            float y1=detection_locations[4*i  ]*cam_height;
            float x1=detection_locations[4*i+1]*cam_width;
            float y2=detection_locations[4*i+2]*cam_height;
            float x2=detection_locations[4*i+3]*cam_width;

            Rect rec((int)x1, (int)y1, (int)(x2 - x1), (int)(y2 - y1));
            rectangle(src,rec, Scalar(0, 0, 255), 1, 8, 0);
            putText(src, format("%s", Labels[det_index].c_str()), Point(x1, y1-5) ,FONT_HERSHEY_SIMPLEX,0.5, Scalar(0, 0, 255), 1, 8, 0);
        }
    }

    return f;
}

float mean_array(vector<float> v){
    int n = v.size();
    float mean = 0;
    for (int i=0; i<n; i++) {
        //cout<< v[i]<<endl;
         mean += v[i]/ n;
    }

    return mean;

}

int main(int argc,char ** argv)
{
    float FPS[16];
    int i;
    int Fcnt=0;
    Mat frame;
    float f;
    float run_time;

    chrono::steady_clock::time_point Tbegin, Tend;

    for(i=0;i<16;i++) FPS[i]=0.0;

    // Load model
    std::unique_ptr<tflite::FlatBufferModel> model = tflite::FlatBufferModel::BuildFromFile("model.tflite");

    // Build the interpreter
    tflite::ops::builtin::BuiltinOpResolver resolver;
    tflite::InterpreterBuilder(*model.get(), resolver)(&interpreter);

    interpreter->AllocateTensors();

	// Get the names
	bool result = getFileContent("COCO_labels.txt");
	if(!result)
	{
        cout << "loading labels failed";
        exit(-1);
	}
    /*
    VideoCapture cap("James.mp4");
    if (!cap.isOpened()) {
        cerr << "ERROR: Unable to open the camera" << endl;
        return 0;
    }

    cout << "Start grabbing, press ESC on Live window to terminate" << endl;

    while(1){
//        frame=imread("Traffic.jpg");  //need to refresh frame before dnn class detection
        cap >> frame;
    */
    vector<cv::String> fn;
	glob("/home/pi/tflite_perf_tests/tflite-perf-tests/object_detection/sample_images/*.jpg", fn, false);
	size_t count=fn.size();
	vector<float> fps_array;
	bool break_flag=false;

	float start_time=20000, end_time=40000;
	int waitkey;

	cout<<"Enter starting millisecond: ";
	cin>>start_time;
	cout<<"Enter ending millisecond: ";
	cin>>end_time;
	cout<<"enter waitkey: ";
	cin>>waitkey;

	Tbegin = chrono::steady_clock::now();
    for(int num=0; num<10000;num++){
    if(break_flag==true){break;}
    for(size_t k=0; k<count; k++){

        Tend = chrono::steady_clock::now();
        run_time = chrono::duration_cast <chrono::milliseconds> (Tend - Tbegin).count();
        if (run_time>end_time){
            cout<<"FPS : "<<mean_array(fps_array)<<endl;
            break_flag=true;
            break;}


        frame=imread(fn[k]);
        f=detect_from_video(frame);

        FPS[((Fcnt++)&0x0F)]=1000.0/f;
        for(f=0.0, i=0;i<16;i++){ f+=FPS[i]; }

        if (run_time>start_time){
        fps_array.push_back(f/16);
        }

        putText(frame, format("FPS %0.2f",f/16),Point(10,20),FONT_HERSHEY_SIMPLEX,0.6, Scalar(0, 0, 255));

        //show output
        imshow("RPi 4 - 2.0 GHz - 2 Mb RAM", frame);

        char esc = waitKey(waitkey);
        //char esc = waitKey(-1);
        if(esc == 27) break;
    }}

    cout << "Closing the camera" << endl;

    // When everything done, release the video capture and write object
    //cap.release();

    destroyAllWindows();
    cout << "Bye!" << endl;

    return 0;
}
