# kopp14-vlm
This module implements the Kopp et al. (2014) long-term background contribution methodology, as employed in IPCC AR6. It includes long-term (centennial-scale) contributions from vertical land motion and other background process (e.g., geoid effects of glacial isostatic adjustment). See iPCC AR6 WG1 9.6.3.2.9.

>[!CAUTION]
> This is a prototype. It is likely to change in breaking ways. It might delete all your data. Don't use it in production.

## Example

TODO

### Setup

Clone the repository and create directories to hold input and output data. 

```shell
git clone git@github.com:fact-sealevel/kopp14-vlm.git

# Input data we will pass to the container
mkdir -p ./data/input

echo "New_York	12	40.70	-74.01" > ./data/input/location.lst

# Output projections will appear here
mkdir -p ./data/output
```

Next, run the container associated with this package. For example: 

TODO 

## Features

See this help documentation by passing the `--help` flag when running the application, for example: 

```shell
docker run --rm kopp14-vlm --help
```   

## Results
TODO

## Build the container locally
You can build the container with Docker by cloning the repository locally and then running the following command from the repository root:

```shell
docker build -t kopp14-vlm .

```

## Support

Source code is available online at https://github.com/facts-org/kopp14-vlm. This software is open source, available under the MIT license.

Please file issues in the issue tracker at https://github.com/facts-org/kopp14-vlm/issues.