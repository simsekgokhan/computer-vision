curl -X POST "http://hostname:8080/predict" -d '{
        "service": "simsearch",
        "parameters": {
          "input": { "height": 224, "width": 224 },
          "output": { "index": true  },
          "mllib": { "extract_layer": "pool5/7x7_s1", "gpu": false  }
        },
        "data": [ "/data/lamps/shelby-655-floor-lamp.jpg.jpg" ]
      }'