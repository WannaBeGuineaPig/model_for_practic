__all__ = [
    'request_api',
    'formatting_output_data_API',
    'save_temporary_file',
    'deleted_temporary_file',
]

import base64, os

from requests import get

BASE_URL_API = 'http://127.0.0.1:8000/'

def request_api(path_to_api: str, attemp_to_reauest:int = 3):
    full_url = f'{BASE_URL_API}{path_to_api}'
    errors = []

    while True:
        if attemp_to_reauest == 0:
            return {'error' : errors}
        
        try:
            response = get(full_url)
            break

        except Exception as e:
            errors.append(e)

        attemp_to_reauest -= 1

    return response.json()

def formatting_output_data_API(dct: dict) -> str:
    return f'Название файла: {dct['name_file']};\n\nДата последнего изменения: {dct['date_last_modified_file']};\n\nНайденный схожий текст:\n{dct["find_similarity"]}'

def save_temporary_file(path_file, data_file_base64: str) -> str:
    data_bytes = base64.b64decode(data_file_base64)
    with open(path_file, 'wb') as file:
        file.write(data_bytes)

def deleted_temporary_file(path_file: str) -> str:
    os.remove(path_file)