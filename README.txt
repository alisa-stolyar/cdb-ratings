
1. crawl_best_buy.ipynb and crawl_amazon.ipynb

    These files use the links from respective website excel sheets with initial links to crawl the websites. It also uses regex to find the subsequent review page links (i.e. 1-10 on Amazon) and crawl those. 
    The files are saved locally - found in 'amazon pages' and 'bestbuy pages'. 

2. scrape_files.py 

    This file has methods for both Amazon and Best Buy to scrape necessary information from the html files downloaded from step 1. 
    ** This file scrapes review titles and text as well. Even if you are only looking for star ratings, it might be worth it to scrape text as well - sometimes there are duplicates so step 3 will filter out duplicate reviews. 

    This data can be found in the reviews-excel-sheets folder. 

3. clean_data.ipynb

    This file has code to clean the text data + standardize star ratings. 

    - The code chunk following "GET STAR INTEGER FROM RATING TEXT" will get the single integer rating from the rating text (it is usually like "4.0 out of 5 stars"). 
    - The code chunk following "DROP DUPLICATES" will drop duplicate reviews based on review column. 
    - The following code chunk after that will aggregate the star reviews by device including review count and mean star rating.  
