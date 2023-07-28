
import time
import os
path = "./log"
index_api = ["eeprom_read_string", "get_calibration_mode", "set_calibration_mode", "load_calibration", "calibrate", 
             "read_nvmem", "read_nvmem_size", "write_calibration_cell", "read_calibration_cell","read_user_area", 
             "write_user_area", "write_module_calibration", "read_calibration_item", "get_ranges_name"]
def find_api(file_path):
    print("file_path = ", file_path)
    with open(file_path, 'r') as fp:
        a = fp.read()
        message = str(a)
    fp.close()
    for api in index_api:
        if api in message:
            print("api = ", api)
        else:
            continue

def find_log(path):
    for root, dirs, files in os.walk(path):
        return root, files

root, files = find_log(path)
for file in files:
    # print(root+'/'+file)
    find_api(root + '/' + file)
