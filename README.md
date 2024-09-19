# 

# ESI Maya22 GUI controller.

This repository provides all the source files used to create the "maya22\_package.deb" package. You can download and build your own package or simply download the `.deb` file and install it using `dpkg -i maya22_package.deb`.

## Creating the Debian Package

This repository includes all the files and configurations required to create a Debian package for the ESI Maya22 GUI controller.

ESI Maya22 USB Packege DEB

This project provides a command line interface and a graphical interface to control the [ESI Maya22](http://www.esi-audio.com/products/maya22usb/) usb sound device. The interface allows you to adjust input and output volumes, enable/disable monitoring and headphones, and synchronize output volumes. Configuration is automatically saved to a JSON file.

![panel control](./docs/images/img1.png)

The graphical interface is achieved by running the "main.py" file, which launches a GUI using python-tk. This interface interacts with "[maya22-control](https://github.com/piposeimandi/esi-maya22-linux)" 

## General Features

- Adjust input volumes (left and right).
- Adjust output volumes (left and right).
- Automatic synchronization of output volumes.
- Enable and disable monitoring.
- Enable and disable (all output).
- Select input channel.
- Automatic configuration saving in a JSON file.

## Requirements

- Python 3.x
- Tkinter for Python - The standard Python library for creating graphical user interfaces (GUIs). It provides a simple way to build desktop applications using Python with a native look and feel on different operating systems.
- (Incluida in the Deb ) "[maya22-control](https://github.com/piposeimandi/esi-maya22-linux)"

This will install Python 3, the Tkinter GUI toolkit. 



## Contact

For any questions or comments, please contact [bajosega@gmail.com](mailto:bajosega@gmail.com).
