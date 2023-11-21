import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
import lxml
import os
import glob

from lxml import etree

CLASSES = ["car", "bus", "truck"]

def to_yolov8(y):
  """
  # change to yolo v8 format
  # [x_top_left, y_top_left, x_bottom_right, y_bottom_right] to
  # [x_center, y_center, width, height]
  """
  width = y[2] - y[0]
  height = y[3] - y[1]

  if width < 0 or height < 0:
      print("ERROR: negative width or height ", width, height, y)
      raise AssertionError("Negative width or height")
  return (y[0] + (width/2)), (y[1] + (height/2)), width, height


def load_xml_annotations(f):
  tree = etree.parse(f)
  anns = []
  for dim in tree.xpath("image"):
    image_filename = dim.attrib["name"]
    width = int(dim.attrib["width"])
    height = int(dim.attrib["height"])
    # print(image_filename)
    # print(len(dim.xpath("box")))
    boxes = []
    for box in dim.xpath("box"):
      label = CLASSES.index(box.attrib["label"])
      xtl, ytl = box.attrib["xtl"], box.attrib["ytl"]
      xbr, ybr = box.attrib["xbr"], box.attrib["ybr"]

      xc, yc, w, h = to_yolov8([float(xtl), float(ytl), float(xbr), float(ybr)])
      boxes.append([label, round(xc/width, 5), round(yc/height, 5), round(w/width, 5), round(h/height, 5)])

    anns.append([image_filename, width, height, boxes])

  return np.array(anns)


def write_yolov8_txt(folder, annotation):
  #print(annotation[0][:-3])
  out_filename = os.path.join(folder,str(annotation[0][:-3]))
  out_filename = os.path.splitext(out_filename)[0]
  out_filename = out_filename+'.txt'

  f = open(out_filename,"w+")
  for box in annotation[3]:
    f.write("{} {} {} {} {}\n".format(box[0], box[1], box[2], box[3], box[4]))

# get car type
def get_car_type(f):
  tree = etree.parse(f)
  car_type = []
  for meta_tag in tree.xpath("meta"):
    for task_tag in meta_tag.xpath("task"):
      for lables_tag in task_tag.xpath("labels"):
        for lable_tag in lables_tag.xpath("label"):
          for name_tag in lable_tag.xpath("name"):            
            car_type.append(name_tag.text)
  result = []
  truck_cnt = 0
  bus_cnt = 0
  car_cnt = 0
  for dim in tree.xpath("image"):
    for box in dim.xpath("box"):
      cars = box.attrib["label"]
      if cars == car_type[0]:
        truck_cnt = truck_cnt + 1
      elif cars == car_type[1]:
        bus_cnt = bus_cnt + 11
      elif cars == car_type[2]:
        car_cnt = car_cnt + 1
   
#  print("truck_cnt : ", truck_cnt)
#  print("bus_cnt : ", bus_cnt)
#  print("car_cnt : ", car_cnt)

  return np.array([[car_type[0] , truck_cnt] , [car_type[1] , bus_cnt] , [car_type[2] , car_cnt]])


def get_total_car_count(val_file_list):
  val_file_name_list = []
  val_xml_name_list = []
  val_file_path_list = []
  val_xml_path_list = []

  for files in val_file_list:
    file_name = os.path.basename(files)
    if os.path.splitext(file_name)[1] == '.png':
      val_file_name_list.append(file_name)
      under_file_path = files
      under_file_path = under_file_path.replace(".\\", "/").replace("\\", "/")
      path_list = val_base_dir + under_file_path
      val_file_path_list.append(path_list)
    elif os.path.splitext(file_name)[1] == '.xml':
      val_xml_name_list.append(file_name)
      under_file_path = files
      under_file_path = under_file_path.replace(".\\", "/").replace("\\", "/")
      path_list = val_base_dir + under_file_path
      val_xml_path_list.append(path_list)
      
  return np.array([val_xml_path_list])



val_base_dir = 'C:/ftp_base/datasets/Validation/바운딩박스'
os.chdir(val_base_dir)
os.getcwd()

# Validation의 하위폴더에서 모든 파일을 리스트로 만들기
val_file_list = glob.glob('./**', recursive=True)
val_file_name = [os.path.basename(x) for x  in val_file_list]


val_file_name_list = []
val_xml_name_list = []
for filename in val_file_name:
    if os.path.splitext(filename)[1] == '.png':
        val_file_name_list.append(filename)
    elif os.path.splitext(filename)[1] == '.xml':
        val_xml_name_list.append(filename)

        
print("png file cnt : ", len(val_file_name_list))
print("xml file cnt : ", len(val_xml_name_list))




val_file_name_list2 = []
val_xml_name_list2 = []

