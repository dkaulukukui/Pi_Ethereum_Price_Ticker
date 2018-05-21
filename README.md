# Pi_Ethereum_Price_Ticker

Python script that continuously grabs the current etheruem price via coinbase API and displays it via a SURE 0832 LED matrix display.  Should work with any of the other more readily available HT1632 matrix led displays currenlty available with some minor modifications.

## Prerequisites

Utlizes the Python HT1632 library by mchester
https://github.com/mchestr/HT1632C-Python

Follow the instructions on his git for installation and testing first.  If the samples dont work then the ticker wont work.

Any changes made to the panelconfig.h (or any of the ht1632 library files for that matter) file will require you to delete the entire "build" directory and then recompile.

sudo rm -r ./build (from HT1632C-Python directory)

sudo python setup.py install

You will need the feed parser python module:
https://pypi.org/project/feedparser/

sudo pip install feed parser

## Hardware

The SURE panel I am using is an older SURE0832 panel that still uses the newer HT1632C chipset.

The datasheet for the older panel is here:
https://alastair.d-silva.org/system/files/DE-DP105_Ver1.0_EN_0.pdf

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

