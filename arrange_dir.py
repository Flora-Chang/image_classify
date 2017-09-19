import pandas as pd 
import csv
import os
import sys
import json
import shutil

image_root ="../data/scene_validation_images_20170908/"
new_image_root = 'little_val_images/'

data = pd.read_csv(os.path.join(image_root, "scene_classes.csv"))
names = data['chinese']

if not os.path.exists(new_image_root):
	os.mkdir(new_image_root)
for i, name in enumerate(names):
	os.mkdir(os.path.join(image_root, new_image_root, str(i) + "_" + "_".join(name.split("/")[0].split())))
count = 0
with open(os.path.join(image_root, "scene_validation_annotations_20170908.json")) as json_file:
	for line in json_file:
		items = json.loads(line)

		for item in items:
			name = item['image_id']
			label = int(item["label_id"])
			shutil.copy(os.path.join(image_root, name), os.path.join(new_image_root, str(label) + "_" + "_".join(names[label].split("/")[0].split())) + '/')
			count += 1
			if count >= 1000:
				break

