from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request
from pytube import YouTube
import os
from pathlib import Path
import yt_dlp as youtube_dl
import os
from pyChatGPT import ChatGPT
from random import randint

def youtube2mp3 (url):
    os.remove('song.mp3')
    # url input from user
    yt = YouTube(url)

    ##@ Extract audio with 160kbps quality from video
    video = yt.streams.filter(abr='160kbps').last()

    ##@ Downloadthe file
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = 'song.mp3'
    os.rename(out_file, new_file)
    ##@ Check success of download


def GetImage(topic):
    try:
        #service = Service()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless=new")
        #chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=chrome_options)#service=service, options=options)
        driver.get("https://www.google.com/search?sca_esv=cd43192195f14f59&rlz=1C1CHZN_enCA1059CA1059&sxsrf=ACQVn08vGkFCXbnm3R1OgEwUkre2suvU9w:1710788398051&q="+topic+"&tbm=isch")
        time.sleep(5)
        image = driver.find_elements(By.XPATH, "//div[@class='fR600b islir']/img")
        image = image[3]
        image_url = image.get_attribute("src")
        urllib.request.urlretrieve(image_url, "image.png")

    except Exception as e:
        print(e)

def GetMusic(song):
    try:
        #service = Service()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless=new")
        #chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome()#options=chrome_options)#service=service, options=options)
        driver.get("https://www.youtube.com/results?search_query=" + song)
        time.sleep(2)
        image = driver.find_elements(By.XPATH, "//div[@id='title-wrapper']/h3/a")[1]
        image_url = image.get_attribute("href")
        print(image_url)
        youtube2mp3(image_url)
        os.startfile('song.mp3')

    except Exception as e:
        print(e)

