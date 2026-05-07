from src.kb_builder.naming import make_id_slug_filename, slugify


def test_slugify_basic_names():
    assert slugify("Security Account Manager") == "security-account-manager"
    assert slugify("Command and Scripting Interpreter") == "command-and-scripting-interpreter"


def test_slugify_preserves_dots():
    assert slugify("certutil.exe") == "certutil.exe"
    assert slugify("T1003.002") == "t1003.002"


def test_id_slug_filename():
    assert (
        make_id_slug_filename("T1003.002", "Security Account Manager")
        == "T1003.002-security-account-manager.md"
    )


def test_ampersand_normalised():
    assert slugify("Command & Control") == "command-and-control"
