import arrow
from selenium import webdriver


def SSD_Crawl():
    # SSD specific data

    pricesProducts = []             # SSD Prices
    namesProducts = []              # SSD Name
    linksProducts = []              # SSD Links
    imgProducts = []                # SSD Image
    local = arrow.utcnow()          # Scraping date and time
    allData = []                    # SSD all data

    for i in range(1, 4):
        driver = webdriver.Chrome()
        link = f'https://www.kabum.com.br/hardware/ssd-2-5/ssd-pcie-nvme?page_number={i}&page_size=100&facet_filters=&sort=most_searched'
        driver.get(link)

        # Crawling Products == Image
        product = driver.find_elements('class name', 'imageCard')
        for e in product:
            imgProducts.append(e.get_attribute('src'))

        # Crawling Products == Price
        product = driver.find_elements('class name', 'priceCard')  # Possibles class name = jss191, jss69, jss64, jss201
        for i in product:
            if ',' in i.text:
                pricesProducts.append(i.text)

        # Crawling Products == Name
        product = driver.find_elements('class name', 'nameCard')
        for i in product:
            j = i.text.replace('"', '')
            namesProducts.append(j)

        # Crawling Products == Links
        links = driver.find_elements('tag name', 'a')
        for i in links:
            if i.get_attribute('href') is None:
                continue
            if 'produto' in i.get_attribute('href'):  # Only separate images with product in the name
                linksProducts.append(i.get_attribute('href'))
        driver.close()

    # Separating data in dictionary for better reading
    linksProducts = list(dict.fromkeys(linksProducts))
    for i in range(len(pricesProducts)):
        if '.' in pricesProducts[i]:
            pricesProducts[i] = pricesProducts[i].replace('.', '')
        changeablePrices = pricesProducts[i].replace('R$', '').replace(',', '.')
        dataDic = {'Store': 'Kabum', 'Name': namesProducts[i], 'Price': [pricesProducts[i], float(changeablePrices)],
                   'Installment price': [0, 0],
                   'Link': linksProducts[i], 'Image': imgProducts[i], 'Time': local.format('YYYY-MM-DD HH:mm:ss'),
                   'Logo': 'https://logodownload.org/wp-content/uploads/2017/11/kabum-logo.png', 'Type': 'SSD','Model': '', 'Format': '',
                   'Discount': '', 'Old Prices': '',
                   'Interface': '', 'Capacity': '', 'DDR': '', 'Frequency': '', 'Platform': '', 'Color': ''}
        allData.append(dataDic)
    return allData
