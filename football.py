from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd
import time

link = "https://www.adamchoi.co.uk/teamgoals/detailed"
path = "c:\\chromedriver.exe"
options = Options()
options.add_argument(f"executable_path={path}")
browser = webdriver.Chrome(options=options)
browser.get(link)

all_matches = browser.find_element(By.XPATH, "//label[@analytics-event='All matches']")
all_matches.click()

dropdown = Select(browser.find_element(By.XPATH,"//select[@id='country']"))
dropdown.select_by_visible_text('Italy')

time.sleep(5)

parent_trs = browser.find_elements(By.CSS_SELECTOR, "tr")


date = []
team_a = []
score_a = []
score_b = []
team_b = []
winner = []


for parent_tr in parent_trs:
    child_tds = parent_tr.find_elements(By.TAG_NAME, "td")
    for index, td in enumerate(child_tds):
        data = td.text
        if index == 0:
            date.append(data)
        elif index == 1:
            team_a.append(data)
        elif index == 2:
            score_parts = data.split("-")
            score_a.append(score_parts[0].strip())
            score_b.append(score_parts[1].strip())
        elif index == 3:
            team_b.append(data)

        
        if index == 3:
            if score_a[-1] > score_b[-1]:
                winner.append(team_a[-1])  
            elif score_a[-1] < score_b[-1]:
                winner.append(team_b[-1])  
            else:
                winner.append("Draw")  

browser.quit()

data = {
    "Date": date,
    "Team_A": team_a,
    "Score_A": score_a,
    "Score_B": score_b,
    "Team_B": team_b,
    "Winner": winner
}

df = pd.DataFrame(data)
df.to_csv("teams.csv", index=False)
