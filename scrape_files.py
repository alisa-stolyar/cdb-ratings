
from bs4 import BeautifulSoup
# import requests
import csv 
import os

## amazon scrape 
def amazon_scrape():
    output_csv = 'amazon_reviews.csv'
    rows= []
            
    
    for folder in os.listdir('/Users/alisa/Desktop/PittNAIL/cleardashboard_reviews/amazon pages'): # path to folder holding all amazon pages 
        folder_path = os.path.join('/Users/alisa/Desktop/PittNAIL/cleardashboard_reviews/amazon pages', folder) 
        row = []
        # check if the current folder exists
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if file_name[-6:] != "t.html": # don't scrape the initial page (called #_init.html)
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        html_content = file.read()
                        print(f"read {file_path}")
                        soup = BeautifulSoup(html_content, 'lxml') #parser method 
                        reviews = soup.find_all('div', {'data-hook': 'review'})

                        if len(reviews)!=0:
                            
                            for review in reviews:
                                # star rating text
                                star_rating_element = review.find('i', {'data-hook': 'review-star-rating'}) 
                                star_rating_text = star_rating_element.text.strip() if star_rating_element else 'No rating found'

                                # review title text
                                review_title_element = review.find('a', {'data-hook': 'review-title'})
                                if review_title_element:
                                    review_title_span = review_title_element.find_all('span')
                                    review_title_text = review_title_span[-1].text.strip() if review_title_span else 'No title found'
                                else:
                                    review_title_text = 'No title found'


                                # review text
                                review_text_element = review.find('span', {'data-hook': 'review-body'})
                                review_text = review_text_element.text.strip() if review_text_element else 'No review text found'

                                # print the extracted info
                                # print("Star Rating:", star_rating_text)
                                # print("Review Title:", review_title_text)
                                # print("Review Text:", review_text)

                            
                                row = [folder,"Amazon", star_rating_text, review_title_text, review_text] # row with information in new excel
                                rows.append(row)
                                print('-----------------')
                        else: # if there are no reviews on that page 
                            print("no reviews on this page")
                            row = [folder,"Amazon", "NA","NA","NA" ]
                            rows.append(row)

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile: #write to csv
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['ID', 'Site', 'Star_Rating', 'Title' ,'Review'])
        for row in rows:
            csv_writer.writerow(row)

## best buy scrape 
def bestbuy_scrape():
    output_csv = 'bestbuy_reviews.csv'
    rows= []
            
    
    for folder in os.listdir('/Users/alisa/Desktop/PittNAIL/cleardashboard_reviews/bestbuy pages'):
        folder_path = os.path.join('/Users/alisa/Desktop/PittNAIL/cleardashboard_reviews/bestbuy pages', folder)
        row = []
        # check if the current folder exists
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
            
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    html_content = file.read()
                    print(f"read {file_path}")
                    soup = BeautifulSoup(html_content, 'lxml') #parser method 
                    reviews = soup.find_all('li', class_ = 'review-item')

                    if len(reviews)!=0:
                        
                        for review in reviews:
                        

                            # star rating text
                            star_rating_element = review.find('p', class_ = "visually-hidden")
                            star_rating_text = star_rating_element.text.strip() if star_rating_element else 'No rating found'

                            # review title text
                            review_title_element = review.find('h4', class_= 'c-section-title review-title heading-5 v-fw-medium')
                            review_title_text = review_title_element.text.strip() if review_title_element else 'No review text found'
                        

                            # review text
                            review_text_element = review.find('p', class_ = 'pre-white-space')
                            review_text = review_text_element.text.strip() if review_text_element else 'No review text found'

                            # Print the extracted information
                            # print("Star Rating:", star_rating_text)
                            # print("Review Title:", review_title_text)
                            # print("Review Text:", review_text)

                        
                            row = [folder,"BestBuy", star_rating_text, review_title_text, review_text]
                            rows.append(row)
                            print('-----------------')
                    else:
                        print("no reviews on this page")
                        row = [folder,"BestBuy", "NA","NA","NA" ]
                        rows.append(row)

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['ID', 'Site', 'Star_Rating', 'Title' ,'Review'])
        for row in rows:
            csv_writer.writerow(row)



if __name__ == "__main__":
    #   amazon_scrape()
      bestbuy_scrape()



