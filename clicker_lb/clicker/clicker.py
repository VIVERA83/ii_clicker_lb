from clicker.course import ClickerCourseOOP, ClickerCourseB
from clicker.t_est import ClickerTest
from core.settings import ClickerSettings


class Clicker(ClickerCourseOOP, ClickerCourseB, ClickerTest):
    settings = ClickerSettings()

    async def run(self):
        await self.log_in(new_password=self.login)
        await self.mark_course_b()
        await self.mark_course_oop()
        await self.run_test(self.settings.test_id_b, self.settings.db_b, self.settings.separator_b)
        await self.run_test(self.settings.test_id_oop, self.settings.db_oop, self.settings.separator_oop)
