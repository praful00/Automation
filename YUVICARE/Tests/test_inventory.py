import time

import pytest
from selenium.common.exceptions import StaleElementReferenceException

from PageObjectModel.Inventory import Inventory
from Testdata.Inventorydata import Inventorydata


@pytest.mark.usefixtures("setup")
class Testinventory:

    def test_inventory(self, getdata):
        self.driver.implicitly_wait(5)
        inventory = Inventory(self.driver)
        inventory.enteruserdid().send_keys(getdata["userdid"])
        inventory.enterpassword().send_keys(getdata["password"])
        inventory.clickloginbutton().click()
        item = inventory.click_inventory()
        print(len(item))

        for items in item:
            if items.text == "Inventory":
                items.click()
                time.sleep(3)
                try:

                    inventory.click_navigation().click()
                    time.sleep(3)
                    inventory.click_procurement().click()
                    time.sleep(3)
                    inventory.click_selectlocation().click()
                    time.sleep(3)
                    location = inventory.select_location()
                    print(len(location))
                    for locations in location:
                        if locations.text == "DENTAL STORE":
                            locations.click()
                    time.sleep(3)
                    inventory.click_grnwithpo().click()
                    inventory.click_selectproduct().click()
                    product = inventory.select_productdropdown()
                    print(len(product))
                    for products in product:
                        if products.text == "POCO - GEN - 5796":
                            products.click()
                    break
                except StaleElementReferenceException as e:
                    print(e.msg)









    @pytest.fixture(params=Inventorydata.inventory_data)
    def getdata(self, request):
        return request.param


