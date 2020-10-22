import pytest
import allure
import sys


#安装allure程序 https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/allure-2.7.0.zip
def begin(input):
        print("begin")
def end(input):
    print("end")
@allure.feature("场景:A")
class TestAbb:
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")
    @allure.story("@pytest.mark.parametrize")
    @pytest.mark.parametrize("before,message,after",[(begin,"A",end),(end,"B",begin)])
    def test_chg00(self, before, message, after):
        before(message)
        print(message)
        after(message)

