from selenium import webdriver  # 用来驱动浏览器的
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.support import expected_conditions as EC  # 和下面WebDriverWait一起用的

path = "E:\dirver\msedgedriver.exe"
EDGE = {
    "browserName": "MicrosoftEdge",
    "version": "",
    "platform": "WINDOWS",
    # 关键是下面这个
    "ms:edgeOptions": {
        'extensions': [],
        'args': [
            '--headless',
            '--disable-gpu',
            '--remote-debugging-port=9515',
        ]}
}
driver = webdriver.Edge(executable_path=path, capabilities=EDGE)

# driver = webdriver.PhantomJS()
driver.get("https://www.baidu.com")

input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#banner_link > div > div > form > input")))

submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="banner_link"]/div/div/form/button')))
