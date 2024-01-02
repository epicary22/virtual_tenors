# Virtual Tenors

Real-life tenor drums are expensive and hard-to-store instruments. This changes that: you can now have a virtual set
of tenor drums on your PC! This tenor set is a set of quints (1 spock drum) with a cowbell.

## Installation & Execution
### bash/zsh: 
Run `git clone https://github.com/epicary22/virtual_tenors.git <directory>`, where `<directory>` is the directory you 
want to clone this repository into.  
Make sure you have pygame installed by running `python3 -m pip install pygame` in the `<directory>`.  
Then, run `python3 main.py` from the `<directory>` to start up the virtual tenors.

## How to Play
The tenor set will look like this upon startup:
ADD IMAGE HERE!!!  
You can play each drum by hitting these keys:
* 8-inch: `h` or `j`
* 10-inch: `d` or `f`
* 12-inch: `n` or `m`
* 13-inch: `x` or `c`
* Spock/6-inch: `v` or `b`
* Cowbell: `u`

You can tell the drum is hit when it lights up and plays a sound.

Don't be afraid to use both of the keys for each drum! This means you can use both your left and right hands to play
complex patterns.

## Configuration
If you don't like the default color or hit keys for the drums, you can configure them in `drumhead_data.json`.  
Each drum's `"down_color"` attribute describes which color it will become when hit.
The color's format is `[red, green, blue]`, where each of the values is between 0 and 255, inclusive.
You can use a <a href="https://g.co/kgs/xyHMC3A">color picker</a> to help choose your colors.  
Each drum's `"hit_keys"` attribute describes which keys activate it. You can add more letter keys by appending
the lowercase letter in quotes to the list. For instance, if you wanted to add the Q key to the cowbell's default,
the final list would look like `["u", "q"]`.  
Each drum's `"sound"` attribute has the path to the sound file it plays when hit. This path is relative to your current
directory if it's not an absolute path.

## Demonstration
Check out my demonstration for these virtual tenors: https://youtu.be/9BDgh0zvVg4

## Credits
Cowbell sound effect: https://pixabay.com/sound-effects/13-cowbell-85441/  
Tom sound effect: https://soundcamp.org/drum-samples-loops-and-one-shots/drum-single-hits-one-shots/tom-drum-samples/hi-tom-one-shot-b-key-13-9nz-wav