val_file_path_list = []
val_xml_path_list = []

for file in val_file_list:
  filename = os.path.basename(file)
  if os.path.splitext(filename)[1] == '.png':
    val_file_name_list2.append(filename)
    under_file_path = file
    under_file_path = under_file_path.replace(".\\", "/").replace("\\", "/")
    path_list = val_base_dir + under_file_path
    val_file_path_list.append(path_list)
  elif os.path.splitext(filename)[1] == '.xml':
    val_xml_name_list2.append(filename)
    under_file_path = file
    under_file_path = under_file_path.replace(".\\", "/").replace("\\", "/")
    path_list = val_base_dir + under_file_path
    val_xml_path_list.append(path_list)

#for label_file in val_xml_path_list:
#  carType = get_car_type(label_file)
#  print(carType)

# 각 폴더의 차, 트럭, 버스의 수를 반환
total_truck = 0
total_bus = 0
total_car = 0
for label_file in val_xml_path_list:
  carType1, carType2, carType3 = get_car_type(label_file)
  total_truck = total_truck + int(carType1[1])
  total_bus = total_bus + int(carType2[1])
  total_car = total_car + int(carType3[1])

print("Validation 안의 차량 수")
print("total_truck :", total_truck)
print("total_bus :", total_bus)
print("total_car :", total_car)

type1 = get_total_car_count(val_file_list)

type1

total_truck2 = 0
total_bus2 = 0
total_car2 = 0
for label_file in type1[0]:
  carType1, carType2, carType3 = get_car_type(label_file)
  total_truck2 = total_truck2 + int(carType1[1])
  total_bus2 = total_bus2 + int(carType2[1])
  total_car2 = total_car2 + int(carType3[1])
  
  
print("Validation 안의 차량 수2")
print("total_truck2 :", total_truck2)
print("total_bus2 :", total_bus2)
print("total_car2 :", total_car2)
  

print("test")

######################################

for label_file in val_xml_path_list:
  anns = load_xml_annotations(label_file)
  print(anns)
  label_files = os.path.split(label_file)
  dataPath = label_files[0]
  xmlFile = label_files[1]
  folderName=os.path.splitext(xmlFile)[0]
  os.makedirs(os.path.join(label_files[0],folderName), exist_ok=True)
  for ann in anns:
    write_yolov8_txt(dataPath+folderName, ann)










######################################






## 위쪽에서 셀을 실행 안했을 경우를 대비 다시 한번 불러 온다.
train_base_dir = 'C:/ftp_base/datasets/Training/바운딩박스'
os.chdir(train_base_dir)
os.getcwd()
# Training의 하위폴더에서 모든 파일을 리스트로 만들기
train_file_list = glob.glob('./**', recursive=True)


train_file_name_list2 = []
train_xml_name_list2 = []

train_file_path_list = []
train_xml_path_list = []

for file in train_file_list:
  filename = os.path.basename(file)
  if os.path.splitext(filename)[1] == '.png':
    train_file_name_list2.append(filename)
    under_file_path = file
    under_file_path = under_file_path.replace(".\\", "/").replace("\\", "/")
    path_list = train_base_dir + under_file_path
    train_file_path_list.append(path_list)
  elif os.path.splitext(filename)[1] == '.xml':
    train_xml_name_list2.append(filename)
    under_file_path = file
    under_file_path = under_file_path.replace(".\\", "/").replace("\\", "/")
    path_list = train_base_dir + under_file_path
    train_xml_path_list.append(path_list)

#for label_file in val_xml_path_list:
#  carType = get_car_type(label_file)
#  print(carType)

# 각 폴더의 차, 트럭, 버스의 수를 반환
total_truck2 = 0
total_bus2 = 0
total_car2 = 0
for label_file in train_xml_path_list:
  carType1, carType2, carType3 = get_car_type(label_file)
  total_truck2 = total_truck2 + int(carType1[1])
  total_bus2 = total_bus2 + int(carType2[1])
  total_car2 = total_car2 + int(carType3[1])

print("train 안의 차량 수")
print("total_truck2 :", total_truck2)
print("total_bus2 :", total_bus2)
print("total_car2 :", total_car2)

# type2 = get_total_car_count(train_file_list)

# total_truck2 = 0
# total_bus2 = 0
# total_car2 = 0
# for label_file in type2[0]:
#   carType1, carType2, carType3 = get_car_type(label_file)
#   total_truck2 = total_truck2 + int(carType1[1])
#   total_bus2 = total_bus2 + int(carType2[1])
#   total_car2 = total_car2 + int(carType3[1])
  
  
# print("train 안의 차량 수2")
# print("total_truck2 :", total_truck2)
# print("total_bus2 :", total_bus2)
# print("total_car2 :", total_car2)