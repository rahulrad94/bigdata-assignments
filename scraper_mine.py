from selenium import webdriver
import time

chromedriver = "/Users/rahul/Big_data/ass2/part2/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver)

driver.get("http://www.ufostalker.com/tag/photo")

count = 1
links = []

file = open("image_links.txt", "w")

while count <= 407:
    var = driver.find_elements_by_css_selector('ng-include.ng-scope')[1].find_elements_by_tag_name('tbody')
    # var = driver.find_elements_by_tag_name('tbody')
    time.sleep(6)
    var_size = len(var)
    print "Page: " + str(count)
    for i in range(var_size):
        print "Entry: " + str(i)
        # go to one of the link
        if str(var[i].get_attribute('class')) == "no-media":
            continue
        var[i].click()
        time.sleep(3)

        # parse the page and get to the image section
        val = driver.find_elements_by_css_selector('td.ng-scope')
        time.sleep(3)

        for j in range(len(val)):
            l = val[j].find_elements_by_tag_name('a')
            for k in range(len(l)):
                print str(l[k].get_attribute('href'))
                file.write(str(l[k].get_attribute('href')) + "\n")

        driver.back()
        time.sleep(3)
        var = driver.find_elements_by_css_selector('ng-include.ng-scope')[1].find_elements_by_tag_name('tbody')
        time.sleep(3)

# go to next page
    count = count+1
    if count == 408:
        break
    pages = driver.find_elements_by_tag_name('ul')
    time.sleep(1)
    next_page = pages[0].find_elements_by_link_text(str(count))
    time.sleep(1)
    next_page[0].click()

    time.sleep(30)
