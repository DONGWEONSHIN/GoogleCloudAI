from xml_to_yolo import load_xml_annotations, to_yolov8

import os

def write_yolov8_txt(folder, annotation):
  #print(annotation[0][:-3])
  out_filename = os.path.join(folder,str(annotation[0][:-3]))
  out_filename = os.path.splitext(out_filename)[0]
  out_filename = out_filename+'.txt'

  f = open(out_filename,"w+")
  for box in annotation[3]:
    f.write("{} {} {} {} {}\n".format(box[0], box[1], box[2], box[3], box[4]))


#dataPath='C:/Users/park0/highway/labels/'
dataPath='C:/Users/SBA/my_ws/GoogleCloudAI/edu/yolov8/bbox_highway'

# 파일명을 설정한다.
#xmlFile='Suwon_CH01_20200720_1700_MON_9m_NH_highway_TW5_sunny_FHD.xml'
xmlFile='Suwon_CH02_20200722_1600_WED_9m_RH_highway_TW5_rainy_FHD.xml'
# 현재 경로 + 파일명
label_file = os.path.join(dataPath, xmlFile)

# XML을 TXT로 변환한다.
anns = load_xml_annotations(label_file)
print(anns)

folderName=os.path.splitext(xmlFile)[0]
os.makedirs(os.path.join(dataPath,folderName), exist_ok=True)


# # 이미지 파일별로 TXT파일을 저장한다.
for ann in anns:
  write_yolov8_txt(dataPath+folderName, ann)



