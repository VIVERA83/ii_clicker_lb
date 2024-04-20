import asyncio
from random import randint
from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from clicker.auth import AUTHClicker
from clicker.utils import wait_random_time, load_from_file, save_to_file

Question = str
SubmitBtn = WebElement


class ClickerTest(AUTHClicker):
    @wait_random_time()
    async def open_test(self, id_test: int):
        url = self.create_url("mod/quiz/view.php", id=id_test)
        self.driver.get(url)
        await self.click(".singlebutton.quizstartbuttondiv", By.CSS_SELECTOR)

    def _get_elements_from_question_form(self) -> tuple[Question, list[WebElement], SubmitBtn]:
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, ".mod_quiz-next-nav.btn.btn-primary")
        r0s = self.driver.find_elements(By.CLASS_NAME, "r0")
        r1s = self.driver.find_elements(By.CLASS_NAME, "r1")
        quiz = self.driver.find_element(By.CLASS_NAME, "qtext").text
        return quiz, [*r0s, *r1s], submit_btn

    def _select_answer(self, radios_btn: list[WebElement], correct_answer: str):
        for element in radios_btn:
            if correct_answer == element.text.split("\n")[-1]:
                element.find_element(By.TAG_NAME, "input").click()
                self.logger.info(f"correct answer: {correct_answer}")
                return
        radios_btn[randint(0, len(radios_btn) - 1)].click()

    async def _learn_from_data(self, data: dict, chars: str):
        elements_inc = self.driver.find_elements(By.CSS_SELECTOR, ".que.multichoice.deferredfeedback.incorrect")
        elements_not = self.driver.find_elements(By.CSS_SELECTOR, ".que.multichoice.deferredfeedback.notanswered")
        for index, element in enumerate([*elements_inc, *elements_not]):
            quiz = element.find_element(By.CLASS_NAME, "qtext").text
            correct_answer = element.find_element(By.CLASS_NAME, "rightanswer").text.split(chars)[-1]
            self.logger.info(f"{quiz=} : {correct_answer=}")
            data.update({quiz: correct_answer})

    @wait_random_time()
    async def _submit_test(self) -> bool:
        submit = self.driver.find_element(By.CLASS_NAME, "othernav")
        is_test_passed = "custom_attemp_success" in submit.text
        [check.click() for check in submit.find_elements(By.CLASS_NAME, "form-check-input")]
        submit_btn = submit.find_element(By.CLASS_NAME, "submitbtns").find_element(By.TAG_NAME, "input")
        await asyncio.sleep(1)
        submit_btn.click()
        return is_test_passed

    @wait_random_time()
    async def execute_test(self, data: dict[str, str], chars: str) -> bool:
        while urlparse(self.driver.current_url).path != "/mod/quiz/summary.php":
            quiz, radios_btn, submit_btn = self._get_elements_from_question_form()
            correct_answer = data.get(quiz)
            self._select_answer(radios_btn, correct_answer)
            await asyncio.sleep(5)
            submit_btn.click()
        await asyncio.sleep(5)

        form = self.driver.find_elements(By.TAG_NAME, "form")[-1]
        submit_btn = form.find_element(By.TAG_NAME, "button")
        submit_btn.click()
        await asyncio.sleep(5)

        send_answers_btn = self.driver.find_elements(By.CSS_SELECTOR, ".btn.btn-primary")[-1]
        send_answers_btn.click()
        await self._learn_from_data(data, chars)
        return await self._submit_test()

    @wait_random_time()
    async def run_test(self, id_test: int, db_file: str, separator: str) -> dict[int, dict]:
        self.logger.info(f"run test: {id_test=}")
        data = load_from_file(db_file)
        attempt = 10
        is_success = False
        while attempt :
            attempt -= 1
            await self.open_test(id_test)
            if await self.execute_test(data, separator):
                is_success = True
                break
        save_to_file(db_file, data)
        self.logger.info(f"The test has been completed, {id_test=}")
        return {
            id_test: {
                "status": "The test was passed successfully" if is_success else "The test failed",
                "message": f"Attempts completed: {10 - attempt}",
            }
        }
