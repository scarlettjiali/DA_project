def get_product(asin):
    import requests
    from bs4 import BeautifulSoup
    product_detail = dict()
    product_result = dict()
    url = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + asin
    response = requests.get(url)
    if not response.status_code == 200:
        print(response.status_code)
        return None
    try:
        results_page = BeautifulSoup(response.content,'lxml')
        product_result['product_name'] = results_page.find('h2').get_text()
        detail_url = results_page.find('a', class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal").get('href')
        response1 = requests.get(detail_url)
        if not response1.status_code == 200:
            print(response1.status_code)
            return None
        try:
            results_page1 = BeautifulSoup(response1.content,'lxml')
            detail_code = results_page1.find('div', class_ = 'content').find('ul').find_all('li')
            product_result['product_fig'] = results_page1.find('img',alt = product_result['product_name']).get('src')
            product_result['product_author'] = results_page1.find('a',id ="ProductInfoArtistLink").get_text()
            for detail in detail_code:
                try:
                    detail_name = detail.find('strong').get_text()
                    detail_self = detail.get_text()
                    product_detail[detail_name] = detail_self
                except:
                    pass
        except:
            pass
        product_result['product_detail'] = product_detail
        return product_result
    except:
        return None