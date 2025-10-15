from kopp14_vlm.kopp14_verticallandmotion_preprocess import (
    kopp14_preprocess_verticallandmotion,
)
from kopp14_vlm.kopp14_verticallandmotion_postprocess import (
    kopp14_postprocess_verticallandmotion,
)

import click


@click.command()
@click.option(
    "--pipeline-id", required=True, type=str, help="Unique identifier for the pipeline"
)
@click.option(
    "--rate-file",
    required=True,
    type=str,
    help="Path to the input rate file",
)
@click.option(
    "--nsamps",
    required=False,
    type=int,
    default=500,  # default in f1 script is 20k
    help="Number of samples to generate",
    show_default=True,
)
@click.option(
    "--rng-seed",
    required=False,
    type=int,
    default=1234,
    help="Seed value for random number generator",
    show_default=True,
)
@click.option(
    "--baseyear",
    required=False,
    type=click.IntRange(min=2000, max=2300),
    default=2000,
    help="Base or referecne year for projections",
    show_default=True,
)
@click.option(
    "--pyear-start",
    required=False,
    type=click.IntRange(min=2000, max=2300),
    default=2000,
    help="Year for which projections start",
    show_default=True,
)
@click.option(
    "--pyear-end",
    required=False,
    type=int,
    default=2100,
    help="Year for which projections end",
    show_default=True,
)
@click.option(
    "--pyear-step",
    required=False,
    type=click.IntRange(min=1),
    default=10,
    help="Step size in years between pyear_start and pyear_end at which projections are produced",
    show_default=True,
)
@click.option(
    "--location-file",
    required=True,
    type=str,
    help="File that contains name, id, lat, and lon of points for localization",
)
@click.option(
    "--chunk-size",
    required=False,
    type=int,
    default=50,
    help="Number of locations to process at a time",
    show_default=True,
)
@click.option(
    "--output-lslr-file",
    required=False,
    type=str,
    help="Path to the output local SLR netCDF file",
)
def main(
    pipeline_id,
    rate_file,
    nsamps,
    rng_seed,
    baseyear,
    pyear_start,
    pyear_end,
    pyear_step,
    location_file,
    chunk_size,
    output_lslr_file,
):
    """ """
    click.echo("Hello from Kopp14-vlm!")

    preprocess_dict = kopp14_preprocess_verticallandmotion(pipeline_id, rate_file)
    
    kopp14_postprocess_verticallandmotion(
        preprocess_dict=preprocess_dict,
        nsamps=nsamps,
        rng_seed=rng_seed,
        baseyear=baseyear,
        pyear_start=pyear_start,
        pyear_end=pyear_end,
        pyear_step=pyear_step,
        locationfile=location_file,
        chunksize=chunk_size,
        pipeline_id=pipeline_id,
        output_lslr_file=output_lslr_file,
    )
