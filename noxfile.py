import nox
import os


@nox.session()
def test(session: nox.Session):
    """Run unit tests under coverage (use `nocov` arg to run without coverage)"""
    session.install(
        'coverage',
        '.'
    )
    session.run('coverage', 'run', '-m', 'unittest', 'discover')


@nox.session()
def cov_report(session: nox.Session):
    """Combine coverage.py files and generate an XML report"""
    session.install(
        'coverage'
    )
    session.run('coverage', 'xml', '-i')


@nox.session()
def quality(session: nox.Session):
    session.install('flake8')
    session.run('flake8')


@nox.session()
def whl(session: nox.Session):
    """Build wheel (remember to build docs first)"""
    session.install(
        'wheel',
        'setuptools',
        '.'
    )
    session.run('python', '-m', 'setup', 'bdist_wheel')


@nox.session()
def send(session: nox.Session):
    """Send wheels from the `dist` folder to PyPI"""
    session.install(
        'twine'
    )
    token = os.environ.get("TWINE_TOKEN")
    if not token:
        raise ValueError("PyPi upload token not set!")
    session.run('twine', 'upload', 'dist/*.whl', '-u', '__token__', '-p')
