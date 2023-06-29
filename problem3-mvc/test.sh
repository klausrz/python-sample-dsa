#!/bin/bash
curl http://192.168.1.120:3001/store \
	-H 'Content-Type: application/json' \
	-X "POST" \
	-d '{ "manufacturer_id": 1, "model_id": 1, "imei": "537213228105947", "memory": 512, "manufacture_year": 2022, "os_version": "12.1.5", "body_color": "black", "price": 2000 }' \
	-v 
	
	
