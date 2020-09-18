curl -X POST "http://hostname:8080/predict" -d '{
        "service": "simsearch",
        "parameters": {
          "input": { "height": 224, "width": 224  },
          "output": { "search_nn": 10, "search": true },
          "mllib": { "extract_layer": "pool5/7x7_s1"  }
        },
        "data": ["https://www.ikea.com/ca/en/images/products/hektar-work-lamp..."]
      }'