from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import pandas as pd

path = "c:\\chromedriver.exe"
options = Options()
options.add_argument(f"executable_path={path}")
browser = webdriver.Chrome(options=options)

nam = []
ye = []
wi = []
los = []
pc = []
gfor = []
gaw = []
dif = []

for i in range(1, 25):
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
    browser.get(url)
    names = browser.find_elements(By.CLASS_NAME, 'name')
    years = browser.find_elements(By.CLASS_NAME, 'year')
    wins = browser.find_elements(By.CLASS_NAME, 'wins')
    losses = browser.find_elements(By.CLASS_NAME, 'losses')
    pct = browser.find_elements(By.CLASS_NAME, 'pct.text-success')
    gf = browser.find_elements(By.CLASS_NAME, 'gf')
    ga = browser.find_elements(By.CLASS_NAME, 'ga')
    diff = browser.find_elements(By.CLASS_NAME, 'diff.text-success')
        
    for name, year, win, loss, p, goals_for, goals_away, diff_goals in zip(names, years, wins, losses, pct, gf, ga, diff):
        nam.append(name.text)
        ye.append(year.text)
        wi.append(win.text)
        los.append(loss.text)
        pc.append(p.text)
        gfor.append(goals_for.text)
        gaw.append(goals_away.text)
        dif.append(diff_goals.text)

browser.quit()
data = {
    'Team': nam,
    'Year': ye,
    'Wins': wi,
    'Losses': los,
    'Win(%)': pc,
    'Goals For': gfor,
    'Goals Away': gaw,
    'Goal Difference': dif
}

df = pd.DataFrame(data)
df.to_csv('hockeys.csv', index=False)
