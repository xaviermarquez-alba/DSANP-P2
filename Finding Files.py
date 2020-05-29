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
  if suffix is None or path is None:
    print('A path and suffix needs to be specified')
    return []

  lists_paths = list()
  current_list = os.listdir(path)

  for item in current_list:

    if os.path.isdir(os.path.join(path, item)):
      paths = find_files(suffix, os.path.join(path, item))
      lists_paths += paths
    
    if os.path.isfile(os.path.join(path, item)):
      if item.endswith(suffix):
        lists_paths.append(os.path.join(path, item))

  return lists_paths

def list_files(list_items):
  for item in list_items:
    print(item)

# Test suffix ".h" on test dir

def test_1():
  result = find_files(".h", "./testdir")
  expected_result = ["./testdir/subdir1/a.h","./testdir/subdir3/subsubdir1/b.h","./testdir/t1.h","./testdir/subdir5/a.h"]
  assert result == expected_result, 'Fail Test'
  print('Test 1 Pass!')

# Test suffix ".xyz" on test dir, expected output must be []

def test_2():
  result = find_files(".xyz", "./testdir")
  expected_result = []
  assert result == expected_result, 'Fail Test'
  print('Test 2 Pass!')

# Test suffix "3", there is a folder subdir3 but the result only search files, expected output []

def test_3():
  result = find_files("3", "./testdir")
  expected_result = []
  assert result == expected_result, 'Fail Test'
  print('Test 3 Pass!')

# Test None args
def test_4():
  result_no_suffix = find_files(None, "./testdir")
  result_no_path = find_files('.h', None)
  
  assert result_no_path == [], 'Fail Test'
  assert result_no_suffix == [], 'Fail Test'
  print('Test 4 Pass!')

# Tests
test_1()
test_2()
test_3()
test_4()