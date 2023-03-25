from flask import Flask, render_template, request
import requests
import json

import time
import numpy as np
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


app = Flask(__name__)


@app.route('/')
def get_bee():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    beejson = r.json()
    print(beejson[0]['name'])
    print(beejson[0]['abv'])
    print(beejson[0]['description'])
    print(beejson[0]['food_pairing'][0])

    bee = {
        'name' : beejson[0]['name'],
        'abv' : beejson[0]['abv'],
        'desc' : beejson[0]['description'],
        'foodpair' : beejson[0]['food_pairing'][0]
    }

    print(bee)
    return render_template('index.html', title='Scrape', bee=bee)


@app.route('/scrape', methods=['POST', 'GET'])
def scrape():
    if request.method == 'POST':
        job_name = request.form['job_name']

        # Sleep function 
        def sleep(x):
            time.sleep(x)


        # Wait for a certain measure of time before throwing an exception
        def wait(x):
            driver.implicitly_wait(x)


        # Click Function
        def click_bann_byID(ID):
            actions = ActionChains(driver)
            akzeptieren = driver.find_element(By.ID, ID)
            actions.click(akzeptieren).perform()
            wait(10)
            sleep(0.5)


        # Find Element Function
        def find_element(E):
            elements = driver.find_elements(By.CLASS_NAME, E)
            list_elements = [element.text for element in elements]
            return list_elements


        # Find Elements Function
        def find_elements_HPCO(H,P,C,O):
            header = driver.find_elements(By.CLASS_NAME, H)
            publish = driver.find_elements(By.CLASS_NAME, P)
            company = driver.find_elements(By.CLASS_NAME, C)
            ort = driver.find_elements(By.CLASS_NAME, O) 
            list_header = [title.text for title in header]
            list_publish = [pub.text for pub in publish]
            list_company = [comp.text for comp in company]
            list_ort = [o.text for o in ort]
            return list_header, list_publish, list_company, list_ort


        def log(message):
            timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
            now = datetime.now() # get current timestamp
            timestamp = now.strftime(timestamp_format)
            with open("log/logfile.txt","a") as f:
                f.write(timestamp + ',' + message + '\n')
            
        print('---------------------- StepStone Job Searching Selenium Project ----------------------')
        start=datetime.now()
        log('start_stepstone')
        # Link Descriptions
        link_original_stepstone = 'https://www.stepstone.de/jobs/data-analyst/in-rietberg?radius=50&page=2'

        website_name = 'stepstone'
        job_name = 'Data Engineer'
        ort_ = 'Rietberg'
        radius = 100
        page_number = 1


        #  1 - Create Driver
        Path = '/Users/macbook/Desktop/projects/Github_Repositories/Trainings/web_scpraing_portfolio_deneme/chromedriver'
        driver = webdriver.Chrome(Path)
        print('Create Driver')


        #  2 - Go to Website
        job_link = job_name.replace(' ', '-').lower()
        ort_link = ort_.lower()
        link = f'https://www.stepstone.de/jobs/{job_link}/in-{ort_link}?radius={radius}&page={page_number}&sort=2&action=sort_publish'


        driver.get(link)
        wait(5)
        sleep(1)
        log('Go to Website')


        # 4 -  Take Infos from Page
        # 4.1 - Headers, Publish_Time ,Company, City
        H, P, C, O = ('res-29pyh9', 'res-rf8k2x', 'res-hbyqhf', 'res-1wf9en7')
        list_header, list_publish, list_company, list_ort = find_elements_HPCO(H,P,C,O)


        # 4.2 - Description and Page number of results
        description = driver.find_elements(By.CLASS_NAME, 'res-17md5or')


        # 4.3 - Get Links 'res-1dwe62q'
        list_link01  = driver.find_elements(By.CLASS_NAME, 'res-1dwe62q')
        list_link = [link.get_attribute('href') for link in list_link01]

        # 4.4 - Get Texts for each finding
        list_description = [des.text for des in description]
        print('Header',len(list_header), 'Publish',len(list_publish), 'Company',len(list_company[1:]), 'Ort',len(list_ort), 'Desc', len(list_description), 'Link',len(list_link))


        # 4.6 - DataFrame df
        d = dict(job_title=np.array(list_header), publish=np.array(list_publish), company=np.array(list_company[1:]), city=np.array(list_ort) , description=np.array(list_description), link=np.array(list_link))
        df01 = pd.DataFrame.from_dict(d, orient='index')
        df01 = df01.T


        print(f'DataFrame End : {df01.shape}')
        df01['website'] = website_name
        time_ = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        df01['date'] = time_
        df01['search_title'] = job_name


        # 5.1 - Quit
        end =datetime.now() 
        print('Code Runned No Problem')
        log('end_stepstone')
        print(f'Time = {end - start}')
        sleep(0.5)
        driver.quit()

        # 6.1 Dataframe first 5 Rows
        df01.head(2)

        return render_template('index2.html', title='Scrape', df01=df01)

    else:

        df01 = pd.DataFrame()
        return render_template('index2.html', title='Scrape', df01=df01)




@app.route('/show')
def show():
    return render_template('index2.html', title='show', df01=df01)


if __name__ == '__main__':
    app.run(debug=True)


