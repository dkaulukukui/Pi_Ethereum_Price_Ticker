# Pi_Ethereum_Price_Ticker

Python script that continuously grabs the current etheruem price via coinbase API and displays it via a SURE 0832 LED matrix display

## Prerequisites

Utlizes the Python HT1632 library by mchester
https://github.com/mchestr/HT1632C-Python

Follow the instructions on this github for installation and testing first.  If the samples dont work then the ticker wont work.

## Hardware

The SURE panel I am using is no longer available for sale however is the one listed here:
https://alastair.d-silva.org/system/files/DE-DP105_Ver1.0_EN_0.pdf

## Wiring

Using a Raspberry PI model Zero W, you need to connect some GPIO pins to the
LED Matrix BR1 port, the input port, like this:


| RPI Label      | Pin | SURE Label | Pin |
|----------------|-----|------------|-----|
| GND            | 6   | GND        | 8   |
| 5V             | 4   | 5V         | 16  |
| GPIO 10 (MOSI) | 19  | DATA       | 7   |
| GPIO 11 (SCLK) | 23  | WR         | 5   |
| GPIO 8  (CE0)  | 24  | CLK        | 2   |
| GPIO 7  (CE1)  | 26  | CS         | 1   |

