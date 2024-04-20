from clicker.course import ClickerCourseB, ClickerCourseOOP
from clicker.t_est import ClickerTest
from core.settings import ClickerSettings


class Clicker(ClickerCourseOOP, ClickerCourseB, ClickerTest):
    settings = ClickerSettings()

    async def run(self):
        result = []
        assert await self.log_in(
            new_password=self.login
        ), "Invalid username or password"
        await self.mark_course_b()
        await self.mark_course_oop()
        for test_id, db_file, separator in [
            [self.settings.test_id_b, self.settings.db_b, self.settings.separator_b],
            [
                self.settings.test_id_oop,
                self.settings.db_oop,
                self.settings.separator_oop,
            ],
        ]:
            try:
                result.append(await self.run_test(test_id, db_file, separator))
            except Exception as e:
                result.append(
                    {
                        test_id: {
                            "status": "ERROR",
                            "message": "Something went wrong. Maybe testing is not scheduled",
                        }
                    }
                )
                self.logger.error(str(e))
        return result
