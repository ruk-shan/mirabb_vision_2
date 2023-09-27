import yaml
import time

#write on a file
# pose_to_write = {'time_stamp': ['time_now'], 'pose': [0.001, 0.002, 0.003, 0.004, 0.005, 0.006]}
# with open(r'test_dev_apps/dected_pose.yaml', 'w') as file:
#     documents = yaml.dump(pose_to_write, file)

# #read from a file 
# with open(r'test_dev_apps/dected_pose.yaml') as file:
#     vision_pose = yaml.load(file, Loader=yaml.FullLoader)
#     print (vision_pose)

#     pose = vision_pose['pose']
#     print (pose)

def write_to_file(msg_from_abb):
    print("writing to yaml file")
    ts = time.time()# getting timestamp
    msg_to_write = {'time_stamp': [ts], 'abb_msg': [msg_from_abb]}
    with open(r'test_dev_apps/msg_from_abb.yaml', 'w') as file:
        documents = yaml.dump(msg_to_write, file)
    file.close()

write_to_file("hello from abb")