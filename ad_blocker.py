from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def ad_blocker_coopang(keyword):

    options = Options()
    browser = webdriver.Chrome(options=options)

    base_url = "https://www.coupang.com/np/search?component"
    search_term = keyword

    browser.get(f"{base_url}=&q={search_term}&channel=user")

    soup = BeautifulSoup(browser.page_source, "html.parser")

    search_product_list = soup.find("ul", class_="search-product-list")

    filtered_products = [ product for product in search_product_list.find_all('li', recursive=False) if 'search-product__ad-badge' not in product['class'] ]


    results = []

    for i in range(len(filtered_products)):

        # brand_name, product_name
        s = filtered_products[i].select_one('.name').string
        split_result = s.split(' ', 1)  # 첫 번째 공백을 기준으로 문자열 분리
        brand_name = split_result[0]
        product_name = split_result[1]

        # link
        anchor = filtered_products[i].find('a')

        product_data = {

            'img_link' : 'https:'+filtered_products[i].select_one('.search-product-wrap-img')['src'],
            'brand' : brand_name,
            'name' : product_name.replace(",", ""),
            'price': int(filtered_products[i].select_one('.price-value').string.replace(",", "")),
            'link' : 'https://www.coupang.com/'+anchor['href']
        }

        results.append(product_data)
    
    return results
