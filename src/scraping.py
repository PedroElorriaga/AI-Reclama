import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd

company_url = input('Insira a url da empresa Reclame Aqui '
                    'Ex. (https://www.reclameaqui.com.br/empresa/nome_empresa/lista-reclamacoes/):   ')

# SETTING WEBDRIVER
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options)


# GETTING PAGE
if 'www.reclameaqui.com.br' in company_url:
    driver.get(company_url)
else:
    print('A URL não corresponde ao site do Reclame Aqui, insira algo como'
          '(https://www.reclameaqui.com.br/empresa/nome_empresa/lista-reclamacoes/): ')
    raise Exception('Desculpe, URL inválida')

# GET ALL COMMENTS (ONLY ONE SECTION)
span_comment_section = []
try:
    contanier_comment = driver.find_element(
        By.XPATH, '//*[@id="__next"]/div[3]/div/div/main/section[2]/div[2]/div[2]')
    span_comment_section = contanier_comment.find_element(
        By.CLASS_NAME, 'sc-fAGzit').text.split(' ')
except:
    print('Element not found')

max_section = int(span_comment_section[2]) if span_comment_section else 0

# HANDLING EACH COMMENT
comments_object = []


def handle_comments():
    div_comments_array = contanier_comment.find_elements(
        By.CLASS_NAME, 'sc-1pe7b5t-0')

    for comment in div_comments_array:
        a_title_comment = comment.find_element(By.TAG_NAME, 'a')
        p_content_comment = comment.find_element(By.TAG_NAME, 'p')
        span_contents_comment = comment.find_elements(By.TAG_NAME, 'span')

        # SCROLL TO COMMENT
        driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", div_comments_array[::-1][0])
        time.sleep(1)
        comments_object.append(
            {
                "titulo": a_title_comment.text,
                "conteudo": p_content_comment.text,
                "resposta": False if span_contents_comment[0].text == 'Não respondida' else True,
                "data": span_contents_comment[1].text
            }
        )


if max_section > 50:
    actual_section = 0
    while actual_section < 50:
        handle_comments()
        actual_section += 1
        button_foward_section = contanier_comment.find_elements(
            By.TAG_NAME, 'button')[2]
        button_foward_section.click()
elif max_section > 0:
    actual_section = 0
    while actual_section < max_section:
        handle_comments()
        button_foward_section = contanier_comment.find_elements(
            By.TAG_NAME, 'button')[2]
        actual_section += 1
        button_foward_section.click()
else:
    handle_comments()

# HANDLE WITH DATAFRAMES
df_comments = pd.DataFrame(comments_object)
df_comments.to_csv('./data/raw/reclamacoes.csv',
                   index=False, encoding='utf-8')

print('Scraping realizado com sucesso!')
driver.close()
driver.quit()
