#!/bin/bash

# Loop through all .deb files in the current directory and subdirectories
printf '' > Packages
find . -type f -name "*.deb" | while read -r deb_file; do
    # Extract control.tar.gz from the .deb file into the temporary directory
    ar x "$deb_file" control.tar.gz #-C "$tmp_dir"
    
    # If control.tar.gz was successfully extracted
    if [ -f "./control.tar.gz" ]; then
        # Create a directory named control_extracted within the .deb's directory if it doesn't exist
        #printf '' > Packages
        tar -xf control.tar.gz ./control
        rm control.tar.gz
        printf "%s\n" $deb_file
        python3 gz_generator.py control $deb_file >> Packages
        #gzip -c Packages > Packages.gz
        rm control
    else
        echo "control.tar.gz not found in $deb_file"
    fi
done
