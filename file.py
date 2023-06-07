def save_to_file(keyword,products):

    file = open(f"{keyword}.csv", "w",encoding="utf-8-sig")

    # 파일에 헤더 입력 , \n
    file.write("Image,Brand,Name,Price,URL\n")


    for product in products:
        file.write(f"{product['img_link']},{product['brand']},{product['name']},{product['price']},{product['link']}\n")

    file.close()


        
