# -*- coding: utf-8 -*-
import click
import logging
from dotenv import find_dotenv, load_dotenv
import os
from pathlib import Path
import urllib.request
import shutil


def create_data_directory():
    os.makedirs('data/raw')
    os.makedirs('data/processed')
    os.makedirs('data/interim')
    os.makedirs('data/external')


@click.command()
# @click.argument('input_filepath', type=click.Path(exists=True))
# @click.argument('output_filepath', type=click.Path())
def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)

    logger.info('Checking data-folder')
    if not os.path.exists('data'):
        create_data_directory()

    logger.info('downloading data...')
    url = 'https://data.london.gov.uk/download/smartmeter-energy-use-data-in-london-households/3527bf39-d93e-4071-8451-df2ade1ea4f2/Power-Networks-LCL-June2015(withAcornGps).zip'
    file_path = Path('data/raw/')
    file_name = 'data_london.zip'
    with urllib.request.urlopen(url) as response, open(file_path.joinpath(file_name), 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
