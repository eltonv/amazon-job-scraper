# amazon-job-scraper
This program was created to scrape the Amazon Job hiring page for jobs around the area. I designed this to scrape for job listings that were only part time and around my location.

To change what city you're looking for update the string on line 25:
```
25 city.send_keys('san bernardino')
```
To update what types of jobs you are looking for, update the strings on lines 41 and 45:
```
41 if 'Part Time' in listings[3]
...
45 if 'Part Time' in listings[2]:
```
