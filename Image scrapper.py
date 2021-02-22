import requests
import os
from selenium import webdriver
import time


def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=0.5):
    def scroll_to_end(wd, scroll_point):  
        wd.execute_script(f"window.scrollTo(0, {scroll_point});")
        time.sleep(sleep_between_interactions)    
 
        
    # build the unsplash query
    search_url = f"https://unsplash.com/s/photos/{query}"
# load the page
    wd.get(search_url)
    time.sleep(sleep_between_interactions)  
    
    image_urls = set()
    image_count = 0
    results_start= 0
    
    for i in range(1,20):
        scroll_to_end(wd, i*1000)
        time.sleep(0.5)
        thumb = wd.find_elements_by_css_selector("img._2UpQX")
        number_results=len(thumb)
        time.sleep(0.5)
        for img in thumb[results_start:number_results]:
            image_urls.add(img.get_attribute('src'))
            image_count = len(image_urls)
            time.sleep(.5)
            if image_count>=max_links_to_fetch:
                print(f'Found: {len(image_urls)} image links, done!')
                break
        else:
            continue
        results_start=len(thumb)
        break
    return image_urls

def persist_image(folder_path:str,url:str,counter):
    try:
        image_content = requests.get(url).content
        
    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")
    try:
        f=open(os.path.join(folder_path,'jpg'+'_'+str(counter)+'.jpg'),'wb')
        f.write(image_content)
        f.close()
        print(f'SUCCESS- saved {url}-as {folder_path}')
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")

def search_and_download(search_term:str,driver_path:str,target_path='./images',number_images=30):
    target_folder = os.path.join(target_path,'_'.join(search_term.lower().split(' ')))
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)
    counter=131
    for elem in res:
        persist_image(target_folder,elem,counter)
        counter+=1

DRIVER_PATH='./chromedriver'
search_term='man'
search_and_download(search_term,DRIVER_PATH)