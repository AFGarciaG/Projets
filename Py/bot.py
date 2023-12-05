from selenium import webdriver
from time import sleep

driver_path = '/ruta/al/driver/chromedriver'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://web.whatsapp.com/")

input("Escanea el código QR y presiona Enter")

numero_destino = "???????????" 
mensaje = "Hola, esto es un mensaje automático desde Python."

url_chat = f"https://web.whatsapp.com/send?phone={numero_destino}&text={mensaje}"

driver.get(url_chat)

sleep(5)

driver.find_element_by_css_selector("span[data-icon='send']").click()

driver.quit()
