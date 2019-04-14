def get_or_create_enginetype(database_session_to_act_on, engine_type_str):
    pass

def get_or_create_car_make(database_session_to_act_on, make_name):
    pass


def get_or_create_car(database_session_to_act_on, car_data_list):
    pass


def main_populate(dataset_filename):
    """Accepts dataset filename with expected CSV format. Opens CSV file, loads contents, closes file appropriately, and invokes above functions to populate database"""
    pass

if __name__ == "__main__":
    main_populate("cars.csv") # Invoke with main/expected dataset name cars.csv -- only if you run this specific file
