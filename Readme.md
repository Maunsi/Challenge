# Maureen's challenge submission!

## Requirements:
To be able to run, ```python3```, ```pip3``` and ``make`` should be installed.

## To run invitations:
Open a new terminal window and run:  
```make run```

This creates a virtual environment which installs all required dependencies. 

If the dependencies are already installed, it can also be ran like:

```python3 main.py ```

Parameters can be tweaked if needed:

```python3 main.py -l <location_file>  -d <distance_in_km> -office <office latitude> <office longitude> -o <output_file>```

To get help:
```python3 main.py -h```

The input file will be downloaded into the input_files directory, 
the result will be outputted into the output.csv file in the output_files directory

## To run tests:
Open a new terminal window and run:  

```make test```

Output files will be written to the output_files folder