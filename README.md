FHP IO galton board physarum
======

![slime mold](http://topada.hercules.uberspace.de/d_fhp/io/doc/02_slime_mold/io_2_0.png)

##Abstract
###The Input Output Course ([University of Applied Science, Potsdam](http://www.fh-potsdam.de/)) continued with the assignment to experiment with **slime mold, physarum polycephalum** to be exact, building a timelapse setup with a raspberry pi controlled camera and analysing the captured video with computer vision algorithm.

So, what's a slime mold again? It is an incredibly interesting being – the yellow complex with its tiny slimy roots lives, if not in a forest, in a petri dish and grows fairly quick once it is served something delicious as oat flakes for example. Its not a mushroom nor a plant. It has the capability to *smell* and locate energy resources and has a *slime memory:* as it grows, it leaves a slimy trail of dead cells behind.

##Timelapse Studio Setup
In order to capture my own timelapse, a slimelapse actually, of the physarium growing, I attached my Nikon D90 **DSLR** to a **RaspberryPi** and attached both an old carton.  

![slime mold](http://topada.hercules.uberspace.de/d_fhp/io/doc/02_slime_mold/io_2_2.png)

Unfortunately we already had bought a camera module for our RasperryPis, just to learn that those cheap cams had no refocusing and were impractical for this project. I decided to use a [DSLR controlled by the RaspberryPi instead, which I described in detail.](https://github.com/topada/DSLR-Timelapse-gphoto-RPI)

With this setup I could capture about 700 medium sized images with a full battery load. In total I took **8,382 images** during this experimental project.

##Experiment
Then we had to come up with a suitable experiment of the physarum. After I experimented a lot with salt as a growth inhibitor, but my results weren't satisfying at all. Therefore I decided to analyse the slime molds behavior within a **[galton board](https://en.wikipedia.org/wiki/Bean_machine) like oat flake setup**. I was curious how the mold would grow from flake to flake.

![slime mold](http://topada.hercules.uberspace.de/d_fhp/io/doc/02_slime_mold/io_2_1.png)

##Computer Vision
In the end, we learned about computer vision (CV) algorithm and how to use them with processing. I wanted to create an algorithm that tracks the physarum growth and the order in which the oat flakes are *eaten.* 

I realized the **Physarum Tracking** by isolating the saturation channel and tracking changing contours. **The Oat Recognition** on the other hand solely uses the first frame of the timelapse material and utilizes the lightness channel to track the right contours.

Once those two procedures intersect another oat has been captured by the physarum.

![slime mold](http://topada.hercules.uberspace.de/d_fhp/io/doc/02_slime_mold/io_2_4.png)

##What's it for?
I consider this project to be highly experimental and I don't expect any outcome in a higher sense. This tiny experiment taught me vast knowledge about raspberryPi and computer vision. 

However, I'd love to see the galton board like physarum experiment to turn into a live online bitcoin gambling experience. Someday.

##Thanks
I want to thank our tutor pal [@fabiantheblind](https://github.com/fabiantheblind), whose inspiring excitement always pushed us further. Also, I have to thank my fellow students for their helping critisim and ideas.

##Ahoi
Follow me on twitter [@topada](http://twitter.com/topada), or get in touch via mail [info@topada.de](mailto:info@topada.de), I'll keep you informed as soon as topada.de eventually rises from the grave.

##License
![CC_CC](http://creativecommons.org/wp-content/themes/creativecommons.org/images/chooser_cc.png)
![CC_BY](http://creativecommons.org/wp-content/themes/creativecommons.org/images/chooser_by.png)
![CC_NC](http://creativecommons.org/wp-content/themes/creativecommons.org/images/chooser_nc.png)
![CC_SA](http://creativecommons.org/wp-content/themes/creativecommons.org/images/chooser_sa.png)

This project is licensed under a [**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License**](http://creativecommons.org/licenses/by-nc-sa/4.0/)

###The source code is licensed under the MIT License (MIT)

Copyright (c) 2015 Jonas Köpfer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
