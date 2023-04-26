from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import time

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.find_element(By.CSS_SELECTOR, ".nav-link[href*='shop']").click()
        cards = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for card in cards:
            cardName = card.find_element(By.XPATH, "div/h4/a").text
            if cardName == "Blackberry":
                card.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary'").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        alertText = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
        assert "Success! Thank you" in alertText

