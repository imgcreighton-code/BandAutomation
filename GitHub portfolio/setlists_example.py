import PyPDF2
import sys
import os
from contextlib import chdir
from pathlib import Path

#CHANGE ME!!!
instruments=["drums", "tenor", "alto", "guitar", "bass", "trumpet", "trombone", "keys"]

pieces=[

        "superstition",
        "blameitonseptember",
        "mytype",
        "babyonemoretime",
        "respect",
        "lushlife",
        "sweetdreamsaretoxic",
        "yougotthelove",
        "proud(er)mary"

        # "lover"
        # "itsrainingmen",
        # "moveonup",
        #
        # "iwish",
        # "gimmegimmegimme",
        # "playthatfunkymusic",
        # "holdonimcoming",
        # "mytype",
        # "umbrella",
        #
        # "superstition",
        # "blameitonseptember",
        # "beggin",
        # "babyonemoretime",
        # "imeverywoman",
        # "sirduke",
        # "respect",
        # "naturalwoman",
        # "as",
        # "sweetdreamsaretoxic",
        # "copamericabana",
        # "yougotthelove",
        # "proud(er)mary"
        #
        # "badromance",
        # "grease",
        # "whereismyhusband",
        # "latenighttalking",
        #blameitonthehottogo,
        #"24kmagic",
]

gig="2026-08-01 Example Gig"


############################################################################################
############################################################################################

base_dir=os.path.join(Path.home(),"Charts")
database=os.path.join(base_dir,"Database")
base_path=os.path.join(base_dir,gig)
newpath=base_path

if os.path.exists(newpath):
    replace = input("Folder already exists, do you wish to continue? (Y/N): ")
    if replace == "N":
        print("Exiting...")
        sys.exit()
    elif replace == "Y":
        counter = 1
        while os.path.exists(newpath):
            newpath = f"{base_path}_+{counter}"
            counter += 1
    else:
        print("Invalid input. Terminating to prevent overwrites.")
        sys.exit()

os.makedirs(newpath)

for instrument in instruments:
    with chdir(os.path.join(database,instrument)):
        merger = PyPDF2.PdfMerger()

        for piece in pieces:
            file_name = f"{piece}_{instrument}.pdf"

            if os.path.exists(file_name):
                merger.append(file_name)
            else:
                print(f"Warning: Missing file {file_name} in {instrument} database.")

        with chdir(newpath):
            output_name = f"{gig} - {instrument}.pdf"
            merger.write(output_name)
            merger.close()
            print(f"Successfully created: {output_name}")



