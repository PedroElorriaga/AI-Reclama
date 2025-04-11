import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd

# SETTING WEBDRIVER
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options)


# GETTING PAGE
driver.get('https://www.reclameaqui.com.br/empresa/nubank/lista-reclamacoes/')

# GET ALL COMMENTS (ONLY ONE SECTION)
contanier_comment = driver.find_element(
    By.XPATH, '//*[@id="__next"]/div[3]/div/div/main/section[2]/div[2]/div[2]')
div_comments_array = contanier_comment.find_elements(
    By.CLASS_NAME, 'sc-1pe7b5t-0')

# HANDLING EACH COMMENT
comments_object = []
for comment in div_comments_array:
    a_title_comment = comment.find_element(By.TAG_NAME, 'a')
    p_content_comment = comment.find_element(By.TAG_NAME, 'p')
    span_contents_comment = comment.find_elements(By.TAG_NAME, 'span')

    # SCROLL TO COMMENT
    driver.execute_script(
        "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", a_title_comment)
    time.sleep(1.5)
    comments_object.append(
        {
            "titulo": a_title_comment.text,
            "conteudo": p_content_comment.text,
            "resposta": False if span_contents_comment[0].text == 'Não respondida' else True,
            "data": span_contents_comment[1].text
        }
    )

# HANDLE WITH DATAFRAMES
df_comments = pd.DataFrame(comments_object)
df_comments.to_csv('data/raw/reclamacoes.csv',
                   index=False, encoding='utf-8')

print('Scraping realizado com sucesso!')
driver.close()
driver.quit()
