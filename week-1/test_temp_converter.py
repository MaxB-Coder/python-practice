import pytest

from temp_converter import cel_to_fahr, main


@pytest.mark.parametrize(
    ("temp_celsius", "expected_output"),
    [
        (-100.0, -148.0),
        (-50.0, -58.0),
        (-40.0, -40.0),
        (0.0, 32.0),
        (32.8, 91.04),
        (50.0, 122.0),
        (100.0, 212.0),
    ],
)
def test_converting_temps_correctly(
    temp_celsius: float, expected_output: float
) -> None:
    assert cel_to_fahr(temp_celsius) == pytest.approx(expected_output)


def test_main_prints_converted_temperature(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "100")

    main()

    assert capsys.readouterr().out == "212.0°F\n"


def test_main_rejects_non_numeric_input(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "abc")

    with pytest.raises(ValueError):
        main()
