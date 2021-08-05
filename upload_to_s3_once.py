import json
import pathlib
import boto3


def load_json(file_location):
    """I like creating json dictionaries that store all my configuration settings"""
    with open(file_location, 'r+') as file:
        return json.load(file)


def print_to_log(ingestible_item, log_location):
    """easy log writer that doesn't open and close for each line."""
    with open(log_location, 'a+') as log:
        log.writelines(ingestible_item)
    return ingestible_item


def get_files_in_folder(folder_location):
    return [x for x in pathlib.Path(folder_location) if x.is_file()]


def upload_files_in_folder(file_collection, bucket_name, file_collection_folder):
    s3 = boto3.resource('s3')
    return list(map(lambda x: s3.meta.upload_file(str(file_collection_folder + x), bucket_name, x), file_collection))


def main(config_location):
    config = load_json(config_location)
    files = get_files_in_folder(config['folder_location'])
    return print_to_log(upload_files_in_folder(files, config['bucket_name'], config['folder_location']))


if __name__ == '__main__':
    main('monitored_folder.json')
