
import os
import shutil

# Specify source directory
source_dir = r""

# Specify destination directory
destination_dir = r""

# List for sub directory names within destination 
sub_directories = []

# Funtion to check if a file name contains a sub directory name
def get_location(file_name):
  result = ""
  for directory_name in sub_directories:
    if directory_name in file_name:
      result = directory_name
      break

  return result

# Iterate through the destination to find the sub directories
for filename in os.listdir(destination_dir):
  f = os.path.join(destination_dir, filename)

  # If a directory is found, store the name
  if os.path.isdir(f):
    sub_directories.append(filename)

# Iterate through the source directory and transfer based on the file name
for filename in os.listdir(source_dir):
  f = os.path.join(source_dir, filename)
  transfer_location = get_location(filename)
  if transfer_location:
    new_location = os.path.join(destination_dir, transfer_location)
    print('Matching subdirectory found, transfering to:', new_location)
    try:
      shutil.move(f, new_location)
    except RuntimeError as err:
      print('Unable to move file, error:', err)

  else:
    print('Skipping, unable to find a matching subdirectory for:', filename)
