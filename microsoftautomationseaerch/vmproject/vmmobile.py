import pyautogui,time,requests,random,asyncio,randomWords
count = 0
switch = True

async def maxWindow():
    time.sleep(3)
    pyautogui.hotkey('win', 'up')
    time.sleep(1)
    pyautogui.hotkey('win', 'down')
    time.sleep(1)
    pyautogui.hotkey('win', 'up')
    time.sleep(1)

async def openedge():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('edge',interval=0.2)
    time.sleep(3)
    pyautogui.press('enter')

async def closewidnows():
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'm')
    for a in range(0, 6):
        pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.hotkey('ctrl', 'shift', 'm')
    for a in range(0, 6):
        pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('alt', 'f4')

async def searchOnBing(word):
    global count
    time.sleep(3)
    pyautogui.scroll(-100)
    time.sleep(2)
    pyautogui.scroll(600)
    time.sleep(3)
    #click the ms logo at top
    x, y = pyautogui.locateCenterOnScreen('./src/vmbinglogo.jpg',confidence=0.5)
    pyautogui.moveTo(x,y,2)
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)

    #click to search bar
    # x, y = pyautogui.locateCenterOnScreen('./src/search.png',confidence=0.7)
    pyautogui.moveTo(300,200,2)
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    pyautogui.write(word,interval=0.2)
    pyautogui.press('enter')
    time.sleep(7)
    count = count + 1


async def newtab():
    time.sleep(10)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.moveTo(300, 540,2)
    time.sleep(1)
    pyautogui.click(button='right',clicks=1)
    time.sleep(1)
    #click the inspect button
    x, y = pyautogui.locateCenterOnScreen('./src/vminspect.jpg',confidence=0.5)
    pyautogui.moveTo(x,y,2)
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)
    # search on overflowed version of edge
    x, y = pyautogui.locateCenterOnScreen('./src/vmbiglogo.jpg',confidence=0.5)
    pyautogui.moveTo(x,y,2)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write('https://www.bing.com',interval=0.2)
    pyautogui.press('enter')
    time.sleep(5)


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

async def main():
    global count,switch
    time.sleep(5)
    # await closewidnows()
    await openedge()
    #await maxWindow()
    await newtab()
    # Fetch random words asynchronously
    random_words = await fetch_random_words()
    if random_words:
        for word in random_words:
            if count == 25:
               break
            await searchOnBing(word)   
          


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main()) 



    
