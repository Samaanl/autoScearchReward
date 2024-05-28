import pyautogui,time,requests,random,asyncio,randomWords
#write code to fetch data from using request https://random-word-api.herokuapp.com/word?number=30
pyautogui.PAUSE = 1
count = 0
switch = True
start_time = time.time()

async def maxWindow():
    time.sleep(3)
    pyautogui.hotkey('win', 'up')
    time.sleep(1)
    pyautogui.hotkey('win', 'down')
    time.sleep(1)
    pyautogui.hotkey('win', 'up')
    time.sleep(1)

# async def searchOnBing(word):
#     global count
#     pyautogui.scroll(100)
#     time.sleep(3)
#     #click the ms logo at top
#     x, y = pyautogui.locateCenterOnScreen('./src/msLogo.png',confidence=0.5)
#     pyautogui.moveTo(x,y,2)
#     time.sleep(1)
#     pyautogui.click()
#     time.sleep(3)

#     #click to search bar
#     # x, y = pyautogui.locateCenterOnScreen('./src/search.png',confidence=0.7)
#     pyautogui.moveTo(500,250,2)
#     time.sleep(1)
#     pyautogui.click()
#     time.sleep(1)
#     pyautogui.write(word,interval=0.2)
#     pyautogui.press('enter')
#     time.sleep(7)
#     count = count + 1

# async def newtab():
#     global mobile, searcOnPC
#     time.sleep(3)
#     pyautogui.hotkey('ctrl', 't')
#     time.sleep(1)
#     pyautogui.moveTo(300, 540,2)
#     time.sleep(1)
#     pyautogui.click(button='right',clicks=1)
#     time.sleep(1)
#     #click the inspect button
#     x, y = pyautogui.locateCenterOnScreen('./src/inspect.png',confidence=0.8)
#     pyautogui.moveTo(x,y,2)
#     time.sleep(1)
#     pyautogui.click()
#     time.sleep(5)
#     # search on overflowed version of edge
#     x, y = pyautogui.locateCenterOnScreen('./src/searchmobile.png',confidence=0.5)
#     pyautogui.moveTo(x,y,2)
#     time.sleep(1)
#     pyautogui.click()
#     time.sleep(1)
#     pyautogui.write('https://www.bing.com',interval=0.2)
#     pyautogui.press('enter')
#     time.sleep(3)
#     mobile = False
#     searcOnPC = False

async def openedge():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('edge',interval=0.2)
    time.sleep(3)
    pyautogui.press('enter')

async def switchuser():
    global switch
    # #click to open menu page
    # x, y = pyautogui.locateCenterOnScreen('./src/Red.jpg',confidence=0.5,region=(0,0,400,90))
    # pyautogui.click(x, y, interval=0.5)
    # time.sleep(3)
    # #click to switch user
    # x, y = pyautogui.locateCenterOnScreen('./src/Red.jpg',confidence=0.5,region=(0,300,400,100))
    # pyautogui.click(x, y, interval=0.5)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'm')
    for a in range(0, 6):
        pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('enter')
    switch = False

async def fetch_random_words():
    # try:
    #     url = "https://random-word-api.herokuapp.com/word?number=110"
    #     response = await loop.run_in_executor(None, requests.get, url)
    #     words = response.json()
    #     return words
    # except Exception as e:
    #     print(f"Error fetching data from API: {e}")
    #     return None
    return randomWords.random_words

async def scroll():
    number = random.randint(300, 800)
    time.sleep(1)
    pyautogui.scroll(int(f'-{number}'))
    time.sleep(5)
    #pyautogui.scroll(number)

async def search(word):
    global count
    time.sleep(1)
    pyautogui.press('f4')
    time.sleep(1)
    pyautogui.write(f'{word} ', interval=0.25)
    pyautogui.press('enter')
    count = count + 1
    print(f"local Search {count}: {word}")
    await scroll()
    time.sleep(1)

async def main():
    global count, switch
    await openedge()
    # await maxWindow()

    # Fetch random words asynchronously
    random_words = await fetch_random_words()
    pyautogui.moveTo(300,100,2)
    time.sleep(5)
    if random_words:
        for word in random_words:
            if count == 35:
                break
            await search(word)
    print("--- %s seconds ---" % (time.time() - start_time))
    pyautogui.hotkey('alt', 'f4')
    time.sleep(3)   



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main()) 



