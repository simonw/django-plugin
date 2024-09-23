from cookiecutter.main import cookiecutter
import pathlib

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_generated_files(tmpdir):
    generate(
        tmpdir,
        {
            "plugin_name": "django-foo",
            "description": "blah",
        },
    )
    assert paths(tmpdir) == {
        "django-foo/.github",
        "django-foo/tests/test_django_foo.py",
        "django-foo/.github/workflows/test.yml",
        "django-foo/.github/workflows",
        "django-foo/django_foo",
        "django-foo/.gitignore",
        "django-foo",
        "django-foo/pyproject.toml",
        "django-foo/.github/workflows/publish.yml",
        "django-foo/README.md",
        "django-foo/tests",
        "django-foo/LICENSE",
        "django-foo/django_foo/__init__.py",
    }


def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}
