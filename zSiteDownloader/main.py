from selenium import webdriver
from selenium.webdriver.common.by import By
import os,sys, time, requests, random
from prettyprinter import pprint


def download_image(url, save_as):

    # download image an save in current work dir
    res = requests.get(url, stream=True)

    # Output total file size
    total_size = int(res.headers.get('content-length', 0))
    total_size_kb = round(total_size/1024, 2)

    # Download info:
    print(f"Downloading - {os.path.basename(save_as)}")
    print(f"File size - {total_size_kb}kb")


    done = downloaded = 0
    with open(save_as, 'wb') as file:

        # iterate over content to download
        chunk_size = int(total_size/100)
        for data in res.iter_content(chunk_size=chunk_size):
            file.write(data)
            downloaded += chunk_size
            done += 1

            # print download progress
            progress =f"[{'='*(int(done/2))}|({done}%){round(downloaded/1024, 2)}/{total_size_kb}]" 
            print(progress, end="\r")
            

            # Download is complete
            if downloaded >= total_size:
                done = 100
                progress =f"[{'='*(int(done/2))}|({done}%){total_size_kb}/{total_size_kb}kb]" 
                print(progress)

def download_from_site(save_to_dir):

    for page in page_data:

        comic_page_link = page['link']
        title = page['title']

        # load the new page
        driver.get(comic_page_link)
        time.sleep(2)

        # create directory in pictures folder
        comic_name = comic_page_link.split("/")[-2]

        # get img path online
        img_path = driver.find_element(By.CSS_SELECTOR, value=".photo img").get_attribute("src")

        # create directory if not already existing
        if not os.path.isdir(save_to_dir):
            os.makedirs(save_to_dir)

        # download image to new folder
        download_image(img_path, f"{save_to_dir}/{comic_name}-{title}.jpg")

        # Wait a little for going to next page
        time.sleep(random.randint(1, 6))



chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrom_options)

comic_page = "https://comics.8muses.com/comics/album/Hentai-and-Manga-English/Mosquito-Man/Yabai-yo-Bakunyuu-Yankee-Musume-Ricchan-Oh-God-My-Delinquent-Daughter-Ricchan-Has-Huge-Tits"
driver.get(comic_page)

page_list = driver.find_elements(By.CLASS_NAME , "c-tile")

print("\n".join([str({"title": page.get_attribute('title'), "link":page.get_attribute('href')}) for page in page_list]))
page_data = [{"title": page.get_attribute('title'), "link":page.get_attribute('href')} for page in page_list]

res = input("Do you want to continue? y/n : ")

if res == 'n' or res == 'N':
    driver.quit()

else :
    # create directory in pictures folder
    comic_page_link = comic_page
    comic_page_directories = comic_page_link.split("/")[5:] # Get necessary directory
    site_name = "8muses"
    comic_folder = f"C:/Users/adegb/Pictures/{site_name}/{'/'.join(comic_page_directories)}"

    download_from_site(save_to_dir=comic_folder)
        

    print(f"All {len(page_list)} pages succefully downloaded ")

    driver.quit()






