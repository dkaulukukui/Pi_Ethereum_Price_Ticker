# Pi_Ethereum_Price_Ticker

Python script that continuously grabs the current etheruem price via coinbase API and displays it via most HT1632c driven LED matrix displays.  

## Prerequisites

Utlizes the Python HT1632 library by mchester
https://github.com/mchestr/HT1632C-Python (out of date install instructions, see below)

I have cloned and updated the installation instructions and stored them here:
https://github.com/dkaulukukui/HT1632C-Python

I have included the modified HT1632C-Python files used for my setup in this repo. 

Execute the following commands to have an updated package database, and
to install python-dev and git-core:

```
sudo apt-get update
sudo apt-get install python-dev
sudo apt-get install git

sudo apt-get install -y python-setuptools
```

You are now ready to install the wiringPi library. You may have a look
at http://wiringpi.com/ for further information and documentation.
WiringPi is PRE-INSTALLED with standard Raspbian systems.

To update or install on a Raspbian-Lite system:
```
sudo apt-get install wiringpi
```

### Enable SPI on Board
This is done through raspi-config.  Go

```
sudo raspi-config

```
Select Option 5 Interfacing Options
Select Option P4 SPI
Select Yes to enable SPI

After all of that you should be able to clone this git and run an example I have

```
git clone git://github.com/dkaulukukui/Pi_Ethereum_Price_Ticker.git

```

Navigate to the HT Directory and install

```
 cd Pi_Ethereum_Price_Ticker/HT1632C-Python
 sudo python setup.py install

```
Start by running the wipe example

```
 cd examples
 sudo python wipe.py

```
NOTE: Any changes made after the initial install above to the panelconfig.h (or any of the ht1632 library files for that matter) file will require you to delete the entire "build" directory and then recompile.

```
sudo rm -r ./build (from HT1632C-Python directory)

sudo python setup.py install

```


You will now need to install pip and the feed parser python module:
https://pypi.org/project/feedparser/

```
sudo apt-get install python-pip

sudo pip install feedparser
sudo pip install requests

```

Once the above is complete you should be able to run the main script:

```
 sudo python setup.py install

```




## Hardware

The SURE panel I am using is an older SURE0832 panel that still uses the newer HT1632C chipset.  

SURE model 15151-11V110 however as of this writing I can no longer find it for sale online.

I have tested it with this cheap AliExpress version and it works plug and play:

https://www.aliexpress.com/item/Lattice-Breakout-LED-HT1632C-Module-8X32-Red-Dot-matrix-Screen/32681502073.html?spm=a2g0s.9042311.0.0.51504c4doAaNF3

They are being sold as "Lattice Breakout LED HT1632C Modules".  For $8 you cant go wrong.


## Wiring

Using a Raspberry PI model Zero W, you need to connect some GPIO pins to the SURE matrix display port:


| RPI Label      | Pin | SURE Label | Pin |
|----------------|-----|------------|-----|
| GND            | 6   | GND        | 8   |
| 5V             | 4   | 5V         | 16  |
| GPIO 10 (MOSI) | 19  | DATA       | 7   |
| GPIO 11 (SCLK) | 23  | WR         | 5   |
| GPIO 8  (CE0)  | 24  | CS1        | 2   |


## Notes

- When testing the the panel or the SPI interface tends to get hung up after making changes.  Especially to any of the ht1632 library files and when recompiling.  A soft reset of the raspi normally does the trick.  Try disconnecting then reconnecting if that doesnt work.

