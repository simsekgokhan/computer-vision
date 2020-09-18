curl -X PUT "http://hostname:8080/services/simsearch" -d '{
      "mllib": "caffe",
      "description": "similarity search service",
      "type": "unsupervised",
      "parameters": {
        "input": {
          "connector": "image",
          "height": 224,
          "width": 224
        },
        "mllib": {
          "nclasses": 1000,
          "template": "se_resnet_50"
        }
      },
      "model": {
        "repository": "/opt/data/simsearch/",
        "templates": "/opt/deepdetect/templates/caffe/"
      }
    }'