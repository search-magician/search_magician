from selenium import webdriver
import time

#CONSTANTS
OTHER_VIDS = 'https://www.youtube.com/watch?v='
ID_LEN = 11
OTHER_VIDS_LEN = len(OTHER_VIDS)

def main(VIDEO_ID):

    driver = webdriver.Firefox()
    URL = 'https://www.youtube.com/watch?v=' + VIDEO_ID
    driver.get(URL)

    #TODO : Change next line and implement better waiting handler ,
    # the next line is to wait for the website to load all of its components
    time.sleep(5)

    continue_link = driver.find_element_by_tag_name('a')
    elems = driver.find_elements_by_xpath("//a[@href]")

    ret = []
    for elem in elems:
        res = str(elem.get_attribute("href"))
        videoId = res[OTHER_VIDS_LEN:OTHER_VIDS_LEN + ID_LEN]
        if OTHER_VIDS in res:
            ret.append(videoId)

    driver.quit()
    return ret
