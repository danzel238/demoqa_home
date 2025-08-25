
from pages.swag_labs import SwagLabs


class TestSwagLabs:

    def test_check_icon(self, driver):


        swag_page = SwagLabs(driver)
        swag_page.visit()

        assert swag_page.exist_icon(), "Иконка не найдена на странице"

    def test_check_username_field(self, driver):


        swag_page = SwagLabs(driver)
        swag_page.visit()


        assert swag_page.exist_username_field(), "Поле имени не найдено на странице"

    def test_check_password_field(self, driver):


        swag_page = SwagLabs(driver)
        swag_page.visit()


        assert swag_page.exist_password_field(), "Поле пароля не найдено на странице"