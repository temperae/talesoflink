#!/bin/bash
# Remove directories used for parsing (if they exist)
rm -rf cleaned formatted parsed transcript.txt

# Create new copies of these directories
mkdir cleaned formatted parsed

# Initial parse of raw transcript files:
for i in $( ls raw ); do
    python parse_script.py raw/$i >parsed/$i
done

# Clean up parsed files so they can be formatted nicely:
for i in $( ls parsed ); do
    python clean_parsed.py parsed/$i >cleaned/$i
done

# Format the cleaned files into wiki markup:
for i in $( ls cleaned ); do
    python format_script.py cleaned/$i >formatted/$i
done

# Take the output of every formatted file and concatenate them
# into one giant file:
for i in $( ls formatted ); do
    echo "$( printf "===%s===\n" "$i" )" >> transcript.txt
    echo "$( cat formatted/$i )" >> transcript.txt
    echo "$( printf "\n" )" >> transcript.txt
done

# Delete temporary directories:
rm -rf cleaned formatted parsed
