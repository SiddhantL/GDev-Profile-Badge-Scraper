# GDev-Profile-Badge-Scraper
### GDev Profile Badge Scraper is a Google Developer Profile Web Scraper which scrapes for specific badges in a user's Google Developer Profile. This first version is specific to the use case for detecting 16 badges for Android Study Jam participants/facilitators and gives an output of each badge filtered individually. As Google themselves do not provide a service to track multiple user's GDev profile, I thought of writing this script myself. This script has a time complexity of 8(n). It can further be modified to reduce the time complexity.
![Sample Output](http://url/to/img.png)
## Requirements
- [x] Selenium
- [x] Chrome Driver
- [x] Pandas
- [x] time
- [x] bs4 (BeautifulSoup)
- [x] [Executable Chrome Driver Script](https://chromedriver.chromium.org/downloads)(Select compatible chrome version)

## How to run the script?
- Keep ChromeDriver executable file(.exe) in the same folder as the program code or in the same project folder
- [Have list of all participants in a .csv file](https://docs.google.com/spreadsheets/d/1gUeJaZH4WQUQoIYJ020QyDOF4M7le7-E3QC6xhmks2E/edit?usp=sharing)
- Customize the badges according to your requirements, modify the if statements as mentioned in the comments
- Finally, press RUN!
