from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas
import random

FIRST_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
SECOND_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
                  'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
THIRD_LETTERS = ['A', 'C']


class InventoryControl:
    def __init__(self):
        self.chrome_driver_path = Service("/Users/harryform/Documents/Development/chromedriver")
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)

    # web scraping to fetch item names from Kohl's website
    def get_item_name(self):
        self.driver.get("https://www.kohls.com/catalog/comforters-bedding-bed-bath.jsp?CN=Product:"
                        "Comforters+Category:Bedding+Department:Bed%20%26%20Bath&icid=bba-a1-"
                        "comforters&kls_sbp=58733507514709319003316217040519848908&PPP=120&S=1")

        time.sleep(5)
        close_tab = self.driver.find_element(By.CLASS_NAME, "dy-lb-close")
        close_tab.click()
        time.sleep(3)
        item_name = self.driver.find_elements(By.CLASS_NAME, "prod_nameBlock")
        item_text = [name.text for name in item_name]

        item_names = pandas.DataFrame(item_text)
        with open('item_names.txt', 'a') as f:
            items_as_string = item_names.to_string(justify='left', header=False, index=False)
            f.write(items_as_string)


# assigns locations and item numbers for items in warehouse
class WarehouseOrganizer:
    def __init__(self):
        pass

    def location_generator(self):

        bin_location_list = []

        for i in range(0, 100):
            random_first_number = random.randint(18, 56)
            random_second_number = random.randint(1, 6)
            random_first_letter = random.choice(FIRST_LETTERS)
            random_second_letter = random.choice(SECOND_LETTERS)
            random_third_letter = random.choice(THIRD_LETTERS)

            x = f"{random_first_letter}{random_second_letter}{random_first_number}" \
                f"-0{random_second_number}{random_third_letter}"
            bin_location_list.append(x)
        bin_locations = pandas.DataFrame(bin_location_list)
        with open('bin_locations.txt', 'a') as file:
            locations_as_string = bin_locations.to_string(justify='left', header=False, index=False)
            file.write(locations_as_string)

    def item_number_generator(self):

        item_number_list = []

        for i in range(0, 100):
            random_first_letter = random.choice(SECOND_LETTERS)
            random_second_letter = random.choice(SECOND_LETTERS)
            random_first_number = random.randint(0, 9)
            random_second_number = random.randint(0, 9)
            random_third_number = random.randint(0, 9)
            random_fourth_number = random.randint(0, 9)

            y = f"{random_first_letter}{random_second_letter}-" \
                f"{random_first_number}{random_second_number}{random_third_number}{random_fourth_number}"

            item_number_list.append(y)
        item_numbers = pandas.DataFrame(item_number_list)
        with open('item_numbers.txt', 'a') as file:
            items_as_string = item_numbers.to_string(justify='left', header=False, index=False)
            file.write(items_as_string)


# bot = InventoryControl()
# bot.get_item_name()
# pick = WarehouseOrganizer()
# pick.location_generator()
# pick.item_number_generator()
