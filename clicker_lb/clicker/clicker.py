from clicker.course import ClickerCourseB, ClickerCourseOOP, ClickerCourseA, ClickerCourseOB
from clicker.t_est import ClickerTest
from core.settings import ClickerSettings


class Clicker(ClickerCourseOOP, ClickerCourseA, ClickerCourseB, ClickerCourseOB, ClickerTest):
    settings = ClickerSettings()

    async def run(self, course_type: list[int]) -> list[dict]:
        result = []
        try:
            assert await self.log_in(
                new_password=self.login
            ), f"Invalid username or password: {self.login} {self.password}"
            # course_type = [2393, 2310, 2311], a=2311, b = 2393, oop = 2310
            if 2311 in course_type:
                await self.mark_course_a()
            if 2393 in course_type:
                await self.mark_course_b()
            if 2310 in course_type:
                await self.mark_course_oop()
            if 2275 in course_type:
                await self.mark_course_ob()

            for test_id, db_file, separator in [
                [self.settings.test_id_a, self.settings.db_a, self.settings.separator_a],
                [self.settings.test_id_b, self.settings.db_b, self.settings.separator_b],
                [self.settings.test_id_oop, self.settings.db_oop, self.settings.separator_oop],
                [self.settings.test_id_siz, self.settings.db_siz, self.settings.separator_siz],
                [self.settings.test_id_ob, self.settings.db_ob, self.settings.separator_ob],
            ]:
                # try:
                # course_type = [2393, 2310, 2311], a=2311, b = 2393, oop = 2310
                if test_id in course_type:
                    result.append(await self.run_test(test_id, db_file, separator))
            # except Exception as e:
            #     result.append(
            #         {
            #             "username": self.login,
            #             "password": self.password,
            #             test_id: {
            #                 "status": "ERROR",
            #                 "message": "Something went wrong. Maybe testing is not scheduled",
            #             },
            #         }
            #     )
            #     self.logger.error(str(e))
        except AssertionError:
            result.append({
                course_type[0]: {
                    "username": self.login,
                    "password": self.password,
                    "id_test": course_type[0],
                    "status": "не выполнено, неверный логин или пароль",
                    "message": f"Попыток выполнения теста: 0",
                }
            }
            )
        return result
