import arrow
from selenium import webdriver
import socket


def HD_Crawl():
    # HardDisk specific data
    installmentPriceProducts = []  # HardDisk Installment Prices
    pricesProducts = []  # HardDisk Prices
    namesProducts = []  # HardDisk Name
    linksProducts = []  # HardDisk Links
    imgProducts = []  # HardDisk Image
    local = arrow.utcnow()  # Scraping date and time
    hostIP = socket.gethostname()  # IP Local
    IPAddr = socket.gethostbyname(hostIP)  # Specif IP
    allData = []  # HardDisk all data

    for i in range(2):
        driver = webdriver.Chrome()
        page = i + 1
        link = 'https://www.pichau.com.br/hardware/hard-disk-e-ssd?page='
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
        if IPAddr == '192.168.2.38':  # Id verification
            product = driver.find_elements('class name', 'jss69')  # Possibles class name = jss191, jss69
            for i in product:
                if 'R$' in i.text:
                    pricesProducts.append(i.text)

            # Crawling Products == Installment Price
            product = driver.find_elements('class name', 'jss77')  # Possibles class name = jss199, jss77
            for i in product:
                if 'R$' in i.text:
                    installmentPriceProducts.append(i.text)

        else:  # Different ID
            # Crawling Products == Price
            product = driver.find_elements('class name', 'jss191')  # Possibles class name = jss191, jss69
            for i in product:
                if 'R$' in i.text:
                    pricesProducts.append(i.text)

            # Crawling Products == Installment Price
            product = driver.find_elements('class name', 'jss199')  # Possibles class name = jss199, jss77
            for i in product:
                if 'R$' in i.text:
                    installmentPriceProducts.append(i.text)

        # Crawling Products == Name
        product = driver.find_elements('tag name', 'h2')
        for i in product:
            if i.text == "":
                continue
            namesProducts.append(i.text)

        # Crawling Products == Links
        links = driver.find_elements('tag name', 'a')
        for i in links:
            if 'hd' in i.get_attribute('href'):
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
                   'Logo': 'https://static.pichau.com.br/logo-pichau-2021-dark.png'}
        allData.append(dataDic)
    return allData
