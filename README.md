
# Video Caption Renderer

This Python script reads a WebVTT file and generates a video that displays the captions at the appropriate times, without any sound.

## Prerequisites

This project requires Python 3.6 or higher. 

The following Python packages are also required:
- moviepy
- webvtt-py

You can install these packages using pip:

```bash
pip install moviepy webvtt-py
```

This script also requires ImageMagick for rendering text. You can download ImageMagick from the [official website](https://imagemagick.org/script/download.php). After installation, make sure to specify the path to the ImageMagick binary in your `moviepy` configuration.

## Usage

To use this script, simply run it with Python:

```bash
python main.py
```

The script will generate a video named `output.mp4` in the current directory. The video will display the captions from the input WebVTT file at the appropriate times.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
