import os
import shutil
from pathlib import Path
import json


keywords_path = Path(__file__).parent / "keywords.json"  # assumes json is in the same directory
with open(keywords_path, "r") as f:
    pieces_keywords = json.load(f)

charts=os.path.join(Path.home(),"Charts")
unsorted=os.path.join(charts,"unsorted")
database=os.path.join(charts,"Database")

for (root,dirs,files) in os.walk(unsorted,topdown=True):
    for file in files:

      if not file.endswith(".pdf"):
          print(f"{file} in {root} is not a PDF")
          continue

      matches = []
      file_low = file.lower()
      # "as":"as", had to move bc just as is everywhere (e.g. b*as*s_guitar)
      if file_low.startswith('as '):
          matches.append('as')

      file_lower="".join(file_low.split())

      for piece_name, keyword in pieces_keywords.items():
          if keyword in file_lower:
              matches.append(piece_name)

      if len(matches) == 0:
          print(f"no matches for {file} in {root}")
      elif len(matches) > 1:
          print(f"multiple matches for {file} in {root}")
      elif len(matches) == 1:
          instruments=[]
          if "alto" in file_lower:
              instruments.append("alto")
          if "tenor" in file_lower:
              instruments.append("tenor")
          if "bone" in file_lower:
              instruments.append("trombone")
          if "trumpet" in file_lower:
              instruments.append("trumpet")
          if "guitar" in file_lower and not "bass" in file_lower:
              instruments.append("guitar")
          if "bass" in file_lower:
              instruments.append("bass")
          if "drum" in file_lower:
              instruments.append("drums")
          if any(k in file_lower for k in ["key", "piano"]):
              instruments.append("keys")
          if any(k in file_lower for k in ["voice", "vox", "vocal", "singer"]):
              instruments.append("vocals")

          if len(instruments) == 0:
              print(f"could not find instrument for {file} in {root}")
          elif len(instruments) > 1:
              print(f"multiple instruments for {file} in {root}")
          elif len(instruments) == 1:
              source_path= os.path.join(root, file)
              destination_path = os.path.join(database, instruments[0])
              final_name=f"{matches[0]}_{instruments[0]}.pdf"
              final_destination=os.path.join(destination_path, final_name)
              if os.path.exists(destination_path):
                  if os.path.exists(final_destination):
                      print(f"{final_name} already exists in {destination_path}")
                  else:
                    shutil.move(source_path, final_destination)
              else:
                  print(f"destination path {destination_path} does not exist")
