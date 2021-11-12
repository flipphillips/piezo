# Test 1 2021-11-11 19:13:38

We just set up a single sensor on the FIP lab table. This is from the 'cooked' data. One second capture, so a 25000 samples, give or take.

The data ranges from [0,32767]. Here's a thing - The ADCs are 12-bit, meaning that they should only return between [0,4095] but it appears that there is some re-scaling that happens in the library that expands them to 32768 levels. 

So, to rescale these values, divide each by 32767.

- `01noise.dat` - bg noise
- `02near.dat` - first test, ball near
- `03far.dat` - ball far (some synthetic data because I made  bad copypaste)
