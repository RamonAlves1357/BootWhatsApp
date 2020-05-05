from selenium import webdriver
import time

class whatsappBoot:
    def __init__(self):
        # Simulando apanes uma mensagem
        self.mensagem = "Bom dia Pessoal!" # Mensagens a ser enviada
        self.grupos = ["Só Recapitulando :leaves::leaves:"] #Grupos/Contatos 

        # Algumas config...
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br') #Adicionando um argumento para o objeto 'options'
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe') # Caminho do WebDriver
        
    def EnviarMensagens(self):
        self.driver.get("https://web.whatsapp.com")
        time.sleep(40)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            
            time.sleep(1)
            chat_box.send_keys(self.mensagem)
            
            botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = whatsappBoot()
bot.EnviarMensagens()