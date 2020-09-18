"mllib":"caffe" // Caffe is a deep learning framework developed by Berkeley AI Research (BAIR) 

"mllib":{
  "nclasses": 1000,	      // Number of classes of images this model can recognize
  "template": "se_resnet_50"  // Use ResNet50 deep convolutional neural network model
}

"mllib":{ 
  "extract_layer": "pool5/7x7_s1"  // Use “pool5/7x7_s1” layer of ResNet50 model
				   //  (pooling layer, kernel size: 7, stride: 1)	
}