def chat(prompt):
    session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..O8uNa99Jbk1fYYcl.k6MBQlUz-_A4usIEoHoLupv4RFYNboWf9U-i5pioqV7I6PM-1pJLtjfmFh0li7nJV-UQk_97m0gW93jPPXqEbBMYJg68mwwR1QjmLRo6dv1JOsx76dUsoTr1opLBgc7jWdS9_OKbMl2mI0pPpk0YGHztQzZmgL_68letQSF6B4ep-D-ttmRY8WX3va2HCfYzxoGtUaNlBVoYKQb0KUfqooQtci1Qxmgb4cgqpm2gUTF4P5eYnh8t8qjr7NuABZDrJS56Lme-rdLLn8wm1DZwKLDjLZ0zvpYxyJJ6c_NurShobV__Cg5itJ7GeRte658wC9kKO4oQfCXHNUJtvhcrt3aKSEhWbFGDk9UQwQaR3ltRInWCqDbJZjBSW7uuipQkaDQzN8Mj_qd7LiPXGQwGub8XelKLcnI6obo7TZ75lfHkb_eh0AI7ejMNlTqk1x0rWpyc3tM7RPfaPMXGxL_hL_wcHojxFfvMrc-AFBkcwa2DgI7RQOrH4moINGuOGRmgyAovf0guw83babARtZcSDDg0L3KQASDzE36iSrlKfsG-V5k9ww9q3fl1AshqlzsmRgvljiG6DG_p_hoWFMkc34VWyjxXr8tLVEePA8VOHa0qn6tYfVHLmcTSeam1UhSiJPW94TipgPo3XhDM8D8kI92W3x5BYFi98ms0IPTs6eSbMDuf8pDvraci-ASyJRKI-Nn4PHXDzu3hK1f2bAjHyuYrgossK7qow-QaHwRhFbdRy9pS5PhTTZPhOJLFo2YTxau5_u1pnr-QB9z6UznRz-SYa-PVKYePjV0yCWUnal4l2j7roIuPkgZ8W6jV_vsUAfdYXn9myNHInOz65RvA4bLM_ido6ilPmZ3jcHqPYyuUE5NjTS27D4xmZGHBIYXbyDrtAFTe1Px-0PksuP1_t7KJJaz1yC3tSU-WeDXLNbwY-anHO_4Httn18QrH0e_y2goCSQ1w95MrRbiC0eL0yPdIIlXsghM0kCpQdkjHMVP1ZfMGdBT0hIRRQAaudEOungVgwZqy-VCz7FgMpQZ-76s5D1CEUeg5eKFo4Ix7NiRUKWv-Tt9SMN_qLzTRhMpfz1AheXFYWfnOwi70TldFwRW0vOOpdzxCrmgII2hiBcqd5pCUGUrXMn4wkahm7iqDtkjFvMJp2F53Mt5IbwJ3T4q7ibJbBW9dJD_9LUNuxuxZ2cI-Mo5hyhZE9HRLx3pleyMoYwXX4tP_QplDqoWfR76IvyfYXV_STMkc8Gd9r1Fn3fcI4otfKH2KScRJTgzTfh1-UvG1z8c6Fw0tedHrvSJVTxqhHy-tBbFJWf1ewf8EsHQ8u_jpyPF0lQrOVN_qvelL1a6aTOnb95Ege6BI7nyECZkk_I7IrJOKyJEI2aqliKrbxvunEjHpM6NOFS-LPyAGpJucNdd86bD_Pzxz9HqTH-cYkXvXPEjnkrRH0gr_vKcm_E0VJg77KP6mRYnEX5DDW9hoyk9RPsnwtGm4nfrw_pM-kQxZOtVMR7Mly0slT8_QuQf3jML5NF3SwFzX3F84UQ_JSbE3gpF8T2ZoxmksePbgm79rv7gulIVxOIQ38OsPTjok5DQGR3GZ7UN1n0crW0P53K51PMaMOpKbZvZ4MyCMupgOoJvKvA-qiLqrtAbTT9BRlCLIgZrUeRWGcxD3KyWzDteenLKRVqUenrhWB98GiRPFBULXIqap17jbYaOfyNto4Zmaso8PF2ruwsc3vEt1bVv-pfkAb1aWQE4TrsGFiek6tj6D7Q7In8-Sxas53U_N_jIajX-ZI7UGulGuHtGdFKNxhuqGm2HZXaGXXH6JrUj04xIWi7T8gJnTM9N2zo6Q-6kexJLIH8AuNgKhPCAZyQcdZolwq6dCI3_le6wEpFKgT9CcUxLfY91c4iGpLPze6A7jKwtuthktgOYgbz_mj0wEL6AybyZrsmDmH9QfmfNSts1GSohENahKaDY8wEYDrU6uHSecR4-qQkLHKI3D_i4E9lTy-7abJQhCttjEz9xqcLGvofJ4Ma3q6zheBRnIgeChu4cry0W1bWKrNmk-vswXBIFDM1AA4bAC6NkYnBJJLwEtJlF6rp5-IxaglgdY2q1V6gEz3BNOzBDS4DKHBA0MLUL8_hGvQBXzziwoeFhXvHEIH3KLJs5IYPfWVeV8M7yJDumLJ0yMcWSuqePXy_zu983m7XF6fd6AcvuIWL1zGuTwpeb01vd_BQK9LUqRz5sgqTq6ygFQCm2U5faos8Y7LARFXWujHBk9cfmaYcycnMBRe4WdzaS_UoC7TTTmSM3M8bDDQ_l3AGXh1Uv952_ikPxE83nYxjZoNYMQiUIwVQSdnLJwUURj6lwvZPyjnbGsPlFB4ln_gBBeSSTK0FYbE72gjeMzVr5Aap8YqDb1jNSR5YFN5AQjhXuWl-O9vFHIP-RJ2bF2NNHqDsuKRyh3taHI6mj0TYUuY8JwVl-FOXhZWGZbkyNu0xaeMk-vEA9fJxESW2YF8WJa5FCS_Rw74DrMsCBlkfS3djaZUOmeUNMFdkhRR2BRanrv7yIn7d05W5FqvqX-BEH-OjbXnj6LAObuVxuPFWvjz9Y174hhFPRyQ0in7_EFOrYFiRKPIFpNtRz28nkKGB8x8FttGctwAfBTH0Z0cy0fXrluwSkjA348P4iAq-fe0H_GrWp9MBuCyUCjjDtJnTbogHQS91zTEllQVRZpMxkP8AczjdQEMQtE8Gt3edaCKOqpriFnjlZbHoXz8DBMWVk0cuUBeu2bV602w9T3y5hqLZck7Yz1S_15rptKwwTc6CyJQGHSygalwACjFg3HD7Z3Iz8yQzulCDTjrFkLtsqQeq4ZGPAV53iUgOFQGUUBV6ZwYeab1HEtAHf6ernUy96s36hBsIVVfPeX9QqQtCDod1YJiH8EwJxI5dvlrRn9fXirDWfORzoKaJuuatrgmUKvNKzOBRDhofgtflnKZ7tw4TqW5Q.pUY9udMim71C1DmrtJbJBQ'
    api = ChatGPT(session_token)
    resp = api.send_message(prompt + " In 5 sentences")
    print(resp['message'])
    return resp['message']


