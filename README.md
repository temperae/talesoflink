# Requirements

* Bash (or Git Bash)
* Python 3.x
   * When installing Python, make sure to add it to your PATH. 
   * If you're using the installer, there's a box you'll need to check ("Add Python 3.x to PATH").
   
# Usage

* Dump all your raw transcript files into the `raw/` directory
    * **[NOTE]** This script will format _everything_ in `raw/`, so delete older transcript files from that directory if you don't need them anymore!
* Run `parse.sh`
* `parse.sh` will generate a new file (`transcript.txt`) containing all the wiki-formatted transcripts

# Troubleshooting

* `python: command not found`
   * Python is not added to your PATH
* `TypeError: 'encoding' is an invalid keyword argument for this function`
   * Upgrade your Python to 3.x
   * You can check your Python version in Bash by typing: `python --version`
* If you're running MacOSX, you may need to change all the scripts to use `python3` instead of just `python`
