# Gig Management & Music Automation Toolkit

A Python automation tool built to manage sheet music libraries, dynamically generate instrument setlist charts, and compile itemised PDF invoices for live performance events.

## Description

This project consists of:  

* **PDF Sheet Music Auto-Sorter ("organiser_example.py"):** Scans unsorted folder structures, parses filenames against target song keywords and instrument patterns, and routes charts into categorized database folders.
*  **Setlist Booklet Compiler ("setlists_example.py"):** Reads active setlists and automatically merges individual PDF charts into consolidated gig booklets for specific instruments using `PyPDF2`.  
*  **Automated PDF Invoicing ("invoices_example.py"):** Calculates totals, itemized deductions, deposit adjustments, and travel costs to render branded PDF invoices using `ReportLab`.

## Tech Stack
* **Python 3**
* **PyPDF2**
* **ReportLab**

## Setup & Usage

1. Clone this repository to your local machine.
2. Install required packages:
   ```bash
   pip install PyPDF2 reportlab

## Programs Walkthrough

### **PDF Sheet Music Auto-Sorter ("organiser_example.py")**
Our music is stored on a Google drive in folders according to the different pieces. When I download this directory it looks like this:  

<img width="1271" height="899" alt="Capture d’écran 2026-08-20 à 12 58 06" src="https://github.com/user-attachments/assets/54635e7f-7352-499b-ad12-675c3684895c" />  

and within each folder, the individual PDF files are named according to the instrument, like this:  

<img width="251" height="271" alt="Capture d’écran 2026-08-20 à 12 58 21" src="https://github.com/user-attachments/assets/6204035e-8dcd-472b-8091-6ec80f523d2a" />  

I want to sort these files into folders for each musician, to make it convenient for practice and rehearsals. These are the individual musician folders:  

<img width="284" height="294" alt="Capture d’écran 2026-08-20 à 12 59 10" src="https://github.com/user-attachments/assets/e69814bb-46e9-49bc-826b-cd48315c3fe0" />

We do this by identifying keyword expressions that will uniquely identify every piece while allowing for variations in the original naming conventions. The dictionary of keywords is found in **"keywords.JSON"**. Similarly, we identify keywords for each musician where necessary (e.g. "piano" and "key" both represent "keys"). Finally, move and rename each piece into the appropriate folder, with a naming convention optimal for **""setlists_example.py""**

