# # import os
import os
import shutil

# Define the source directory where the files are located
source_directory = '2020'
# Define the destination directories
sim_directory = source_directory+'/sim'
src_directory = source_directory+'/src'
script_directory = source_directory+'/script'
doc_directory = source_directory+'/docs'

os.system('mkdir {}'.format(src_directory))
os.system('mkdir {}'.format(sim_directory))
os.system('mkdir {}'.format(script_directory))
os.system('mkdir {}'.format(doc_directory))
# os.system('mkdir {}'.format(include_directory))

# print(os.listdir(source_directory))
# Iterate over all files in the source directory

width = 30
for filename in os.listdir(source_directory):
    source_path = os.path.join(source_directory, filename)
    
    # Check if the file name contains '*tb*'
    if 'tb' in filename:
        # Move to the simulation directory
        destination_path = os.path.join(sim_directory, filename)
        shutil.move(source_path, destination_path)
        # print("{}==========>{}".format(source_path,destination_path))
        print(source_path.ljust(width),"==========>",destination_path.ljust(width))
        # print("==========>",)
    
    elif filename.endswith('.v'):
        # Move .v files to the src directory
        destination_path = os.path.join(src_directory, filename)
        shutil.move(source_path, destination_path)
        # print("{}==========>{}".format(source_path,destination_path))
        print(source_path.ljust(width),"==========>",destination_path.ljust(width))
    
    elif filename.endswith('.tcl') or filename.endswith('.setup') or filename.endswith('.sdc'):
        # Move .tcl and .setup files to the script directory
        destination_path = os.path.join(script_directory, filename)
        shutil.move(source_path, destination_path)
        # print("{}==========>{}".format(source_path,destination_path))
        print(source_path.ljust(width),"==========>",destination_path.ljust(width))

    elif 'report' in filename or filename.endswith('.txt') :
        # Move .tcl and .setup files to the script directory
        destination_path = os.path.join(doc_directory, filename)
        shutil.move(source_path, destination_path)
        # print("{}==========>{}".format(source_path,destination_path))
        print(source_path.ljust(width),"==========>",destination_path.ljust(width))

print("Files has been rearranged")
