import os.path

from app.storage import storage_base_path


def is_file_location_present_in_file() -> bool:
    storage_location = os.path.join(storage_base_path, "file_location.txt")

    with open(storage_location, "r") as file:
        file_location = file.readline().strip()

    if len(file_location) > 0:
        return True

    return False


def get_new_file_location() -> str:
    new_file_location = input("Please enter the location of the file: \n")

    storage_location = os.path.join(storage_base_path, "file_location.txt")

    with open(storage_location, "w") as f:
        # Write the new value to the file
        f.write(new_file_location)

    return new_file_location


def set_new_file_location(access_log_location: str) -> str:
    new_file_location = access_log_location

    storage_location = os.path.join(storage_base_path, "file_location.txt")

    with open(storage_location, "w") as f:
        # Write the new value to the file
        f.write(new_file_location)

    return new_file_location


def get_file_location() -> str:
    if is_file_location_present_in_file():
        file_location = os.path.join(storage_base_path, "file_location.txt")
        with open(file_location, "r") as file:
            file_location = file.readline().strip()
    else:
        file_location = get_new_file_location()

    return file_location
