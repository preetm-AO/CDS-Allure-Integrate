import allure


@allure.suite("tests")
@allure.sub_suite("ABC")
@allure.title("test ABC")
def test_abc():
    assert False


@allure.suite("tests")
@allure.sub_suite("ABC")
@allure.title("test XYZ")
def test_xyz():
    assert True


@allure.suite("tests")
@allure.sub_suite("ABC")
@allure.title("test HAHA")
def test_haha():
    assert True
