# AutomaticTinderSwiper

## Overview

A Python3 script which automates allowing one to login to Tinder and interact with the web application using Selenium.

## Previous Work and Motivations

The original idea for this project came about from a conversation in the pub - as all great ideas do ;) - where the following reddit post titled [Automate the boring stuff with python - tinder](https://www.reddit.com/r/Python/comments/7kpme8/automate_the_boring_stuff_with_python_tinder/) by [u/backprop88](https://www.reddit.com/user/backprop88) was resurfaced.

The `pyautogui` library was really cool and I have been enjoying learning more about it, but the example presented in the gif preseted the very obvious problem whereby you lost control of your computer inputs. Following a quick bit of research on GitHub, I came across the following repo titled [TinderAutoSwipe_Selenium](https://github.com/dbangera23/TinderAutoSwipe_Selenium) by [Dean Bangera (dbangera23)](https://github.com/dbangera23). I downloaded Dean's code and began experimenting. Major fixes involved editing the UI element interactions due to the different layout implemented by web Tinder.

## Installation and Requirements

This script utilizes Python3, Selenium, and the Google Chrome webdriver. Python3 and Selenium can be downloaded to your environment using `PiP`, but the Google Chrome webdriver I had to download (and append to my `PATH`) separately. More information on them is available here:

Python3 can be found [here](https://www.python.org/downloads/).

Selenium can be found [here](http://www.seleniumhq.org/download/).

Google Chrome webdriver will be required with Selenium. This can be found [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## ScriptFlow - V1

* Navigate to Facebook.com and login using your provided username and password.
* Navigate to Tinder.com and login via Facebook SSO.
* Pass through the various tutorial screens.
* Swipe right on every profile until no profiles are remaining.
* The script quits and the browser is closed.

## Ideas and Improvements for V2

- [ ] Upon a match, a new pop-up window appears. This needs to be accounted for as additional logic to return to the profile viewer and continue swiping. V1 currently quits following a match.
- [ ] Pause and end on console input. Currently the script swipes right whilst a profile can be swiped right. A method to pause or stop based on the console inputs would therefore be more useful.
- [ ] Random time insertion. Currently the script clicks every `0.2` seconds. Whilst this feels like a normal human interaction / speed, this may raise the suspicions of bot checkers being so perfect. A random time should therefore be implemented throughout to prevent this.

## Ideas and Improvements for V3
- [ ] Additional logic to analyse profile pictures.
- [ ] Additional logic to analyse profile text.
