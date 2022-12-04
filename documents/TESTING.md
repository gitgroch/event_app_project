# Testing 

Testing methodologies and results are detailed below.

## A note on Responsiveness

Bootstrap was used in this development which is a "Mobile First" approach to development, responsiveness was tested throughout development. Using a "Build, Test, Learn" approach meant that responsiveness issues were addressed as the project progressed (some of these issues can befound in the Bugs & Fixes section below.)

Once the site was completed and deployed, formal testing took place under the following conditions: 

## Hardware Testing 

- Desktop responsiveness was tested on multiple screen sizes and resolutions including:

    - 14 inch 1920 x 1080
    - 24 inch 1920 x 1080 
    - 27 inch 2560 x 1440
    - 34 inch 3440 x 1440
- The Following Mobile Devices were used test layout and responsiveness:

    - Google Pixel 6 
    - Huawei P30 Pro 
    - Samsung Galaxy S20 plus 

## Virtual Testing 

- In addition to hardware testing, multiple templates were used to test responsiveness in Google Chrome Developers tools with the screen size template for Moto 4G being the baseline for the smallest screen size. 

## Browser Testing 

The website was tested manually on the latest versions of following browsers: 

- Chrome 
- Edge 
- Firefox 
- Opera 


## Testing Results 
I used a manual testing method to test all functions of the app. 
Steps Included: 
- Creating Multiple test accounts 
- Creating Multiple test posts and comments
- Editing multiple posts and comments
- Deleting posts and comments 

These tests were performed in bot dev and production environments, results and learninfs from testing is as follows: 


- All internal and external links have been tested and work as intended.
- All Images are responsive and scale to screen size. 
- All navigation menus appear and operate as expected at each defined break point for media queries.
- I did not find any instance of elements such as text or images touching the side of the screen at any screen size.
- Post and comment form sends data to databse as expected
- Post and comment edit form sends data as expected 
- Post and comment deletion works as expected 
- Account creation, login and logout all work as expected.
- Admin dashboard and functionality all work as expected. 
- There are no errors in the console
- There are no remaining app breaking bugs

## Lighthouse 

All pages in the deployed site were passed through Google's Lighthouse tool to test for Performance, Best Practices, Accessibility and SEO in incognito mode. 

The scores from Lighthouse at time of testing were:

**Home Page**
- **Desktop**
    - 80 performance, 92 Accessibility, 100 Best Practice, 100 SEO 
- **Mobile**
    - 70 performance, 92 Accessibility, 100 Best Practice, 92 SEO 

**Post Detail Page**
- **Desktop**
    - 79 performance, 92 Accessibility, 92 Best Practice, 80 SEO 
- **Mobile**
   - 92 performance, 92 Accessibility, 92 Best Practice, 91 SEO 



## Validator Testing 

- HTML 
    - No errors were returned when passing through the official W3C validator.
- CSS
    - No errors were found when passing through the official (Jigsaw) validator.

## Accessibility 

- I used the [Web accessibility evaluation (WAVE)](https://wave.webaim.org/) tool to check if there were any major issues with the Accessibility of website.
- The tool gave me one error for an element in my navigation menu for very low contrast, this was resolved.

# Bugs and Fix Log 

There were numerous bugs discovered and fixes applied throughout development, too many to keep track of, however below I have logged some of the more complex issues I came across that took the most time find a fix for.

**Bug:** County and Categry fields noe passing to DB 

- **Fix:** Change model to include form choices rather from the form iteself

**Bug** Images not passing to DB from form

- **Fix** Add request=FILES to form views