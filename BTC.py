from selenium import webdriver
import time

ids="mizuno.kakeru@icloud.com"
pas="Starwars0510"

def without():
    driver= webdriver.Chrome(r"C:\Users\mizun\OneDrive\MyPythonProject\Mypandas\chromedriver.exe")
    driver.get("https://freebitco.in/?op=home")
    
    login=driver.find_element_by_link_text("LOGIN")
    login.click()
    
    time.sleep(1)

    idss=driver.find_element_by_id("login_form_btc_address")
    idss.send_keys(ids)

    #pass入力
    passs=driver.find_element_by_id("login_form_password")
    passs.send_keys(pas)

    #ログインボタンクリック
    inn=driver.find_element_by_id("login_button")
    inn.click()
    time.sleep(1)
    
    #ページ最下部へ移動
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    try:
        #witoutボタンクリック
        cap=driver.find_element_by_id("play_without_captchas_button")
        cap.click()
        
        #GOT ITクリック
        cc=driver.find_element_by_link_text("Got it!")
        cc.click()
        
        #ロールボタンクリック
        roll=driver.find_element_by_css_selector("#free_play_form_button")
        roll.click()
        print("ロール完了")
    except:
        print("まだ時間じゃない")
    time.sleep(1)
    driver.quit()

without()