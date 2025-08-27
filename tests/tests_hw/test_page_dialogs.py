from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    page = ModalDialogs(browser)
    page.visit()


    assert page.count_submenu_buttons() == 5, (f"Ожидалось 5 пунктов подменю, получено: {page.count_submenu_buttons()}" )


def test_navigation_modal(browser):
    page = ModalDialogs(browser)
    page.visit()

    browser.refresh()
    page.home_icon().click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()

    assert "https://demoqa.com/" in browser.current_url

    assert browser.title.strip().upper() == "DEMOQA"

    browser.set_window_size(1000, 1000)
