from pages.webtables import WebTables


def test_webtables_crud(browser):
    page = WebTables(browser)
    page.visit()

    start_rows = page.rows_count()

    page.open_add()
    assert page.modal_visible()

    page.submit()
    assert page.modal_visible()

    data = {
        "first": "Ivan",
        "last": "Petrov",
        "email": "ivan.petrov@test.tt",
        "age": 28,
        "salary": 120000,
        "dept": "QA"
    }
    page.fill_form(**data)
    page.submit()

    #диалог закрылся
    assert not page.modal_visible()

    #строк стало на 1 больше, данные совпали
    assert page.rows_count() == start_rows + 1
    assert page.last_row_values() == [
        data["first"], data["last"], str(data["age"]),
        data["email"], str(data["salary"]), data["dept"]
    ]

    #клик по карандашу — открылся диалог, данные предзаполнены
    page.edit_last_row()
    assert page.modal_visible()
    assert page.form_values() == [
        data["first"], data["last"], str(data["age"]),
        data["email"], str(data["salary"]), data["dept"]
    ]

    #меняем имя и сохраняем 
    new_first = "Pavel"
    page.fill_form(new_first, data["last"], data["email"], data["age"], data["salary"], data["dept"])
    page.submit()
    assert not page.modal_visible()
    vals = page.last_row_values()
    assert vals[0] == new_first

    #удаляем запись 
    page.delete_last_row()
    assert page.rows_count() == start_rows
