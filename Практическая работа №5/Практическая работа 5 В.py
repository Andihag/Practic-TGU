import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s=Service('C:/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login")
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[1]/div/input").send_keys("test@test.ru")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[2]/div/input").send_keys("123456")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[2]/button").click()
time.sleep(20)

# откроем блок Паспорт
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]").click()

# Фамилия
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Иванов")

# Имя
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Иван")

# Отчество
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Иванович")

# Дата рождения
driver.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div/input").click()
driver.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div/input").clear()
driver.find_element(By.XPATH, "//*[@id='birthday']/div/input").send_keys("25.01.2000")

# Серия
driver.find_element(By.ID, "passportSeries").click()
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("1212")

# Номер
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys("123456")

# Код подразделения
driver.find_element(By.ID, "code").clear()
driver.find_element(By.ID, "code").send_keys("123123")

# СНИЛС
driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").send_keys("12312312312")

# Дата выдачи
driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input").click()
driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input").clear()
driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input").send_keys("25.01.2014")

# Кем выдан
driver.find_element(By.ID, "issued").click()
driver.find_element(By.ID, "issued").clear()
driver.find_element(By.ID, "issued").send_keys("УФМС Адлерского района г.Сочи")

# Адрес
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.CONTROL + "a") # Выделяем весь текст поля
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.DELETE) # Удаляем весь текст поля
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("Краснодарский край, г Сочи, ул Просвещения, д 1")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.ENTER)
time.sleep(2)

# Телефон
driver.find_element(By.ID, "phone").clear()
driver.find_element(By.ID, "phone").send_keys("(1231231212")

# Чек бокс
driver.find_element(By.ID, "privacy").click()
driver.find_element(By.ID, "privacy").click()

# Прикрепление документов
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("C:/ii.jpg")
time.sleep(20)
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div[2]/div[3]/div[9]/button[2]").send_keys(Keys.ENTER)