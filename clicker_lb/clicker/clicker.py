from clicker.course import ClickerCourseB, ClickerCourseOOP, ClickerCourseA
from clicker.t_est import ClickerTest
from core.settings import ClickerSettings


class Clicker(ClickerCourseOOP, ClickerCourseA, ClickerCourseB, ClickerTest):
    settings = ClickerSettings()

    async def run(self, course_type: list[int]) -> list[dict]:
        result = []
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
        for test_id, db_file, separator in [
            [self.settings.test_id_a, self.settings.db_a, self.settings.separator_a],
            [self.settings.test_id_b, self.settings.db_b, self.settings.separator_b],
            [self.settings.test_id_oop, self.settings.db_oop, self.settings.separator_oop],
            [self.settings.test_id_siz, self.settings.db_siz, self.settings.separator_siz]
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
        return result
