from app import EngineType, Make, Car
# If you are only going to run this file because it is imported into app.py, then this isn't necessary! But it's here in case we want to run this file on its own for any reason -- needs to be in same directory as this app.py
import csv

#########################################

def get_or_create_enginetype(database_session_to_act_on, engine_type_str):
    enginetype = EngineType.query.filter_by(name=engine_type_str).first()
    if not enginetype:
        enginetype = EngineType(name=engine_type_str)
        database_session_to_act_on.add(enginetype)
        database_session_to_act_on.commit()
    return enginetype

def get_or_create_car_make(database_session_to_act_on, make_name):
    make = Make.query.filter_by(name=make_name).first()
    if not make:
        make = Make(name=make_name)
        database_session_to_act_on.add(make)
        database_session_to_act_on.commit()
    return make


def get_or_create_car(database_session_to_act_on, car_data_list):
    pass

# Above functions all tools to be properly invoked in the main_populate function to do the full population of db; they are available should other types of data need to be handled with them (unlikely if you're depending on an existing dataset)

def main_populate(dataset_filename):
    """Accepts dataset filename with expected CSV format. Opens CSV file, loads contents, closes file appropriately, and invokes above functions to populate database"""
    # We'll use CSV module to handle CSV data


if __name__ == "__main__":
    main_populate("cars.csv") # Invoke with main/expected dataset name cars.csv -- only if you run this specific file
