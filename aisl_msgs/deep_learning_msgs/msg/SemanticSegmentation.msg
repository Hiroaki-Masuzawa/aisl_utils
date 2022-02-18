#Semantic Segmentation
#---------------------------------------------------

std_msgs/Header header
# String class IDs for each bouding box
string[] class_names

# Segmentation Image
sensor_msgs/Image segmentation_image #indexのみ
sensor_msgs/Image[] score_image #各クラスごとのSoftmax値