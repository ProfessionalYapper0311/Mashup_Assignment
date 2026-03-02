# Mashup Generator

## Project Overview
[cite_start]This project implements a "Mashup" generator that downloads songs of a specified singer from YouTube, cuts them, and merges them into a single audio file[cite: 12, 17]. [cite_start]It includes both a **Command Line Interface (CLI)** and a **Web Interface**[cite: 6, 29].

## Features
1. **Download**: Automatically searches and downloads **N** videos of a singer ($N > 10$)[cite: 18].
2. **Convert**: Extracts audio (MP3) from videos using `pypi.org` libraries[cite: 20].
3. **Cut**: Trims the first **Y** seconds of each audio ($Y > 20$)[cite: 21].
4. **Merge**: Joins all parts into a single output file[cite: 22].
5. **Email**: (Web Service) Zips the result and emails it to the user's correct email ID[cite: 39, 40].

> **Note**: Since I used **Streamlit** to develop the web service, a separate `index.html` file was not required as the interface is rendered natively through Python.
**Further updates will be made, this is an incremental/ongoing project and not representative of the final work**
---

## Program 1: Command Line Usage
**File**: `102317201.py` [cite: 15]

### How to Run
The program requires four parameters: Singer Name, Number of Videos, Audio Duration, and Output File Name[cite: 24].

```bash
python 102317201.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>

