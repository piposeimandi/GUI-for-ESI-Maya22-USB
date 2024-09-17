# GUI for ESI Maya22 USB

This project provides a command line interface and a graphical interface to control the [ESI Maya22](http://www.esi-audio.com/products/maya22usb/) usb sound device. The interface allows you to adjust input and output volumes, enable/disable monitoring and headphones, and synchronize output volumes. Configuration is automatically saved to a JSON file.

![panel control](./docs/images/img1.png)

The graphical interface is achieved by running the "main.py" file, which launches a GUI using python-tk. This interface interacts with "maya22-control.py," which communicates with the python-hidapi library responsible for sending and receiving data with the Maya22 USB sound interface.

1. `.command/maya22-control.py` - Can be used via command line. More information is available in the readme.md. It handles sending and receiving data from the sound card using the hidapi library.

2. `main.py` - Launches a graphical interface through which you can interact with `maya22-control.py`. Commands can be sent via the graphical interface.

## General Features

- Adjust input volumes (left and right).
- Adjust output volumes (left and right).
- Automatic synchronization of output volumes.
- Enable and disable monitoring.
- Enable headphones (all output).
- Select input channel.
- Automatic configuration saving in a JSON file.

## Requirements

- Python 3.x
- Tkinter for Python - The standard Python library for creating graphical user interfaces (GUIs). It provides a simple way to build desktop applications using Python with a native look and feel on different operating systems.
- HIDAPI for Python - A Python library that provides cross-platform support for communicating with USB and Bluetooth Human Interface Devices (HID). It allows easy interaction with HID devices like keyboards, mice, game controllers, and more.

## Installation

1. Clone this repository:

   `git clone https://github.com/piposeimandi/esi-maya22-linux-gui`

2. Navigate to the project directory:

   `cd esi-maya22-linux-gui`

## Installing Dependencies for ESI Maya22 Controller

### For Debian/Ubuntu Systems

To install the required dependencies using `apt-get`, follow these steps:

1. Update your package list:

   `sudo apt-get update`

2. Install the necessary packages:

   `sudo apt-get install python3 python3-tk python3-hid`

This will install Python 3, the Tkinter GUI toolkit, and HID support.

### For Arch Linux Systems

To install the required dependencies using `pacman`, follow these steps:

1. Update your system:

   `sudo pacman -Syu`

2. Install the necessary packages:

   `sudo pacman -S python python-tk python-hidapi`

These commands will install Python, Tkinter, and HID support on Arch Linux.

## After Installation

Once the dependencies are installed, you can run the Python script as usual:

   `python3 main.py`

## Configuration

Configuration is saved in a JSON file named `config.json` in the same directory as the script. Settings are automatically loaded from this file when the application starts.

## Information

It was made possible thanks to the original `maya22-control` from the [rabits/esi-maya22-linux](https://github.com/rabits/esi-maya22-linux) repository.

## Contributions

Contributions are welcome. If you find any bugs or have improvements to propose, please open an issue or a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or comments, please contact [bajosega@gmail.com](mailto:bajosega@gmail.com).

