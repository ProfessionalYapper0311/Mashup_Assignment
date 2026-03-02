# Mashup Generator

## Project Overview
[cite_start]This project implements a "Mashup" generator that downloads songs of a specified singer from YouTube, cuts them, and merges them into a single audio file[cite: 12, 17]. [cite_start]It includes both a **Command Line Interface (CLI)** and a **Web Interface**[cite: 6, 29].

## Features
1. [cite_start]**Download**: Automatically searches and downloads **N** videos of a singer ($N > 10$)[cite: 18].
2. [cite_start]**Convert**: Extracts audio (MP3) from videos using `pypi.org` libraries[cite: 20].
3. [cite_start]**Cut**: Trims the first **Y** seconds of each audio ($Y > 20$)[cite: 21].
4. [cite_start]**Merge**: Joins all parts into a single output file[cite: 22].
5. [cite_start]**Email**: (Web Service) Zips the result and emails it to the user's correct email ID[cite: 39, 40].

> **Note**: Since I used **Streamlit** to develop the web service, a separate `index.html` file was not required as the interface is rendered natively through Python.

---

## Program 1: Command Line Usage
[cite_start]**File**: `102317201.py` [cite: 15]

### How to Run
[cite_start]The program requires four parameters: Singer Name, Number of Videos, Audio Duration, and Output File Name[cite: 24].

```bash
python 102317201.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>
