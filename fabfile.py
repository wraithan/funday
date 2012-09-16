from fabric.api import task, local, lcd


s3 = {
    'bucket': 'media.fundayroulette.com',
    'key': 'static',
}


@task
def deploy():
    local('git push heroku')
    local('heroku run ./manage.py migrate')
    local('./manage.py collectstatic --noinput')
    local('s3sync.rb -r --progress collectedstatic/ %(bucket)s:%(key)s' % s3)


@task
def style_check():
    ignored_dirs = ['migrations', 'settings', 'collectedstatic']
    local('pip install pyflakes pep8')
    ignore = ' '.join(['-not -ipath "*%s*"' % dir for dir in ignored_dirs])
    local('pyflakes `find . -iname "*.py" %s`' % ignore)
    local('pep8 . --exclude=%s' % ','.join(ignored_dirs))


@task
def build_docs():
    with lcd('docs'):
        local('pip install -r requirements.txt')
        local('make html')
