from pathlib import Path

# absolute path
# c:/user/... for mac , c:\pro... for wins
# relative path

path = Path("email")
print(path.mkdir())  # make directory 
print(path.exists()) # check if directory exists
print(path.rmdir())  # remove directory


