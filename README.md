# Band Automation



# Gig Management & Music Automation Toolkit

A Python automation tool built to manage sheet music libraries, dynamically generate instrument setlist charts, and compile itemised PDF invoices for live performance events.

## Description

This project consists of:  

* **PDF Sheet Music Auto-Sorter ("organiser_example.py"):** Scans unsorted folder structures, parses filenames against target song keywords and instrument patterns, and routes charts into categorized database folders.
*  **Setlist Booklet Compiler ("setlists_example.py"):** Reads active setlists and automatically merges individual PDF charts into consolidated gig booklets for specific instruments using `PyPDF2`.  
*  **Automated PDF Invoicing ("invoices_example.py"):** Calculates totals, itemized deductions, deposit adjustments, and travel costs to render branded PDF invoices using `ReportLab`.

## 🛠️ Tech Stack
* **Python 3**
* **PyPDF2**
* **ReportLab**

## 📥 Setup & Usage

1. Clone this repository to your local machine.
2. Install required packages:
   ```bash
   pip install PyPDF2 reportlab
