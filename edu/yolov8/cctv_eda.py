import numpy as np
import lxml
import os

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
   
  print("truck_cnt : ", truck_cnt)
  print("bus_cnt : ", bus_cnt)
  print("car_cnt : ", car_cnt)

  return np.array([car_type[0] , truck_cnt, car_type[1] , bus_cnt , car_type[2] , car_cnt])


def write_yolov8_txt(folder, annotation):
  #print(annotation[0][:-3])
  out_filename = os.path.join(folder,str(annotation[0][:-3]))
  out_filename = os.path.splitext(out_filename)[0]
  out_filename = out_filename+'.txt'

  f = open(out_filename,"w+")
  for box in annotation[3]:
    f.write("{} {} {} {} {}\n".format(box[0], box[1], box[2], box[3], box[4]))


dataPath='/home/shin/my_ws/GoogleCloudAI/edu/yolov8/highway/bbox_highway/'

# 파일명을 설정한다.
xmlFile='Suwon_CH02_20200722_1600_WED_9m_RH_highway_TW5_rainy_FHD.xml'

# 현재 경로 + 파일명
label_file = os.path.join(dataPath, xmlFile)

carType = get_car_type(label_file)
print(carType)

# # XML을 TXT로 변환한다.
# anns = load_xml_annotations(label_file)
# print(anns)

# folderName=os.path.splitext(xmlFile)[0]
# os.makedirs(os.path.join(dataPath,folderName), exist_ok=True)


# # # 이미지 파일별로 TXT파일을 저장한다.
# for ann in anns:
#   write_yolov8_txt(dataPath+folderName, ann)
  
  
