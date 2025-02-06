import pandas as pd
import re
import os

data = 'data/companies_sorted.csv' # https://www.kaggle.com/datasets/peopledatalabssf/free-7-million-company-dataset
output = 'data/company_names.txt'


def looks_natural(word):
    # Handle non-string types
    if not isinstance(word, str):
        return False
    word = word.strip()
    
    # Rest of function remains same
    if not any(c in word for c in 'aeiou'):
        return False
    consonants = 'bcdfghjklmnpqrstvwxz'
    for i in range(len(word)-2):
        if all(word[j] in consonants for j in range(i, i+3)):
            return False
    consonant_count = sum(1 for c in word if c in consonants)
    if consonant_count / len(word) > 0.7:
        return False
    return True


if not os.path.exists(output):
    df = pd.read_csv(data)
    company_names = df['name'].drop_duplicates()
    filtered_companies = company_names[
    (company_names.str.split().str.len() == 1) &
    (company_names.str.match('^[a-z0-9]+$')) &
    (company_names.str.len().between(5, 9)) &
    (company_names.apply(looks_natural))
    ]
    filtered_companies.to_csv(output, index=False, header=False)
