
from tflite_runtime.interpreter import Interpreter
import numpy as np
from PIL import Image


# below files should be there in the directory !!!
filename='dog.jpg'
model_path='models/mobilenet_v1/model.tflite'
label_path='models/mobilenet_v1/labelmap.txt'

with open(label_path, 'r') as f:
    labels=list(map(str.strip,f.readlines()))
    
    
interpreter=Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details=interpreter.get_input_details()
output_details=interpreter.get_output_details()

size=input_details[0]['shape'][1:3]


img=Image.open(filename).convert('RGB')
img=np.array(img.resize(size))
input_data=np.expand_dims(img, axis=0)


interpreter.set_tensor(input_details[0]['index'], input_data) # set the data to the model tensor given by index field
interpreter.invoke()
predictions=interpreter.get_tensor(output_details[0]['index'])[0] # get the output from the tensor given by "index" of output details


top_indices=np.argsort(predictions)[::-1][:3]
for i in range(3):
    print(labels[top_indices[i]])
predictions[top_indices[i]]/255.0
