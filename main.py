from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os


load_dotenv()



chrome_configurations = webdriver.ChromeOptions()
chrome_configurations.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_configurations)
driver.get("https://tinder.com/")
sleep(1)
driver.find_element(By.XPATH, '//*[@id="s1592971809"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]').click() # INCIAR SECCION
sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="s-135409267"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click() # FACEBOOK

main = driver.current_window_handle

for new_window in driver.window_handles:
    if new_window != main:
        driver.switch_to.window(new_window)
        break

driver.find_element(By.ID, "email").click()
driver.find_element(By.ID, "email").send_keys(os.environ.get("EMAIL"))
sleep(0.2)
driver.find_element(By.ID, "pass").click()
driver.find_element(By.ID, "pass").send_keys(os.environ.get("CONTRA"))
sleep(0.2)
driver.find_element(By.ID, "loginbutton").click()
sleep(3)
driver.close()
driver.switch_to.window(main)
sleep(3)


cookies = driver.find_element(By.XPATH, '//*[@id="s-135409267"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()
location = driver.find_element(By.XPATH, '//*[@id="s-135409267"]/div/div[1]/div/div/div[3]/button[1]')
location.click()
notificacion = driver.find_element(By.XPATH, '//*[@id="s-135409267"]/div/div/div/div/div[3]/button[1]')
notificacion.click()

##### DAR LIKE

for i in range(30):
    sleep(1)
    try:
        print("DENTRO DEL LLOOOOPP de mi looop")
        driver.find_element(By.XPATH, '//*[@id="s1592971809"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button').click()
    except NoSuchElementException:
        sleep(2)
        print("Aun no esta tu boton de like")
    except ElementClickInterceptedException:
        '''Aqui esta expecion me maneja cuando tengo un match entonces lo que realizo es 
        es selecciono y le doy en con BACK TO TINDER 
        '''
    else:
        sleep(2)
