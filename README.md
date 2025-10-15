# kopp14-verticallandmotion
This module implements the Kopp et al. (2014) long-term background contribution methodology, as employed in IPCC AR6. It includes long-term (centennial-scale) contributions from vertical land motion and other background process (e.g., geoid effects of glacial isostatic adjustment). See iPCC AR6 WG1 9.6.3.2.9.

>[!CAUTION]
> This is a prototype. It is likely to change in breaking ways. It might delete all your data. Don't use it in production.

## Example

### Setup

Clone the repository and create directories to hold input and output data. 

```shell
#git clone git@github.com:fact-sealevel/kopp14-verticallandmotion.git
#^eventually, for now :
git clone --single-branch --branch package git@github.com:e-marshall/kopp14-verticallandmotion.git
```

Input data we will pass to the container
```
mkdir -p ./data/input
curl -sL https://zenodo.org/record/7478192/files/kopp14_verticallandmotion_preprocess_data.tgz | tar -zx -C ./data/input
echo "New_York	12	40.70	-74.01" > ./data/input/location.lst

# Output projections will appear here
mkdir -p ./data/output
```

Next, run the container associated with this package. For example: 
```shell
docker run --rm \
-v /path/to/kopp14-verticallandmotion/data/input:/mnt/kopp14verticallandmotion_data_in:ro \
-v /path/to/kopp14-verticallandmotion/data/output:/mnt/kopp14verticallandmotion_data_out \
kopp14-verticallandmotion \
--pipeline-id MY_PIPELINE_ID \
--rate-file /mnt/kopp14verticallandmotion_data_in/bkgdrate-210306.tsv \
--location-file /mnt/kopp14verticallandmotion_data_in/location.lst \
--output-lslr-file /mnt/kopp14verticallandmotion_data_out/localsl.nc
``` 

## Features
```shell
Usage: kopp14-verticallandmotion [OPTIONS]

Options:
  --pipeline-id TEXT           Unique identifier for the pipeline  [required]
  --rate-file TEXT             Path to the input rate file  [required]
  --nsamps INTEGER             Number of samples to generate  [default: 500]
  --rng-seed INTEGER           Seed value for random number generator
                               [default: 1234]
  --baseyear INTEGER RANGE     Base or referecne year for projections
                               [default: 2000; 2000<=x<=2300]
  --pyear-start INTEGER RANGE  Year for which projections start  [default:
                               2000; 2000<=x<=2300]
  --pyear-end INTEGER          Year for which projections end  [default: 2100]
  --pyear-step INTEGER RANGE   Step size in years between pyear_start and
                               pyear_end at which projections are produced
                               [default: 10; x>=1]
  --location-file TEXT         File that contains name, id, lat, and lon of
                               points for localization  [required]
  --chunk-size INTEGER         Number of locations to process at a time
                               [default: 50]
  --output-lslr-file TEXT      Path to the output local SLR netCDF file
  --help                       Show this message and exit.
```
See this help documentation by passing the `--help` flag when running the application, for example: 

```shell
docker run --rm kopp14-verticallandmotion --help
```   

## Results
If this module runs successfully, one netCDF file containing local sea level change projections will be written to `./data/output`.

## Build the container locally
You can build the container with Docker by cloning the repository locally and then running the following command from the repository root:

```shell
docker build -t kopp14-verticallandmotion .
```

## Support

Source code is available online at https://github.com/facts-org/kopp14-verticallandmotion. This software is open source, available under the MIT license.

Please file issues in the issue tracker at https://github.com/facts-org/kopp14-verticallandmotion/issues.
