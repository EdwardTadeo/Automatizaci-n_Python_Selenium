from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time

chrome_driver_path = 'chromedriver'
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://prueba-bolsas.krowdy.net/"
driver.get(url) 
ingresar = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/button[3]' ) 
ingresar.click()

correo = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/div/input')
correo.send_keys("test1.krowdy@gmail.com")

ingresar_correo = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/button')
ingresar_correo.click()

contraseña = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/input')
time.sleep(2)
contraseña.send_keys("krowders")

ingresar_contraseña = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/button')
ingresar_contraseña.click()

time.sleep(2)
acceder = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/a')
acceder.click()

time.sleep(2)
search = driver.find_element(By.XPATH,'//*[@id="root"]/main/div[1]/div/div[2]/div/div/div/input' ) 
search.send_keys("aviso")
buscar = driver.find_element(By.XPATH,'//*[@id="root"]/main/div[1]/div/div[2]/button')
buscar.click()

time.sleep(2)
ver_postulacion = driver.find_element(By.XPATH,'//*[@id="root"]/main/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[1]/button')
ver_postulacion.click()
input("------------------Ejecución Completada-----------------")