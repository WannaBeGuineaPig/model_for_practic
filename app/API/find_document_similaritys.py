__all__ = [
    'TextCleaning',
    'ParsingDocumentation',
    'FindDocumentSimilaritys',
]

import pandas as pd, numpy as np, os, string, re, pymorphy3, base64

from pickle import load
from datetime import datetime
from spire.doc import Document
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine

PATH_TO_DOCUMENTATION = "./documentation"
PATH_TO_VECTORIZER = "./vectorizer.pkl"

class TextCleaning:
    def __init__(self):
        # Русские стоп слова
        self.russian_stopwords = stopwords.words("russian")
        self.russian_stopwords.extend(['т.д.', 'т', 'д', 'это','который','с','своём','всем','наш', 'свой']) 

        # Анализатор для лемматизация
        self.morph = pymorphy3.MorphAnalyzer(lang='ru')

        # Специальные символы
        self.special_symbols = '❯\xa0—«»–'
    
    # Функция для удаления ссылок
    def remove_link(self, text: str) -> str: 
        return re.sub(r'http://.+|https://.+', '', text, flags=re.I)

    # Функция для удаления ссылок markdown 
    def remove_link_markdown(self, text: str) -> str: 
        return re.sub(r'\[\w+\]\(.+\)', ' ', text, flags=re.I)

    # Функция для удаления html-тегов
    def remove_html_tags(self, text: str) -> str: 
        return re.sub(r'(</[a-z]+>|<[a-z]+>)', ' ', text, flags=re.I)

    # Функция для удаления знаков препинания
    def remove_punctuation(self, text: str) -> str: 
        return "".join([ch if ch not in string.punctuation else ' ' for ch in text])

    # Функция для удаления чисел
    def remove_numbers(self, text: str) -> str:
        return ''.join([i if not i.isdigit() else ' ' for i in text])

    # Функция для удаления лишних пробелов
    def remove_multiple_spaces(self, text: str) -> str:
        return re.sub(r'\s+', ' ', text, flags=re.I)

    # Функция для удаления специальных символов
    def remove_othersymbol(self, text: str) -> str:
        return ''.join([ch if ch not in self.special_symbols else ' ' for ch in text])
        
    # Функция для удаления одиночных символов
    def remove_single_symbol(self, text: str) -> str:
        return re.sub(r' [a-zа-яё] ', ' ', text, flags=re.I)
        
    # Функция для удаления стоп слов и лемматизации текста
    def lemmatization_of_text(self, text: str) -> str:
        try:
            tokens = word_tokenize(text)
            tokens = [token for token in tokens if token not in self.russian_stopwords]
            res = list()
            for word in tokens:
                p = self.morph.parse(word)[0]
                res.append(p.normal_form)
            text = " ".join(res)
            return text
        except Exception as e:
            return f'Ошибка: {e}'

    def text_processing(self, text: str) -> str:
        text = text.lower()
        text = self.remove_link_markdown(text)
        text = self.remove_link(text)
        text = self.remove_html_tags(text)
        text = self.remove_punctuation(text)
        text = self.remove_numbers(text)
        text = self.remove_othersymbol(text)
        text = self.remove_single_symbol(text)
        text = self.remove_multiple_spaces(text)
        text = text.strip()
        text = self.lemmatization_of_text(text)
        return text
    
class ParsingDocumentation:
    def get_text_in_word_file(self, path_to_file: str) -> str:
        if (extension:=os.path.splitext(os.path.basename(path_to_file))[1]) != '.doc' and extension != '.docx':
            return None
        doc = Document()
        doc.LoadFromFile(path_to_file)
        text = doc.GetText()
        del doc
        name_file = os.path.basename(path_to_file)
        date_last_modified_file = datetime.fromtimestamp(os.path.getmtime(path_to_file)).strftime("%d-%m-%Y %H:%M")
        return text[71:], name_file, date_last_modified_file
    
    def get_text_in_markdown_file(self, path_to_file: str) -> str:
        if os.path.splitext(os.path.basename(path_to_file))[1] != '.md':
            return None
        with open(path_to_file, 'r', encoding='utf-8') as file:
            text = file.read()
        name_file = os.path.basename(path_to_file)
        date_last_modified_file = datetime.fromtimestamp(os.path.getmtime(path_to_file)).strftime("%d-%m-%Y %H:%M")
        return text, name_file, date_last_modified_file
    
    def get_data_file_on_base64(self, path_file: str) -> base64:
        with open(path_file, 'rb') as file:
            data_bytes = file.read()
            encoded_bytes = base64.b64encode(data_bytes)
            encoded_string = encoded_bytes.decode('utf-8')
        return encoded_string

    def create_dataframe_documentation(self) -> pd.DataFrame:
        dict_data = {
            'name_file' : [],
            'text_file' : [],
            'date_last_modified_file' : [],
        }
        for path in os.listdir(PATH_TO_DOCUMENTATION):
            function_load_data = ''
            extention = os.path.splitext(os.path.basename(path))[1]
            match(extention):
                case ".doc":
                    function_load_data = self.get_text_in_word_file
                
                case ".docx":
                    function_load_data = self.get_text_in_word_file
                
                case ".md":
                    function_load_data = self.get_text_in_markdown_file

            data_file = function_load_data(f'{PATH_TO_DOCUMENTATION}/{path}')
            
            if not data_file:
                continue
            
            dict_data['name_file'].append(data_file[1])
            dict_data['text_file'].append(data_file[0])
            dict_data['date_last_modified_file'].append(data_file[2])

        df = pd.DataFrame(dict_data)
        # df.to_csv('data_from_documentation.csv') Сохранение датасета в файл - отключено
        return df
    
