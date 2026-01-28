# IBM TORCs 🏎️

This repository contains my submission for the **IBM Early Adopter AI Race League**, focused on developing and evaluating autonomous driving logic in **TORCS** using the TORCs environment and the provided F1-style car.

🏎 Current Best Lap Time: 1:59:49

Our blog can found in IBM TORCs blog.pdf!



## Main file overview

### `fastest.py`

The hall-of-fame file 🏆

* Contains **only the parameters** that currently produce the best lap time
* No experimentation here, this file is for proven winners only
* Used as a reference point when judging new ideas

---

### `experimental.py`

The mad science lab 🔬

* Where new driving ideas live
* Code here is constantly modified, tested, and sometimes abandoned
* If something works well, it graduates to `fastest.py`

This file targets the **new F1 car** provided by TORCS.

---

### `v1.py`

The legacy driver 🚗

* Contains the original driving code
* Built for the **old car**, not the new F1 car
* Mostly kept for comparisions

---

### `startup.py`

The ignition key 🔑

* Starts TORCS
* Launches a new race
* Runs the driving script (usually `experimental.py`)

This is the entry point when you want to go from zero to racing as fast as possible.

---

### `recordings.csv`

The memory bank 📊

* Stores logged lap time data
* Used to track performance across runs
* Makes it easy to see whether an idea actually helped or just *felt* faster

---

### `logger.py`

The pit engineer 🧠

* Defines the logger class used to interact with `recordings.csv`
* Handles:

  * Logging new lap data
  * Retrieving and organizing previous results

Keeps performance tracking tidy so the rest of the code can stay focused on driving.

---

## Typical workflow

(Ensure that TORCs is installed first before any of this)

1. Start TORCS using `startup.py` - make sure to update the file paths!
2. Hack on ideas in `experimental.py`
3. Log lap times to `recordings.csv`
4. Promote the best parameters to `fastest.py`
5. Repeat until victory or exhaustion

---

## Context

This project was developed as part of the **IBM Early Adopter AI Race League**. The primary objective is to explore autonomous driving strategies, evaluate their impact on lap time performance, and refine the driving logic for competitive racing in TORCS.

---





