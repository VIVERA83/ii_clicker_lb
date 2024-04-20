from clicker.auth import AUTHClicker
from clicker.utils import wait_random_time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BaseClickerCourse(AUTHClicker):
    @wait_random_time(min_sec=3, max_sec=5)
    async def _mark_completed(self, button: WebElement):
        if button.text == "Отметить как выполненный":
            button.click()


class ClickerCourseB(BaseClickerCourse):
    @wait_random_time()
    async def mark_course_b(self):
        sections = [2, 3]
        for section in sections:
            url = self.create_url("course/view.php", id=163, section=section)
            self.driver.get(url)
            await self._mark_completed_section()
            self.logger.info(f"mark section {section} ")
        self.logger.info("the course has been completed: b")

    @wait_random_time()
    async def _mark_completed_section(self):
        element = self.driver.find_element(By.CLASS_NAME, "content")
        buttons = element.find_elements(By.TAG_NAME, "button")
        await self.__mark_completed(buttons)

    async def __mark_completed(self, buttons: list[WebElement]):
        for button in buttons:
            await self._mark_completed(button)


class ClickerCourseOOP(BaseClickerCourse):

    @wait_random_time()
    async def mark_course_oop(self):
        url = self.create_url("course/view.php", id=162)
        self.driver.get(url)
        button = self.driver.find_element(
            By.XPATH, '//*[@id="module-2152"]/div/div/div[2]/div[2]/div/button'
        )
        await self._mark_completed(button)
        self.logger.info("the course has been completed: oop")