class FindDocumentSimilaritys:
    def __init__(self):
        # Отключение научной степени при выводе
        np.set_printoptions(suppress=True)
        self.vectorizer = self.load_vectorizer()
        self.text_cleaning = TextCleaning()
        self.parsing_text = ParsingDocumentation()
        self.df = ParsingDocumentation().create_dataframe_documentation()
        self.df['text_processing'] = self.df['text_file'].apply(lambda text: self.text_cleaning.text_processing(text))

    def load_vectorizer(self):
        with open(PATH_TO_VECTORIZER, 'rb') as file:
            vectorizer = load(file)
        return vectorizer
    
    def find_document_on_content(self, input_preprocessing_string: str, count_documents: int) -> list[int]:
        input_string_df = pd.DataFrame({'text_processing' : [input_preprocessing_string]})
        concat_df_test = pd.concat([self.df, input_string_df], ignore_index=True)['text_processing']
        tfidf_matrix = self.vectorizer.fit_transform(concat_df_test)
        similarity_matrix = sklearn_cosine(tfidf_matrix)
        cut_similarity_matrix = similarity_matrix[-1][:-1]
        list_max_index_similarity = np.argpartition(cut_similarity_matrix, -1)[-count_documents:][::-1]
        return [int(index) for index in list_max_index_similarity]

    def split_text(self, text: str, distance_len: int) -> list:
        lst = []
        text_tokenize = word_tokenize(text)
        for index_text in range(0, len(text_tokenize) - distance_len + 1, 1):
            lst.append(" ".join(text_tokenize[index_text:index_text+distance_len]))
        return lst

    def find_index_data(self, text_document: str, text_document_preprocessing: str, find_data: str, count_char_out_sent: int = 350):
        start_index_preprocessing = text_document_preprocessing.find(find_data)
        count_other_symbols = (len(text_document) - len(text_document_preprocessing)) * (start_index_preprocessing / len(text_document_preprocessing))
        start_index = round(start_index_preprocessing + count_other_symbols)
        end_index = start_index + count_char_out_sent
        return start_index, end_index
        
    def find_position_on_document(self, index_document: int, input_preprocessing_string: str) -> tuple:
        text_document = self.df.loc[index_document].text_file
        text_document_preprocessing = self.df.loc[index_document].text_processing
        
        lst_split_text = self.split_text(text_document_preprocessing, len(word_tokenize(input_preprocessing_string)))
        lst_split_text.append(input_preprocessing_string)
        
        tfidf_matrix = self.vectorizer.fit_transform(lst_split_text)
        similarity_matrix = sklearn_cosine(tfidf_matrix)
        index_max_similarity = similarity_matrix[-1][:-1].argmax()
        
        return self.find_index_data(text_document, text_document_preprocessing, lst_split_text[index_max_similarity])

    # Функция поиска всех документов и совпадений в них
    def find_documents(self, input_string: str, count_documents: int = 5):
        input_preprocessing_string = self.text_cleaning.text_processing(input_string)
        find_id_documents = self.find_document_on_content(input_preprocessing_string, count_documents)
        list_data_documents = []
        for index in find_id_documents:
            doc = self.df.loc[index]
            start_index, end_index = self.find_position_on_document(index, input_preprocessing_string)
            list_data_documents.append({
                "name_file" : doc.name_file,
                "date_last_modified_file" : doc.date_last_modified_file,
                "find_similarity" : doc.text_file[start_index:end_index],
                "document" : self.parsing_text.get_data_file_on_base64(f'{PATH_TO_DOCUMENTATION}/{doc.name_file}'),
            })
        return list_data_documents