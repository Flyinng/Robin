import arrow
from selenium import webdriver
import socket


def SSD_Crawl():
    # SSD specific data

    installmentPriceProducts = []           # SSD Installment Prices
    pricesProducts = []                     # SSD Prices
    namesProducts = []                      # SSD Name
    linksProducts = []                      # SSD Links
    imgProducts = []                        # SSD Image
    local = arrow.utcnow()                  # Scraping date and time
    hostIP = socket.gethostname()           # IP Local
    IPAddr = socket.gethostbyname(hostIP)   # Specif IP
    allData = []                            # SSD all data

    for i in range(6):
        driver = webdriver.Chrome()
        page = i + 1
        link = 'https://www.pichau.com.br/hardware/ssd?page='
        new_link = link + str(page)
        driver.get(new_link)
        height = driver.execute_script("return document.body.scrollHeight")
        scroll = 0
        driver.fullscreen_window()

        # Crawling Products == Image
        product = driver.find_elements('tag name', 'img')
        for e in product:
            if 'product' in e.get_attribute('src'):  # Only separate images with product in the name
                imgProducts.append(e.get_attribute('src'))
        while scroll < height:
            driver.execute_script(f"window.scrollTo(0, {scroll});")
            product = driver.find_elements('tag name', 'img')
            for e in product:
                if 'product' in e.get_attribute('src'):  # Only separate images with product in the name
                    imgProducts.append(e.get_attribute('src'))
            scroll += 200
        imgProducts = list(dict.fromkeys(imgProducts))

        # Crawling Products == Price
        priceTag = 0
        product = []
        priceTagList = ['jss201', 'jss213', 'jss191', 'jss191', 'jss201']
        while len(product) == 0:
            product = driver.find_elements('class name', priceTagList[priceTag])
            priceTag += 1
            for i in product:
                if 'R$' in i.text:
                    pricesProducts.append(i.text)

        # Crawling Products == Installment Price
        priceTag = 0
        product = []
        priceTagList = ['jss209', 'jss221', 'jss199', 'jss199', 'jss209']
        while len(product) == 0:
            product = driver.find_elements('class name', priceTagList[priceTag])
            priceTag += 1
            for i in product:
                if 'R$' in i.text:
                    installmentPriceProducts.append(i.text)

        # Crawling Products == Name
        product = driver.find_elements('tag name', 'h2')
        for i in product:
            j = i.text.replace('"', '')
            namesProducts.append(j)

        # Crawling Products == Links
        links = driver.find_elements('tag name', 'a')
        for i in links:
            if 'ssd-' in i.get_attribute('href'):
                linksProducts.append(i.get_attribute('href'))
        driver.close()

    # Separating data in dictionary for better reading
    for i in range(len(installmentPriceProducts)):
        if '.' in pricesProducts[i]:
            pricesProducts[i] = pricesProducts[i].replace('.', '')
        changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
        if '.' in installmentPriceProducts[i]:
            installmentPriceProducts[i] = installmentPriceProducts[i].replace('.', '')
        changeableInstallmentPriceProducts = installmentPriceProducts[i].replace('R$', '').replace(',', '.')
        dataDic = {'Store': 'Pichau', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
                   'Installment price': [installmentPriceProducts[i], float(changeableInstallmentPriceProducts)],
                   'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
                   'Logo': 'https://static.pichau.com.br/logo-pichau-2021-dark.png', 'Type': 'SSD',  'Model': '', 'Format': '',
                   'Interface': '', 'Capacity': '', 'DDR': '', 'Frequency': '', 'Platform': '', 'Color': ''}
        allData.append(dataDic)
    return allData