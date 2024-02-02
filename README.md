
# Super Parser

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

A simple JSON file sniffer that reads all .json files from a **source** folder, parses the "message" key inside files and dumps the parsed schema in a **destination** folder.


## Prerequisites

You need to have Python 3.xx installed in order to run this program

## Installation

```bash
# Clone the repository
git clone https://github.com/coderboy-exe/Data2Bots.git

# Navigate to the project directory
cd Data2Bots
```

## Usage

Call the **main** program with your **source** and **destination** folder arguments repectively
```bash
# Call the main program with your src and dest folders
./main.py data schema
# OR
python main.py data schema
```

Passing a wrong number of arguments prints this in the console:
```bash
- -----Please input a source and destination directory-----
Usage: ./main.py src_folder dest_folder
Usage: python main.py src_folder dest_folder
```


## Testing

```bash
# Run the tests
./tests.py
#  OR
python tests.py
```
All tests shoud pass


## Contributing

Contributions and suggestions for improvement are highly welcomed.

Feel free to create a fork, submit an issue, feature request, or pull requests

## License

This project is free for distribution under the [MIT License](#license).
