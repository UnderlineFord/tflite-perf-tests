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
#include <string>


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

float detect_from_video(Mat &src ,vector<vector<float>>& out_array, float image_id)
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

    const float confidence_threshold = 0.5;vector<float> fps_array;
    for(int i = 0; i < num_detections; i++){
        if(detection_scores[i] > confidence_threshold){
            int  det_index = (int)detection_classes[i]+1;
            float y1=detection_locations[4*i  ]*cam_height;
            float x1=detection_locations[4*i+1]*cam_width;
            float y2=detection_locations[4*i+2]*cam_height;
            float x2=detection_locations[4*i+3]*cam_width;

            out_array.push_back({image_id, (float)detection_classes[i],detection_scores[i],y1, x1, y2, x2});

            //Rect rec((int)x1, (int)y1, (int)(x2 - x1), (int)(y2 - y1));
            //rectangle(src,rec, Scalar(0, 0, 255), 1, 8, 0);
            //putText(src, format("%s", Labels[det_index].c_str()), Point(x1, y1-5) ,FONT_HERSHEY_SIMPLEX,0.5, Scalar(0, 0, 255), 1, 8, 0);
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
    vector<vector<float>> out_array={};

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

    vector<cv::String> fn;
	//glob("/home/pi/tflite_perf_tests/tflite-perf-tests/object_detection/datasets/coco2017_val/check_images/*.jpg", fn, false);
	glob("/home/pi/tflite_perf_tests/tflite-perf-tests/object_detection/datasets/coco2017_val/images/*.jpg", fn, false);

	size_t count=fn.size();
	vector<float> fps_array;


    for(size_t k=0; k<count; k++){
        if(k%100==0){cout<<k<<"/"<<count<<endl;}
        frame=imread(fn[k]);
        string file_name=(string)fn[k];
        string img_name=file_name.substr(file_name.size()-16, 12);
        //cout<<img_name<<endl;
        float image_id= stof(img_name);
        //cout<<file_name.substr(file_name.size()-20,100) << "\n" << image_id <<"\n"<<endl;

        f=detect_from_video(frame, out_array, image_id);

        FPS[((Fcnt++)&0x0F)]=f/1000.0;
        for(f=0.0, i=0;i<16;i++){ f+=FPS[i]; }

        fps_array.push_back(1/(f/16));

        //putText(frame, format("FPS %0.2f",f/16),Point(10,20),FONT_HERSHEY_SIMPLEX,0.6, Scalar(0, 0, 255));
        //imshow("RPi 4 - 2.0 GHz - 2 Mb RAM", frame);
        //char esc = waitKey(1);
        //if(esc == 27) break;
    }

    //cout << "Closing the camera" << endl;
    //cap.release();
    //destroyAllWindows();
    //cout << "Bye!" << endl;

    cout<<"FPS : "<<mean_array(fps_array)<<endl;

    ofstream outputfile("results.txt");
    for(int p=0;p<out_array.size();p++){
        for(int q=0;q<out_array[p].size();q++){
            outputfile<<out_array[p][q]<<" ";}
            outputfile<<"\n";

        }

    return 0;
}
