from app import EngineType, Make, Car, session
# If you are only going to run this file because it is imported into app.py, then this isn't necessary! But it's here in case we want to run this file on its own for any reason -- needs to be in same directory as this app.py
import csv

#########################################

def get_or_create_enginetype(engine_type_str):
    enginetype = EngineType.query.filter_by(name=engine_type_str).first()
    if not enginetype:
        enginetype = EngineType(name=engine_type_str)
        session.add(enginetype)
        session.commit()
    return enginetype

def get_or_create_car_make(make_name):
    make = Make.query.filter_by(name=make_name).first()
    if not make:
        make = Make(name=make_name)
        session.add(make)
        session.commit()
    return make


def get_or_create_car(car_data_dictionary):
    """Accepts list of data about a car -- can assume this is a dictionary of the format of a row of the sample cars.csv file -- and uses that to save a new car and build relationships appropriately."""
    # City mpg,Classification,Driveline,Engine Type,Fuel Type,Height,Highway mpg,Horsepower,Hybrid,ID,Length,Make,Model Year,Number of Forward Gears,Torque,Transmission,Width,Year
    ## ^ Copy in headers from CSV file to refer to

    # Decide what makes a car unique to query for it -- under what case do I NOT want to add this row of data?
    # Model Year, automatic_transmission bool val, and torque ...

    # # City mpg,Classification,Driveline,Engine Type,Fuel Type,Height,Highway mpg,Horsepower,Hybrid,ID,Length,Make,Model Year,Number of Forward Gears,Torque,Transmission,Width,Year
    car = Car.query.filter_by(model_year=car_data_dictionary["Model Year"], torque=car_data_dictionary["Torque"], automatic_transmission=True if car_data_dictionary["Classification"]=="Automatic transmission" else False).first() # "Find the first car that has this dictionary's same model yr, torque, and value of automatic_transmission -- True if this one should be True and False otherwise" -- transmission data re: looking at data
    if not car: # If there isn't one like that
        # Then create a new car instance with same var

        # First create these instances to be able to refer to
        make = get_or_create_car_make( car_data_dictionary["Make"])
        enginetype = get_or_create_enginetype( car_data_dictionary["Engine Type"])

        # Now the car instance itself -- complex but mostly only gotta write this once...
        car = Car(city_mpg=car_data_dictionary["City mpg"], driveline=car_data_dictionary["Driveline"],make=make,enginetype=enginetype,torque=car_data_dictionary["Torque"],model_year=car_data_dictionary["Model Year"], highway_mpg=car_data_dictionary["Highway mpg"],horsepower=car_data_dictionary["Horsepower"], automatic_transmission=True if car_data_dictionary["Classification"]=="Automatic transmission" else False)
        session.add(car)
        session.commit()

    return car
    # Note that this function ^ does NOT allow for updating info easily -- this is showing a simpler version of code that creates if it doesn't exist, but doesn't update existing data thru this manual population format -- if a car with this info exists...

# Above functions all tools to be properly invoked in the main_populate function to do the full population of db; they are available should other types of data need to be handled with them (unlikely if you're depending on an existing dataset)

def main_populate(dataset_filename):
    """Accepts dataset filename with expected CSV format. Opens CSV file, loads contents, closes file appropriately, and invokes above functions to populate database"""
    # We'll use CSV module to handle CSV data
    # First we'll want to run a quick test to see if one of those things works... see in app.py running
    try:
        with open(dataset_filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for ln in reader:
                # print(ln) # an OrderedDict
                get_or_create_car(ln) # ln should be a dictionary
    except:
        return False # Could TODO raise exception to specify what went wrong, but this could be OK



if __name__ == "__main__":
    pass
