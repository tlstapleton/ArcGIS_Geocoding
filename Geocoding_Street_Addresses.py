
import pandas as pd
import argparse
from arcgis.gis import *
from arcgis.geocoding import geocode, reverse_geocode
from arcgis.geometry import Point
pd.options.mode.chained_assignment = None

def parse_args():
    """ Setup the input and output arguments for the script
    Return the parsed input and output files
    """
    parser = argparse.ArgumentParser(description='Geocode Street Addresses with ArcGIS')
    parser.add_argument('infile',
                        type=argparse.FileType('r'),
                        help='geocoding address inputs')
    parser.add_argument('outfile',
                        type=argparse.FileType('w'),
                        help='Output geocoded coordinates')
    return parser.parse_args()

def geocode_address(input, output):
    dev_gis=GIS()
    df=pd.read_csv(input)
    lat=[]
    lng=[]
    for index, row in df.iterrows():
        address = row['searchText']
        response=geocode(address=address, max_locations=1)
        lat.append(response[0]['location']['y'])
        lng.append(response[0]['location']['x'])
    df['lat']=lat
    df['lng']=lng
    df.to_csv(output)


if __name__ == "__main__":
    args = parse_args()
    geocode_address(args.infile.name,args.outfile.name)

