import os


def find_files(suffix, path):
  """
  Find all files beneath path with file name suffix.

  Note that a path may contain further subdirectories
  and those subdirectories may also contain further subdirectories.

  There are no limit to the depth of the subdirectories can be.

  Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system

  Returns:
     a list of paths
  """

  lists_paths = list()
  current_list = os.listdir(path)

  for item in current_list:

    if os.path.isdir(os.path.join(path, item)):
      paths = find_files(suffix, os.path.join(path, item))
      lists_paths += paths
    
    if os.path.isfile(os.path.join(path, item)):
      if item.endswith(".c"):
        lists_paths.append(os.path.join(path, item))

  return lists_paths



a = find_files(".c", "/mnt/homefiles/reivax/Temporal/testdir")
for i in a:
  print(i)