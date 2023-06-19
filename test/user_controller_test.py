import pytest

from src.controller.user_controller import UserController

class TestUserController:
    def test_ユーザーを登録できること(self):
        params = {"name": "田中", "tel": "090-1234-1234"}
        result = UserController().create(params)
        assert result["status"] == 201

    def test_ユーザーを指定したパラメータで登録できること(self):
        params = {"name": "田中", "tel": "090-1234-1111"}
        result = UserController().create(params)
        assert result["status"] == 201

    def test_名前が空文字列だとユーザーを登録ができないこと(self):
        params = {"name": "", "tel": "090-1234-1234"}
        result = UserController().create(params)
        assert result["status"] == 400
        assert result["error"] == "name is required"

    def test_名前がNoneだとユーザーを登録ができないこと(self):
        params = {"name": None, "tel": "090-1234-1234"}
        result = UserController().create(params)
        assert result["status"] == 400
        assert result["error"] == "name is required"

    def test_名前のkeyがないとユーザーを登録ができないこと(self):
        params = {"tel": "090-1234-1234"}
        result = UserController().create(params)
        assert result["status"] == 400
        assert result["error"] == "name is required"

    def test_telのkeyがなくてもユーザーを登録はできること(self):
        params = {"name": "山田"}
        result = UserController().create(params)
        assert result["status"] == 201

    def test_telが空文字でもユーザーを登録はできること(self):
        params = {"name": "田中", "tel": ""}
        result = UserController().create(params)
        assert result["status"] == 201

    def test_telがNoneでもユーザーを登録はできること(self):
        params = {"name": "田中", "tel": None}
        result = UserController().create(params)
        assert result["status"] == 201

    test_cases = [
        "09012341111",
        "090-12341111",
        "090-1234-1-111",
        "0901234--111",
        "-0901234-111",
        "0901234-111-",
        "090-12341-111",
        "0900-12341-111",
        "0900-12341-11111",
        "aaa-aaaa-aaaa",
    ]
    @pytest.mark.parametrize("tel", test_cases, ids=test_cases)
    def test_telは3桁4桁4桁のフォーマットでないとユーザー登録はできないこと(self, tel):
        params = {"name": "田中", "tel": tel}
        result = UserController().create(params)
        assert result["status"] == 400
        assert result["error"] == "電話番号のフォーマットはxxx-xxxx-xxxxにしてください"

