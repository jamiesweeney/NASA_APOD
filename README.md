# NASA_APOD

The National Aeronautics and Space Administration - Astronomy Picture of the Day

This is a small python application with the purpose of bulk downloading the NASA Astronomy Picture of the Day.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

[Python 3](https://www.python.org/download/releases/3.0/)

### Installing

Install Python 3 (if you don't already have it)

Clone the repository
```
git clone https://github.com/jamiesweeney/NASA_APOD
```

Get your own NASA API key from https://api.nasa.gov/index.html 

Add it as an environmental variable on your OS under the name "NASA_API_KEY".

Alternatively use the default key with a limited a number of requests:

"DEMO_KEY"  

## Using the application
Run the application using the following command:

```
python src/getPhotos.py START_DATE END_DATE
```
Where the dates are provided in the format YYYY-MM-DD e.g
```
python src/getPhotos.py 2018-01-01 2018-01-31
```
Which will download all the images from January 2018.

If any of the dates are unspecified or are the wrong format, then the date will default to the current date.

## Running the tests

No tests yet

## Authors

* **Jamie Sweeney** - [jamiesweeney](https://github.com/jamiesweeney)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE v3 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* README adapted from a [template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) by [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* NASA images can be found [here](https://apod.nasa.gov/apod/archivepix.html)