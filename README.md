# Autoclicker
Down and dirty fast auto-clicker with a few options

# Python Autoclicker Script

This Python script offers a customizable autoclicker with pause and stop (kill switch) functionalities. It allows users to set the time between clicks, the duration of each click, and the total number of clicks. Additionally, users can pause and resume the autoclicking process without needing to stop or restart the script.

## Features

- **Customizable Click Intervals**: Set the time between clicks in milliseconds.
- **Customizable Click Durations**: Set how long each click is held, also in milliseconds.
- **Repeat Configuration**: Choose how many times the click should be repeated. Setting this to `0` allows for infinite clicking until the script is paused or stopped.
- **Pause/Resume**: The script can be paused and resumed using a designated hotkey.
- **Kill Switch**: A specific key press stops the autoclicker at any time.

## Requirements

Before running the script, ensure you have Python installed on your system and the following Python packages:

- `pynput`

You can install `pynput` using pip:

```bash
pip install pynput

## Usage

1. Start the script by running it in your Python environment.
2. When prompted, enter the desired time in milliseconds for the wait between clicks, the duration of each click, and the total number of repeats.
3. Once started, the script will listen for the following key presses:
   - Press `p` to pause or resume the autoclicker.
   - Press `k` to stop the autoclicker.

## Contributing
Feel free to fork this repository and submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [MIT License](https://opensource.org/licenses/MIT) page for details.
