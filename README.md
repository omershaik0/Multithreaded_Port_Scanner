# Multi-Threaded Port Scanning Tool

This project is a multi-threaded port scanning tool written in Python. It scans a target IP/Domain for open ports using multiple threads to speed up the process.

## Features

- Multi-threaded port scanning for faster results.
- Accepts single ports, lists of ports, or port ranges.
- Validates and resolves target IP addresses.
- Provides colored terminal output for better readability.

## Requirements

- Python 3.x
- `colorama` library

## Installation

First, clone the repository and navigate into its directory:

```sh
git clone https://github.com/omershaik0/Multithreaded_Port_Scanner.git
cd Multithreaded_Port_Scanner
```

Install the required dependencies using `pip`:

```sh
pip install colorama
```

## Usage

Run the script with the required arguments:

```sh
python3 multi_threaded_port_scanner.py -l <Target IP/Domain> -p <Target Port(s)> -t <Number of Threads>
```

### Arguments

- `-l`, `--target`: Enter the Target IP/Domain to scan Ports (required).
- `-p`, `--port`: Enter the Target Port(s) e.g., `21`, `22,23,21`, or `1-65535` (required).
- `-t`, `--threads`: Enter the number of Threads (optional, default is 10 threads).

### Example

Scan the target `192.168.1.1` for ports `21`, `22`, and `80` using 20 threads:

```sh
python3 multi_threaded_port_scanner.py -l 192.168.1.1 -p 21,22,80 -t 20
```

## Output

The script provides colored terminal output indicating open ports:

```
PORT    STATE
21      OPEN
22      OPEN
80      OPEN
```

## Script Flowchart
![Alt Text](https://github.com/omershaik0/Multithreaded_Port_Scanner/blob/main/multithreaded_portscanner_flowchart.png)

## In Action
![Alt Text](https://github.com/omershaik0/Multithreaded_Port_Scanner/blob/main/multi_threaded_port_scanner.gif)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request.

## Disclaimer
* Use ethically :)
