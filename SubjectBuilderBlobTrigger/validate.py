import logging


def column_headers(header_row):
    logging.info(f"Validating header row, headers: {header_row}")
    header_list = header_row.split(',')
    
    valid = True
    if header_list[0] != "code":
        logging.info(f"got in code: {header_list[0]}")
        valid = False

    if header_list[1] != "english_label":
        logging.info(f"got in english_label: {header_list[1]}")
        valid = False

    if header_list[2] != "level":
        logging.info(f"got in level: {header_list[2]}")
        valid = False

    if header_list[3] != "welsh_label":
        logging.info(f"got in welsh_label: {header_list[3]}")
        valid = False

    return valid
