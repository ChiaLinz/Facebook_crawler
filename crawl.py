import pandas as pd
import re, time, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


def FindLinks(url):
    Links = []
    driver.get(url)
    pos = []
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"]'))
        WebDriverWait(driver, 10).until(element_present)
        print("Page loaded successfully!")
    except TimeoutException:
        print("Timed out waiting for page to load.")
    time.sleep(3)

    children = driver.find_element(By.XPATH, '//*[@aria-label="關閉"]')
    children.click()
    time.sleep(2)
    

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)
    #driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #time.sleep(2)
    driver.execute_script('window.scrollTo(0, 0);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    driver.execute_script('window.scrollTo(0, 0);')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)
    allPostElements = driver.find_elements(By.XPATH, '//*[@class="x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"]')


    idx = 0
    for element in allPostElements:
        
        Links.append(element)
        #ele:WebElement = i
    
        #Gain x, y positions
        ele_location = element.location
        x = ele_location["x"]
        y = ele_location["y"]


        
        pos.append({"x": x, "y": y})
        idx = idx + 1
    return Links, pos


def open_new_page(driver, y_position, target_xpath):
    try:
        # find target element
        target_elements = driver.find_elements(By.XPATH, target_xpath)
        
        # locate href link in selected y area
        for target_element in target_elements:
            ele_location = target_element.location
            if y_position - 50 <= ele_location["y"] <= y_position + 50:  
                # get href element
                href = target_element.get_attribute("href")
                
                # click href
                driver.get(href)
                time.sleep(1)
                
                try:
                    # wait for close botton
                    time.sleep(3)
                    close_button_present = EC.presence_of_element_located((By.XPATH, '//*[@aria-label="關閉"]'))
                    WebDriverWait(driver, 10).until(close_button_present)
                    
                    # close the window
                    children = driver.find_element(By.XPATH, '//*[@aria-label="關閉"]')
                    children.click()
                    time.sleep(2)
                except:
                    print("No window need to be closed")
                break  

    except Exception as e:
        print("Error:", str(e))

def back_origin_page():
    try:
        # return last page
        driver.back()
        time.sleep(5)  # wait for page loaded
        

        
        children = driver.find_element(By.XPATH, '//*[@aria-label="關閉"]')
        children.click()
        time.sleep(2)

        


    except Exception as e:
        print("Error:", str(e))


def expand_img_post():
    time.sleep(2)
    max_scroll_attempts = 5  
    scroll_attempts = 0
    totalCount = 0
    

    while scroll_attempts < max_scroll_attempts:
        try:
            dialog = driver.find_element(By.XPATH, '//*[@class="x1n2onr6 x1ja2u2z x1afcbsf xdt5ytf x1a2a7pz x71s49j x1qjc9v5 x1qpq9i9 xdney7k xu5ydu1 xt3gfkd x78zum5 x1plvlek xryxfnj xcatxm7 xrgej4m xh8yej3"]')
        except:
            dialog = driver
            
        
        driver.execute_script("window.scrollTo(1300, document.body.scrollHeight);")
        time.sleep(2)

        found_new_content = False  # check if find new botton

        for i in dialog.find_elements(By.XPATH, '//*[@class="x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa"]'):
           # Repeatedly detect whether there are buttons such as "See more comments", "See more replies" and "See the complete post content", and click if there are any.
            if bool(re.search('顯示更多', i.text)) or bool(re.search('查看更多留言', i.text)) or bool(re.search('回覆', i.text)) or bool(re.search('查看', i.text)) or bool(re.search('檢視', i.text)) or bool(re.search('查看更多', i.text)):
                try:
                    i.click()
                    totalCount += 1
                    found_new_content = True  
                except:
                    pass

        if not found_new_content:
            scroll_attempts += 1  #If no new content is found, increase the number of swipe attempts
        else:
            scroll_attempts = 0  
        
        driver.execute_script("window.scrollTo(0, 0);")


def expand_v_post():
    time.sleep(2)

    try:
        
        elements = driver.find_elements(By.XPATH, '//*[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"]')

        
        target_element = elements[1]
        time.sleep(2)
        
        target_element.click()
        time.sleep(2)
        scroll_height = 300
        driver.execute_script(f'window.scrollTo(0, {scroll_height});')
        parent_element = driver.find_element(By.XPATH, '//*[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"]')

        
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", parent_element)

        time.sleep(2)  
        
        totalCount = 0
        max_scroll_attempts = 5
        scroll_attempts = 0

        while scroll_attempts < max_scroll_attempts:
            found_new_content = False
            
            for i in parent_element.find_elements(By.XPATH, '//*[@class="x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa"]'):
                
                if bool(re.search('顯示更多', i.text)) or bool(re.search('查看更多留言', i.text)) or bool(re.search('回覆', i.text)) or bool(re.search('查看', i.text)) or bool(re.search('檢視', i.text)) or bool(re.search('查看更多', i.text)):
                    try:
                        i.click()
                        totalCount += 1
                        found_new_content = True  
                    except:
                        pass

            if not found_new_content:
                scroll_attempts += 1
            else:
                scroll_attempts = 0

           
            driver.execute_script("arguments[0].scrollTop = 0;", parent_element)
            time.sleep(2)
    
    except Exception as e:
        print("Error:", str(e))








def PostContent_img(soup):
    
    userContent = soup.find('div', {'class':'x1n2onr6 x1ja2u2z'})
    if userContent is None:
        print("Empty Dataframe")
        return pd.DataFrame()  
        

    
    try:
        PosterInfo = userContent.find('div', {'class':'x1cy8zhl x78zum5 x1q0g3np xod5an3 x1pi30zi x1swvt13 xz9dl7a'})
        ImageInfo = PosterInfo.find('object')
        
        Name = "雨揚樂活家族"
        try:
            ID = userContent.find('div', {'class':'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a'}).text 
            ID = ID[:15] 
        except:    
            ID = None
    except:
        return pd.DataFrame() 
    # url
    Link = driver.current_url
    # post info
    try:
        Time = PosterInfo.find('abbr').attrs['title']
    except:
        Time = PosterInfo.find('span', {'class':'x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j'}).text
    # Content
    try:
        FirstContent = userContent.find('div', {'class':'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a'}).text        
    except:
        FirstContent = ""
    
    all_more_content_divs = userContent.find_all('div', {'class':'x11i5rnm xat24cr x1mh8g0r x1vvkbs xtlvy1s x126k92a'})
    MoreContent = ''.join(div.text for div in all_more_content_divs)

    Content = FirstContent + MoreContent

    # Like
    try:
        all_spans_with_class = userContent.find_all('span', class_='x1e558r4')
        spans_with_only_this_class = [span for span in all_spans_with_class if span.attrs['class'] == ['x1e558r4']]
        if spans_with_only_this_class:
            Like = spans_with_only_this_class[0].text
        else:
            Like = '0'
    except:
        Like = '0' 

    # Comment
    try:
        comment_span = userContent.find('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa')
        match = re.search(r'(\d+)', comment_span.text)        
        if match: 
            commentcount = match.group(1)  
        else:
            commentcount = '0'
    except:
        commentcount = '0' 
    # share
    try:
        share_span = userContent.find_all('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa')
        # select second element
        if len(share_span) >= 2:
            share_span = share_span[1]
        else:
            raise ValueError("Not enough matching elements found.")  
        match = re.search(r'(\d+)', share_span.text)        
        if match:  
            sharecount = match.group(1)  
        else:
            sharecount = '0'
    except:
        sharecount = '0' 
    viewcount = "0"
    return pd.DataFrame(
        data = [{'Name':Name,
                 'ID':ID,
                 'Link':Link,
                 'Time':Time,
                 'Content':Content,
                 'Like':Like,
                 'Commentcount':commentcount,
                 'Share':sharecount,
                 'Viewcount':viewcount}],
        columns = ['Name', 'ID', 'Time', 'Content', 'Like', 'Commentcount', 'Share', 'Viewcount', 'Link'])


# Comment
def CrawlComment_img(soup, postID):
    Comments = pd.DataFrame()
    # Comments
    userContent = soup.find('div', {'class':'x2bj2ny x12nagc'})

    if not userContent:
        userContent = soup.find('div', {'class':'x1n2onr6 x1ja2u2z'})
    
    commentCount = 0
    commentAll = userContent.findAll('div', {'x1n2onr6 x1iorvi4 x4uap5 x18d9i69 x1swvt13 x78zum5 x1q0g3np x1a2a7pz'})
    for i in commentAll:
        try:
            CommentContent = i.find('div', {'class':'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs'}).text
        except:
            CommentContent = 'Sticker'
        
        commentName = i.find('span', {'class':'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u'}).text
        timeBlock = i.find('li', {'class':'x1rg5ohu x1emribx x1i64zmx'})
        commentTime = timeBlock.find('span', {'class':'x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j'}).text        
        link_element = i.find('a', {'class':'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa xo1l8bm'})
        c_link = link_element["href"]
        Comment = pd.DataFrame(data = [
                                {'PostID':postID,
                                 'CommentName':commentName,
                                 'CommentTime':commentTime,
                                 'CommentContent':CommentContent,
                                 'Link':c_link}],
                        columns = ['PostID','CommentName', 'CommentTime', 'CommentContent', 'Link'])
        Comments = pd.concat([Comments, Comment], ignore_index=True)
        commentCount += 1
        
    # Reply on comments
    replyCount = 0
    userContent = soup.find('div', {'class':'x2bj2ny x12nagc'})
    for i in userContent.findAll('div', {'class':'x1n2onr6 x1iorvi4 x4uap5 x18d9i69 xurb0ha x78zum5 x1q0g3np x1a2a7pz'}):
        try:
            reply_CommentContent = i.find('div', {'class':'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs'}).text
        except:
            reply_CommentContent = 'Sticker'
        
        reply_commentID = ""
        reply_commentName = i.find('span', {'class':'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u'}).text
        reply_commentTime = i.find('span', {'class':'x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j'}).text
        r_link_element = i.find('a', {'class':'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa xo1l8bm'})
        r_link = r_link_element["href"]
        reply_Comment = pd.DataFrame(data = [
                                { 'PostID':postID,
                                 'CommentID':reply_commentID,
                                 'CommentName':reply_commentName,
                                 'CommentTime':reply_commentTime,
                                 'CommentContent':reply_CommentContent,
                                 'Link':r_link}],
                        columns = ['PostID','CommentID', 'CommentName', 'CommentTime', 'CommentContent', 'Link'])
        Comments = pd.concat([Comments, reply_Comment], ignore_index=True)
        replyCount += 1
    print(f"CommentCount:{commentCount}, ReplyCount:{replyCount}")        
    return Comments



def PostContent_v(soup):
    
    userContent = soup.find('div', {'class':'x1jx94hy x78zum5 x5yr21d'})
    if userContent is None:
        print("Empty Dataframe")
        return pd.DataFrame()  
        
   
    try:
        PosterInfo = userContent.find('div', {'class':'x78zum5 x1q0g3np'})
        Name = "雨揚樂活家族"
        ID_element = userContent.find('div' , {'class':'x78zum5 xdt5ytf x4cne27 xifccgj'})
        try:
            ID = ID_element.find('span', {'class':'x1lliihq x6ikm8r x10wlt62 x1n2onr6'}).text
            ID = ID[:15] 
        except:
            pass

        try:
            ID = ID_element.find('span', {'class':'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'}).text
        except:
            pass
        
    except:
        return pd.DataFrame()  
    
    Link = driver.current_url
    
    try:
        Time = PosterInfo.find('abbr').attrs['title']
    except:
        Time = PosterInfo.find('span', {'class':'x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j'}).text
    
    try:
        FirstContent = userContent.find('div', {'class':'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs'}).text        
    except:
        FirstContent = ""
    
    all_more_content_divs = userContent.find_all('div', {'class':'x11i5rnm xat24cr x1mh8g0r x1vvkbs xtlvy1s'})
    MoreContent = ''.join(div.text for div in all_more_content_divs)

    Content = FirstContent + MoreContent

    # Like
    try:
        parent_span = userContent.find('span', class_='x6ikm8r x10wlt62 xlyipyv')
        if parent_span:
            like_span = parent_span.find('span', class_='x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j')
            if like_span:
                Like = like_span.text
            else:
                Like = '0'
        else:
            Like = '0'
    except:
        Like = '0'

    # 留言
    try:
        comment_span = userContent.find('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa xo1l8bm xi81zsa')
        match = re.search(r'(\d+)', comment_span.text)
        if match:  
            commentcount = match.group(1)  
        else:
            commentcount = '0'
    except:
        commentcount = '0' 

    #Number of views
    try:
        view_span = userContent.find_all('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa xo1l8bm xi81zsa')
        if len(view_span) >= 2:
            view_span = view_span[1]
        else:
            raise ValueError("Not enough matching elements found.")
        match = re.search(r'([\d,]+)', view_span.text)
        if match:  
            viewcount = match.group(1).replace(',', '')  
        else:
            viewcount = '0'
    except:
        viewcount = '0' 
    share = '0'
    return pd.DataFrame(
        data = [{'Name':Name,
                 'ID':ID,
                 'Link':Link,
                 'Time':Time,
                 'Content':Content,
                 'Like':Like,
                 'Commentcount':commentcount,
                 'Share':share,
                 'Viewcount':viewcount}],
        columns = ['Name', 'ID', 'Time', 'Content', 'Like', 'Commentcount', 'Share', 'Viewcount', 'Link'])
    


def CrawlComment_v(soup, postID):
    Comments = pd.DataFrame()
    
    userContent = soup.find('div', {'class':'x1n2onr6 x1vjfegm x1iyjqo2 x1odjw0f'})
    if not userContent:
        return Comments
    
    commentCount = 0
    commentAll = userContent.findAll('div', {'x1n2onr6 x1iorvi4 x4uap5 x18d9i69 x1swvt13 x78zum5 x1q0g3np x1a2a7pz'})
    for i in commentAll:
        try:
            CommentContent = i.find('div', {'class':'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs'}).text
        except:
            CommentContent = 'Sticker'
        
        commentID = ""
        commentName = i.find('span', {'class':'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u'}).text
        timeBlock = i.find('li', {'class':'x1rg5ohu x1emribx x1i64zmx'})
        commentTime = timeBlock.find('span', {'class':'x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j'}).text
        link_element = i.find('a', {'class':'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa xo1l8bm'})
        c_link = link_element["href"]
        Comment = pd.DataFrame(data = [
                                {'PostID':postID,
                                 'CommentID':commentID,
                                 'CommentName':commentName,
                                 'CommentTime':commentTime,
                                 'CommentContent':CommentContent,
                                 'Link':c_link}],
                        columns = ['PostID','CommentID', 'CommentName', 'CommentTime', 'CommentContent', 'Link'])
        Comments = pd.concat([Comments, Comment], ignore_index=True)
        commentCount += 1
    
        
    
    replyCount = 0
    for i in userContent.findAll('div', {'xdj266r xexx8yu x4uap5 x18d9i69 x46jau6'}):
        reply_CommentContent = 'Sticker'
        try:
            reply_CommentContent_element = i.find('span', {'class':'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u'})
            if reply_CommentContent_element:
                div_element = reply_CommentContent_element.find('div', {'class':'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs'})
                if div_element:
                    reply_CommentContent = div_element.get_text()
        except Exception as e:
            print(f"Error getting comment content: {e}")

        reply_commentName = i.find('span', {'class':'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u'})
        if reply_commentName:
            reply_commentName = reply_commentName.text
        else:
            reply_commentName = ""

        reply_commentTime = i.find('span', {'class':'x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j'})
        if reply_commentTime:
            reply_commentTime = reply_commentTime.text
        else:
            reply_commentTime = ""

        r_link_element = i.find('a', {'class':'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xi81zsa xo1l8bm'})
        if r_link_element and "href" in r_link_element.attrs:
            r_link = r_link_element["href"]
        else:
            r_link = ""

        reply_Comment = pd.DataFrame(data = [
                                {'PostID':postID,
                                 'CommentName':reply_commentName,
                                 'CommentTime':reply_commentTime,
                                 'CommentContent':reply_CommentContent,
                                 'Link':r_link}],
                        columns = ['PostID', 'CommentName', 'CommentTime', 'CommentContent', 'Link'])
        Comments = pd.concat([Comments, reply_Comment], ignore_index=True)
        replyCount += 1
    print(f"CommentCount:{commentCount}, ReplyCount:{replyCount}")        
    return Comments




driver = webdriver.Chrome()  

Links, pos = FindLinks("https://facebook.com/YohoFans/")  
print(pos)
PostsInformation = pd.DataFrame()
PostsComments = pd.DataFrame()

for link, ele_location in zip(Links, pos):
    try:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        driver.execute_script('window.scrollTo(0, 0);')
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
        driver.execute_script('window.scrollTo(0, 0);')
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
        x = ele_location["x"]
        y = ele_location["y"]
        print(y)

        driver.execute_script('window.scrollTo({}, {});'.format(x, y))
        time.sleep(2)

        
        target_xpath = '//*[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm"]'
        time.sleep(3)
        open_new_page(driver, y, target_xpath)
        time.sleep(3)
        
        #Determine whether there is a similar img element
        img_xpath = '//*[contains(@class, "x1ey2m1c xds687c x5yr21d x10l6tqk x17qophe x13vifvy xh8yej3 xl1xv1r")]'
        img_elements = driver.find_elements(By.XPATH, img_xpath)
        
        if len(img_elements) > 0:
            # If there is an img element, execute the expand_img_post function
            expand_img_post()
            post_block = driver.find_elements(By.XPATH, '//*[@class="x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"]')
            post_block_element = post_block[0]
            post_content_html = post_block_element.get_attribute('innerHTML')
            soup = BeautifulSoup(post_content_html, features="html.parser")
            postContent = PostContent_img(soup)
            try:
                postID = postContent["ID"].iloc[0]
            except:
                postID = None
            PostsInformation = pd.concat([PostsInformation, postContent], ignore_index=True)
            PostsComments = pd.concat([PostsComments, CrawlComment_img(soup, postID)],ignore_index=True)
        else:
            # If the img element does not exist, execute the expand_v_post function
            expand_v_post()
            post_block = driver.find_elements(By.XPATH, '//*[@class="x78zum5 xdt5ytf x1t2pt76 x1n2onr6 x1ja2u2z x10cihs4"]')
        
            post_block_element = post_block[0]
            post_content_html = post_block_element.get_attribute('innerHTML')
            soup = BeautifulSoup(post_content_html, features="html.parser")
            postContent = PostContent_v(soup)
            try:
                postID = postContent["ID"].iloc[0]
            except:
                postID = None
            PostsInformation = pd.concat([PostsInformation, postContent], ignore_index=True)
            PostsComments = pd.concat([PostsComments, CrawlComment_v(soup, postID)],ignore_index=True)
      
        print(PostsComments)
        PostsInformation.to_csv('~/Documents/PostsInformation.csv')
        PostsComments.to_csv('~/Documents/PostsComments.csv')    
    except Exception as e:
        print('Error:', e)
    finally:
        back_origin_page()

PostsInformation.to_csv('~/Documents/PostsInformation.csv')
PostsComments.to_csv('~/Documents/PostsComments.csv')

driver.quit()
